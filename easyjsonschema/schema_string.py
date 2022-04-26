# an object schema ia an attempt to make a less verbose, and more simple schema syntax. We would also get the benfit of synbtax hiligting for data types

from easyjsonschema.schema_base import JsonSchemaBase
from easyjsonschema.schema_utils import optional_int_check
from typing import List, Optional
import jsonschema


class JsonSchemaString(JsonSchemaBase):

    @staticmethod
    def build(*,
        minLength:Optional[int]=None,
        maxLength:Optional[int]=None,
        can_be_null:bool=False,
    )->"JsonSchemaString":
        optional_int_check(minLength)
        optional_int_check(maxLength)
        if minLength is not None:
            if maxLength is not None:
                if maxLength < minLength:
                    raise jsonschema.ValidationError(f"maxLength({maxLength}) < minLength({minLength})")
        r=JsonSchemaString()
        r._type=str
        r._minLength=minLength
        r._maxLength=maxLength
        r._can_be_null=can_be_null
        return r

    @property
    def as_json(self):
        _type="string"
        if self._can_be_null:
            _type=["string", "null"]
        r=dict(type=_type,
        minLength=self._minLength,
        maxLength=self._maxLength,
        )
        for key in list(r.keys()):
            if r[key] is None:
                r.pop(key)
        return r
