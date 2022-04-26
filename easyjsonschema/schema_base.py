# Base class for all JSON Schema objects
import jsonschema
import json

class JsonSchemaBase(object):

    def __init__(self):
        pass

    def validate(self, some_object):
        jsonschema.validate(some_object, self.as_json)
    def is_valid(self, some_object)->bool:
        try:
            jsonschema.validate(some_object, self.as_json)
        
        except jsonschema.ValidationError as e:
            return False
        except Exception as e:
            raise e
        return True

    def __str__(self):
        return json.dumps(self.as_json, indent=2)