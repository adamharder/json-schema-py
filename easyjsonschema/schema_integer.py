# An object schema ia an attempt to make a less verbose,
# and more simple JSON schema syntax. We would also get the benfit of synbtax hiligting for data types


from typing import List, Optional
from .schema_utils import optional_int_check
from .schema_base import JsonSchemaBase

import jsonschema


class JsonSchemaInteger(JsonSchemaBase):
    @staticmethod
    def build(*,
        multipleOf:Optional[int]=None,
        minimum:Optional[int]=None,
        maximum:Optional[int]=None,
        exclusiveMinimum:Optional[int]=None,
        exclusiveMaximum:Optional[int]=None)->"JsonSchemaInteger":
        r = JsonSchemaInteger()
        optional_int_check(multipleOf)
        optional_int_check(minimum)
        optional_int_check(maximum)
        optional_int_check(exclusiveMinimum)
        optional_int_check(exclusiveMaximum)
        optional_int_check(multipleOf)
        
        r._type=int
        r._multipleOf=multipleOf
        if None not in [minimum, exclusiveMinimum]: 
            # both cannot be non-null
            raise jsonschema.SchemaError(f"minimum = {minimum} and exclusiveMinimum = {exclusiveMinimum}. this makes no sense.")
        if None not in [maximum, exclusiveMaximum]:
            # both cannot be non-null
            raise jsonschema.SchemaError(f"maximum = {maximum} and exclusiveMaximum = {exclusiveMaximum}. this makes no sense.")

        if minimum is not None:
            if maximum is not None:
                assert maximum >= minimum
        
        if exclusiveMinimum is not None:
            if exclusiveMaximum is not None:
                assert exclusiveMaximum >= exclusiveMinimum
        r._minimum=minimum
        r._maximum=maximum
        r._exclusiveMinimum=exclusiveMinimum
        r._exclusiveMaximum=exclusiveMaximum
        return r

    @property
    def as_json(self):
        r=dict(type="integer",
        multipleOf=self._multipleOf,
        minimum=self._minimum,
        maximum=self._maximum,
        exclusiveMinimum=self._exclusiveMinimum,
        exclusiveMaximum=self._exclusiveMaximum,
        )
        for key in list(r.keys()):
            if r[key] is None:
                r.pop(key)

        return r


