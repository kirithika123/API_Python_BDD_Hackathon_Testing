import json
import jsonschema
from jsonschema import validate


def get_schema(jsonfilePath):
    """This function loads the given schema available"""
    with open(jsonfilePath, 'r') as file:
        schema = json.load(file)
    return schema


def validate_json(json_data,jsonfilePath):
    """REF: https://json-schema.org/ """
    # Describe what kind of json you expect.
    execute_api_schema = get_schema(jsonfilePath)

    try:
        validate(instance=json_data, schema=execute_api_schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is InValid"
        return False, err

    message = "Given JSON data is Valid"
    return True, message


