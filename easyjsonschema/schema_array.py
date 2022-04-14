from .schema_integer import JsonSchemaInteger
from .schema_string import JsonSchemaString
from .schema_base import JsonSchemaBase
from .schema_utils import optional_int_check, optional_bool_check
from jsonschema import ValidationError
from typing import Optional, Union
import json

# The schema_array is an attempt to make a less verbose, and more simple schema syntax. 
# We would also get the benfit of synbtax hiligting for data types
"""
Array of Numbers:
{
  "type": "array",
  "items": {
    "type": "number"
  }
}

array of 2 or 3 numbers
{
  "type": "array",
  "items": {
    "type": "number"
  }
  "minContains": 2,
  "maxContains": 3
}



"""
class JsonSchemaArray(JsonSchemaBase):
    @staticmethod
    def build_number_array(*, 
            inner_items:Optional[JsonSchemaInteger]=None, 
            minItems:Optional[int]=None,
            maxItems:Optional[int]=None,
            unqueItems:Optional[bool]=None)->"JsonSchemaArray":

        if inner_items is None:
            inner_items=JsonSchemaInteger.build()
        return JsonSchemaArray._build(inner_items=inner_items, minItems=minItems, maxItems=maxItems, unqueItems=unqueItems)
    @staticmethod
    def build_str_array(*, 
        inner_items:Optional[JsonSchemaString]=None, 
        minItems:Optional[int]=None,
        maxItems:Optional[int]=None,
        unqueItems:Optional[bool]=None)->"JsonSchemaArray":
        if inner_items is None:
            inner_items=JsonSchemaArray.build()
        return JsonSchemaArray._build(inner_items=inner_items, minItems=minItems, maxItems=maxItems, unqueItems=unqueItems)
    @staticmethod
    def build_array_of_objects(*, 
        inner_items:JsonSchemaBase, 
        minItems:Optional[int]=None,
        maxItems:Optional[int]=None,
        unqueItems:Optional[bool]=None)->"JsonSchemaArray":
        return JsonSchemaArray._build(inner_items=inner_items, minItems=minItems, maxItems=maxItems, unqueItems=unqueItems)
    @staticmethod
    def build_array_of_any(*, 
        minItems:Optional[int]=None,
        maxItems:Optional[int]=None,
        unqueItems:Optional[bool]=None)->"JsonSchemaArray":
        return JsonSchemaArray._build(inner_items=None, minItems=minItems, maxItems=maxItems, unqueItems=unqueItems)

    @staticmethod
    def _build(*,
        inner_items:str,
        minItems:Optional[int]=None,
        maxItems:Optional[int]=None,
        unqueItems:Optional[bool]=None
    )->"JsonSchemaArray":
        optional_int_check(minItems)
        optional_int_check(maxItems)
        optional_bool_check(unqueItems)
        if minItems is not None:
            if maxItems is not None:
                if maxItems < minItems:
                    raise ValidationError(f"maxItems({maxItems}) < minItems({minItems})")
        r=JsonSchemaArray()
        r._inner_items=inner_items
        r._minItems=minItems
        r._maxItems=maxItems
        r._unqueItems=unqueItems
        return r

    @property
    def as_json(self):
        r = dict(
            type="array",
            minItems=self._minItems,
            maxItems=self._maxItems,
            unqueItems=self._unqueItems,
            items={}
        )
        if self._inner_items is not None:
            r['items']=self._inner_items.as_json
            
        
        for key in list(r.keys()):
            if r[key] is None:
                r.pop(key)
        return r


