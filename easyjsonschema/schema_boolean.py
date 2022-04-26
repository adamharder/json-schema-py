# An object schema ia an attempt to make a less verbose,
# and more simple JSON schema syntax. We would also get the benfit of synbtax hiligting for data types

from typing import List, Optional
from .schema_base import JsonSchemaBase

class JsonSchemaBoolean(JsonSchemaBase):
    @staticmethod
    def build():
        r = JsonSchemaBoolean()
        r._type=bool

        return r

    @property
    def as_json(self):
        return dict(type="boolean")


