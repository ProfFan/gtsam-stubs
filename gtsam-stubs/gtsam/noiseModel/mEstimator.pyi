class Base:
    def __init__(self, *args, **kwargs) -> None: ...
    def print_(self, s: str) -> None: ...

class Cauchy(Base):
    def __init__(self, k: float) -> None: ...
    def Create(self, *args, **kwargs) -> Cauchy: ...
    def deserialize(self, serialized: str) -> None: ...
    def loss(self, error: float) -> float: ...
    def serialize(self) -> str: ...
    def weight(self, error: float) -> float: ...

class DCS(Base):
    def __init__(self, c: float) -> None: ...
    def Create(self, *args, **kwargs) -> DCS: ...
    def deserialize(self, serialized: str) -> None: ...
    def loss(self, error: float) -> float: ...
    def serialize(self) -> str: ...
    def weight(self, error: float) -> float: ...

class Fair(Base):
    def __init__(self, c: float) -> None: ...
    def Create(self, *args, **kwargs) -> Fair: ...
    def deserialize(self, serialized: str) -> None: ...
    def loss(self, error: float) -> float: ...
    def serialize(self) -> str: ...
    def weight(self, error: float) -> float: ...

class GemanMcClure(Base):
    def __init__(self, c: float) -> None: ...
    def Create(self, *args, **kwargs) -> GemanMcClure: ...
    def deserialize(self, serialized: str) -> None: ...
    def loss(self, error: float) -> float: ...
    def serialize(self) -> str: ...
    def weight(self, error: float) -> float: ...

class Huber(Base):
    def __init__(self, k: float) -> None: ...
    def Create(self, *args, **kwargs) -> Huber: ...
    def deserialize(self, serialized: str) -> None: ...
    def loss(self, error: float) -> float: ...
    def serialize(self) -> str: ...
    def weight(self, error: float) -> float: ...

class L2WithDeadZone(Base):
    def __init__(self, k: float) -> None: ...
    def Create(self, *args, **kwargs) -> L2WithDeadZone: ...
    def deserialize(self, serialized: str) -> None: ...
    def loss(self, error: float) -> float: ...
    def serialize(self) -> str: ...
    def weight(self, error: float) -> float: ...

class Null(Base):
    def __init__(self) -> None: ...
    def Create(self, *args, **kwargs) -> Null: ...
    def deserialize(self, serialized: str) -> None: ...
    def loss(self, error: float) -> float: ...
    def serialize(self) -> str: ...
    def weight(self, error: float) -> float: ...

class Tukey(Base):
    def __init__(self, k: float) -> None: ...
    def Create(self, *args, **kwargs) -> Tukey: ...
    def deserialize(self, serialized: str) -> None: ...
    def loss(self, error: float) -> float: ...
    def serialize(self) -> str: ...
    def weight(self, error: float) -> float: ...

class Welsch(Base):
    def __init__(self, k: float) -> None: ...
    def Create(self, *args, **kwargs) -> Welsch: ...
    def deserialize(self, serialized: str) -> None: ...
    def loss(self, error: float) -> float: ...
    def serialize(self) -> str: ...
    def weight(self, error: float) -> float: ...
