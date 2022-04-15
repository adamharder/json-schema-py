# an object schema ia an attempt to make a less verbose, and more simple schema syntax. We would also get the benfit of synbtax hiligting for data types

from easyjsonschema.schema_base import JsonSchemaBase
from easyjsonschema.schema_integer import JsonSchemaInteger
from easyjsonschema.schema_string import JsonSchemaString

from typing import List, Optional

class JsonSchemaObject(object):
    # required: type or enum
    def __init__(self):
        self._type=object
        self._required=[]
        self._properties={}
    @staticmethod
    def build()->"JsonSchemaObject":
        return JsonSchemaObject()


    #convenience function
    def add_string(self, *, 
        key:str, 
        required:bool,
        minLength:Optional[int]=None,
        maxLength:Optional[int]=None)->"JsonSchemaObject":
        return self.add(key=key, required=required, object=JsonSchemaString.build(minLength=minLength, maxLength=maxLength))

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






    def add(self, *, key:str, object:JsonSchemaBase, required:bool,):
        self._properties[key]=object
        if required:
            self._required.append(key)
        return self


    @property
    def as_json(self):
        r=dict(type="object")
        if len(self._required)>0:
            r.update(dict(required=list(set(self._required))))
        if len(self._properties)>0:
            r['properties']={}
            for key in self._properties:
                r["properties"][key]=self._properties[key].as_json
        return r


