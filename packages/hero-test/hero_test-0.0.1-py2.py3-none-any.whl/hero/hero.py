from jsonschema import validate
import json


def test_validate(instance, schema):
    validate(instance, schema)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('test_schema.json', 'r') as schema_file:
        schema = json.load(schema_file)

    instance = {
        "id": "sfad"
    }
    test_validate(instance, schema)

