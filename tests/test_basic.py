
import pytest
import json
import easyjsonschema
from easyjsonschema.schema_array import JsonSchemaArray

from easyjsonschema.schema_object import JsonSchemaObject
from easyjsonschema.schema_integer import JsonSchemaInteger
from easyjsonschema.schema_string import JsonSchemaString
# from .schema_string import schema_string
from jsonschema import ValidationError

def test_schema_array():
    print(JsonSchemaArray.build_array_of_any().as_json)



def test():
    import pytest
    assert JsonSchemaArray.build_str_array().as_json == dict(type="array", items=dict(type="string"))
    assert JsonSchemaArray.build_str_array( minItems=10).as_json == dict(type="array", minItems= 10, items=dict(type="string"))

    JsonSchemaArray.build_str_array().validate([])  # should pass
    JsonSchemaArray.build_str_array().validate(["1"])  # should pass
    with pytest.raises(ValidationError):
        JsonSchemaArray.build_str_array().validate([1])  # should fail
    with pytest.raises(ValidationError):
        JsonSchemaArray.build_str_array().validate({})  # should fail
    with pytest.raises(ValidationError):
        JsonSchemaArray.build_str_array(minItems=10).validate([])  # should fail
    coord_array=JsonSchemaArray.build_number_array(minItems=2, maxItems=2)
    coord = JsonSchemaArray.build_array_of_objects(inner_items=coord_array)
    #print(json.dumps(coord.as_json, indent=2))
    with pytest.raises(ValidationError):
        coord.validate([1,"b"])  # should fail
    with pytest.raises(ValidationError):
        coord.validate([[1,2,3]])  # should fail
    with pytest.raises(ValidationError):
        coord.validate([1,2])  # should fail
    coord.validate([[1,2]])  # should pass





def test_schema_object():
    print(JsonSchemaObject.build().as_json)
    # print(str(JsonSchemaString.build()))
    assert dict(  type= "object") == JsonSchemaObject.build().as_json
def test_schema_string():
    # print(JsonSchemaString.build().as_json)
    # print(str(JsonSchemaString.build()))
    assert dict(  type= "string") == JsonSchemaString.build().as_json
def test_schema_integer():
    # print(JsonSchemaInteger.build(multipleOf=5).as_json)
    # print(str(JsonSchemaInteger.build(multipleOf=5)))
    assert dict(  type= "integer",  multipleOf= 5) == JsonSchemaInteger.build(multipleOf=5).as_json
#     test_obj=JsonSchemaObject()
#     test_obj.add(key="house_number", required=True, some_object =JsonSchemaInteger.build(multipleOf=5))
#     with pytest.raises(easyjsonschema.ValidationError):
#         xx = test_obj.validate(dict(house_number = 22))

#     test_obj=schema_object()
#     test_obj.add(key="house_number", required=True, some_object= schema_integer.build(multipleOf=5, minimum=90))

#     with pytest.raises(easyjsonschema.ValidationError):
#         xx = test_obj.validate(dict(house_number = 20))
#     with pytest.raises(easyjsonschema.SchemaError):
#         test_obj=schema_object()
#         test_obj.add(key="house_number", required=True, some_object= schema_integer.build(multipleOf=5, minimum=90, exclusiveMinimum=45))
    
#     xx = test_obj.validate(dict(house_number = 100))

# def test_schema_string():
#     print(">>>>>")
#     test_obj=schema_object()
#     with pytest.raises(easyjsonschema.ValidationError):
#         test_obj.add(key="street", required=True, some_object= schema_string.build(minLength=20, maxLength=10))
#     test_obj.add(key="street", required=True, some_object= schema_string.build(minLength=10, maxLength=20))
#     xx = test_obj.validate(dict(street = "some street 123"))
#     with pytest.raises(easyjsonschema.ValidationError):
#         xx = test_obj.validate(dict(street = "some ave"))
#     with pytest.raises(easyjsonschema.ValidationError):
#         xx = test_obj.validate(dict(street = "some ave12345678901234567890"))

