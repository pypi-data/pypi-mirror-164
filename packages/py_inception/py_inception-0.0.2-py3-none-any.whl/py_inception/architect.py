from __future__ import annotations
from abc import ABC, abstractmethod
import types
from .abstract import AArchitect
from typing import Any

class CoreArchitect(AArchitect):
    """ Core Architect extract common information from object of any type """

    def parse(self, var: Any, parse_as: str = "object", *, metadata: dict | None = None):
        # CoreArchitect stops chain for "object" and "attr" 
        if parse_as in ("object", "attr") :
            return self.parse_object(var, metadata=metadata)

        return self.parse_next(var, parse_as, metadata=metadata)

    def parse_object(self, var: Any, *, metadata: dict | None = None):
        if self.e is None or self.e.maze is None:
            return

        id_ = id(var)
        maze = self.e.maze

        # Check if already parsed
        if id_ in maze.objects:
            return {"id": id_, "mode": "object"}

        obj: dict = {}
        maze.objects[id_] = obj

        try:
            obj["name"] = var.__name__
        except:
            pass
        
        try:
            obj["qualname"] = var.__qualname__
        except:
            pass

        try:
            obj["module"] = var.__module__
        except:
            pass
        
        try:
            obj["class"] = id(var.__class__)
            self.e.parse(var.__class__, "object")
        except:
            pass

        try:
            obj["mro"] = []
            for i in var.__mro__:
                obj["mro"].append(id(i))
                self.e.parse(i, "object")
        except:
            del obj["mro"]

        try:
            obj["bases"] = []
            for i in list(var.__bases__):
                obj["bases"].append(id(i))
                self.e.parse(i, "object")
        except:
            del obj["bases"]

        try:
            d = var.__dict__
            obj["dict"] = {}
            for i in d:
                res = self.e.parse(d[i], "attr", metadata={"object": var, "attr": i})
                if res is not None:
                    obj["dict"][i] = res
        except:
            pass

        return {"id": id_, "mode": "object"}


class StdTypesArchitect(AArchitect):
    """ StdTypes Architect extract data from python standard types objects:
        * Value: str, int, float, bool, None;
        * Sequence: list, set, frozenset, tuple
        * Array: dict
    
        Extract values for presentation in a convenient form.
    """
    
    def __init__(self, transparent: bool=False, **kwargs):
        super().__init__(**kwargs)
        self.transparent = transparent

    def parse(self, var: Any, parse_as: str = "object", *, metadata: dict | None = None):
        parsed = self.parse_stdtype(var, parse_as, metadata=metadata)
        
        # If not standard type var, pass to next Architect
        # If parsing as object - CoreArchitect must create full record in Maze
        if not parsed or parse_as == "object":
            return self.parse_next(var, parse_as, metadata=metadata)
        
        # Pass to next Architect in transparent mode
        # but returned data will be overwritten
        if self.transparent:
            self.parse_next(var, parse_as, metadata=metadata)

        return parsed

    def parse_stdtype(self, var: Any, parse_as: str = "object", *, metadata: dict | None = None):
        if self.e is None or self.e.maze is None:
            return

        id_ = id(var)
        maze = self.e.maze

        if type(var) == str:
            maze.strings[id_] = var
            return {"mode": "str", "type": "str", "id": id_}
        elif type(var) in (int, float):
            return {"mode": "dir", "type": type(var).__name__, "val": var}
        elif var is None:
            return {"mode": "dir", "type": "NoneType", "val": "None"}
        elif type(var) == bool:
            return {"mode": "dir", "type": "bool", "val": str(var)}
        elif type(var) in (list, set, frozenset, tuple):
            if id_ not in maze.lists:
                maze.lists[id_] = {"type": type(var).__name__, "items": []}
                for i in var:
                    maze.lists[id_]["items"].append(self.e.parse(i, "attr"))
            return {"mode": "list", "type": type(var).__name__, "id": id_, "len": len(var)}
        elif type(var) == dict:
            if id_ not in maze.dicts:
                maze.dicts[id_] = {"type": type(var).__name__, "items": []}
                for (i, j) in var.items():
                    maze.dicts[id_]["items"].append( (
                        self.e.parse(i, "attr"),
                        self.e.parse(j, "attr"),
                    ) )
            return {"mode": "dict", "type": type(var).__name__, "id": id_, "len": len(var)}
        return None


class FuncArchitect(AArchitect):
    """ Func Architect extract data from python standard functions """

    def __init__(self, transparent: bool=False, **kwargs):
        super().__init__(**kwargs)
        self.transparent = transparent

    def parse(self, var: Any, parse_as: str = "object", *, metadata: dict | None = None):
        parsed = self.parse_func(var, parse_as, metadata=metadata)
        
        # If not standard type var, pass to next Architect
        # If parsing as object - CoreArchitect must create full record in Maze
        if not parsed or parse_as == "object":
            return self.parse_next(var, parse_as, metadata=metadata)
        
        # Pass to next Architect in transparent mode
        # but returned data will be overwritten
        if self.transparent:
            self.parse_next(var, parse_as, metadata=metadata)

        return parsed

    def parse_func(self, var: Any, parse_as: str = "object", *, metadata: dict | None = None):
        if self.e is None or self.e.maze is None:
            return

        id_ = id(var)
        maze = self.e.maze
        func_types = (
            types.FunctionType,
            types.BuiltinMethodType,
            types.BuiltinFunctionType,
            types.MethodType,
            types.MethodDescriptorType,
            types.ClassMethodDescriptorType,
            types.MethodWrapperType,
            types.WrapperDescriptorType,
            types.GetSetDescriptorType,
            types.MemberDescriptorType,
        )

        if type(var) in func_types:
            return {"mode": "func", "type": type(var).__name__, "id": id_}
        
        return None
