from jsonschema import validate
import json
import pkgutil


def test_validate(instance):
    resources = pkgutil.get_data('hero', 'inner/test_schema.json')
    schema = json.loads(resources)
    validate(instance, schema)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    instance = {
        "id": "sfad"
    }
    test_validate(instance)

