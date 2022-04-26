# an object schema ia an attempt to make a less verbose, and more simple schema syntax. We would also get the benfit of synbtax hiligting for data types

from easyjsonschema.schema_base import JsonSchemaBase
from easyjsonschema.schema_integer import JsonSchemaInteger
from easyjsonschema.schema_string import JsonSchemaString

from typing import List, Optional

class JsonSchemaObject(JsonSchemaBase):
    # required: type or enum
    def __init__(self, additional_properties:bool=False):
        self._type=object
        self._required=[]
        self._properties={}
        self._additional_properties=additional_properties
    @staticmethod
    def build(additional_properties:bool=False)->"JsonSchemaObject":
        return JsonSchemaObject(additional_properties=additional_properties)


    #convenience function
    def add_string(self, *, 
        key:str, 
        required:bool,
        minLength:Optional[int]=None,
        maxLength:Optional[int]=None,
        can_be_null=False)->"JsonSchemaObject":
        return self.add(key=key, required=required, object=JsonSchemaString.build(minLength=minLength, maxLength=maxLength, can_be_null=can_be_null))

    def add_strings(self, *, keys:List[str], required:bool)->"JsonSchemaObject":
        for key in keys:
            self.add_string(key=key, required=required)
        return self


    #convenience function
    def add_integer(self, *, 
        key:str, 
        required:bool,
        multipleOf:Optional[int]=None,
        minimum:Optional[int]=None,
        maximum:Optional[int]=None,
        exclusiveMinimum:Optional[int]=None,
        exclusiveMaximum:Optional[int]=None)->"JsonSchemaObject":

        return self.add(
            key=key, 
            required=required, 
            object=JsonSchemaInteger.build(
                multipleOf=multipleOf,
                minimum=minimum,
                maximum=maximum,
                exclusiveMinimum=exclusiveMinimum,
                exclusiveMaximum=exclusiveMaximum))




    def remove(self, *, key:str):
        if key in self._properties:
            self._properties.pop(key)
        if key in self._required: 
            self._required.remove(key)
        return self


    def add(self, *, key:str, object:JsonSchemaBase, required:bool,):
        self._properties[key]=object
        if required:
            self._required.append(key)
        return self


    @property
    def as_json(self):
        r=dict(type="object", additionalProperties=self._additional_properties)
        if len(self._required)>0:
            r.update(dict(required=list(set(self._required))))
        if len(self._properties)>0:
            r['properties']={}
            # print("__________________________")
            for key in self._properties:
                # print("2 ____________________")
                # print(key)
                # print(type(self._properties[key]))
                # print(self._properties[key].as_json)
                r["properties"][key]=self._properties[key].as_json
        return r


