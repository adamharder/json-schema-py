# Base class for all JSON Schema objects
import jsonschema
import json

class JsonSchemaBase(object):

    def __init__(self):
        pass

    def validate(self, some_object):
        return jsonschema.validate(some_object, self.as_json)

    def __str__(self):
        return json.dumps(self.as_json, indent=2)