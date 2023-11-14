from __future__ import annotations
from kye.compiled import CompiledDataset, CompiledEdge, CompiledType, TYPE_REF, EDGE
from typing import Optional

class Type:
    ref: TYPE_REF
    name: str
    indexes: list[list[EDGE]]
    extends: Optional[Type]
    edges: dict[EDGE, Edge]

    def __init__(self, name: TYPE_REF):
        self.ref = name
        self.name = name
        self.indexes = []
        self.extends = None
        self.edges = {}
    
    @property
    def has_edges(self) -> bool:
        return len(self.edges) > 0
    
    @property
    def has_index(self) -> bool:
        return len(self.indexes) > 0
    
    @property
    def base(self) -> Optional[Type]:
        return self.extends if self.extends else self

    @property
    def index(self) -> list[EDGE]:
        """ Flatten the 2d list of indexes """
        return [idx for idxs in self.indexes for idx in idxs]
    
    def __getitem__(self, name: EDGE) -> Edge:
        return self.edges[name]

    def __contains__(self, name: EDGE) -> bool:
        return name in self.edges
    
    def __iter__(self) -> iter[Edge]:
        return iter(self.edges.values())
    
    def __repr__(self):
        return "Type<{}>".format(self.ref)

class Edge:
    name: EDGE

    def __init__(self, name: EDGE, edge: CompiledEdge, model: DefinedType):
        self.ref = model.ref + '.' + name
        self.name = name
        self._edge = edge
        self._model = model
    
    @property
    def multiple(self) -> bool:
        return self._edge.multiple
    
    @property
    def nullable(self) -> bool:
        return self._edge.nullable
    
    @property
    def is_index(self) -> bool:
        return self.name in self._model.index
    
    @property
    def type(self) -> Type:
        return self._model._models[self._edge.type]
    
    def __repr__(self):
        return 'Edge<{}:{}{}>'.format(
            self.ref,
            self.type.name or '',
            ([['' ,'+'],
              ['?','*']])[int(self.nullable)][int(self.multiple)]
        )

class DefinedType(Type):
    def __init__(self, ref: TYPE_REF, type: CompiledType, models: Models):
        self.ref = ref
        self._type = type
        self._models = models

        self.edges = {
            name: Edge(name, edge, self)
            for name, edge in self._type.edges.items()
        }
        for parent in self.parents():
            for edge in parent.edges.values():
                if edge.name not in self.edges:
                    self.edges[edge.name] = edge
    
    @property
    def name(self):
        return self._type.name if self._type.name else self.extends.name

    @property
    def indexes(self):
        return self._type.indexes if self._type.indexes else self.extends.indexes
    
    @property
    def extends(self):
        return self._models[self._type.extends] if self._type.extends else None

    def parents(self):
        if self.extends:
            return [ self.extends ] + self.extends.parents()
        return []
    
    def __repr__(self):
        return repr(self._type)

class Models:
    globals = {
        'Number': Type('Number'),
        'String': Type('String'),
        'Boolean': Type('Boolean'),
        'Struct': Type('Struct'),
        'Model': Type('Model'),
    }

    def __init__(self, models: CompiledDataset):
        self._models = models

    def __getitem__(self, ref: TYPE_REF):
        if ref in self.globals:
            return self.globals[ref]
        if ref in self._models:
            return DefinedType(ref, self._models[ref], self)
        raise KeyError(ref)

    def __contains__(self, ref: TYPE_REF):
        return ref in self.globals or ref in self._models
    
    def __repr__(self):
        return repr(self._models)