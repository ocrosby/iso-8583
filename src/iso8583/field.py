import re

from typing import Optional

from yaml import load

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

data = load(stream, Loader=Loader

class Field:
    definition: Optional[str]

    def __init__(self, definition: Optional[str] = None):
        self.definition = definition

    def is_alpha(self) -> bool:
        return re.match("^a.*$", self.definition) is not None

    def is_numeric(self) -> bool:
        return re.match("^n.*$", self.definition) is not None

    def is_lvar(self) -> bool:
        return self.definition[1] == 'l'

    def is_llvar(self) -> bool:
        return self.definition[1] == 'L'

    def is_lllvar(self) -> bool:
        return self.definition[1] == 'm'

    @property
    def type(self) -> str:
        if self.is_alpha():
            return 'alpha'
        elif self.is_numeric():
            return 'numeric'
        else:
            return 'unknown'


class FieldBuilder:
    _instance: Optional[Field]

    def __init__(self):
        self._instance = None

    def build(self):
        self._instance = Field()

    def build_definition(self, definition: str):
        self._instance.definition = definition

    def get_instance(self) -> Field:
        return self._instance
