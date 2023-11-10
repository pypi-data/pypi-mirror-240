from unittest.mock import patch
import json

from tests.utils import fixtures_path
from hestia_earth.validation.validators.indicator import (
    validate_characterisedIndicator_model,
    validate_landTransformation
)

class_path = 'hestia_earth.validation.validators.indicator'
models = ['ipcc2007']


@patch(f"{class_path}.get_methodModels", return_value=models)
def test_validate_characterisedIndicator_model_valid(*args):
    # no infrastructure should be valid
    assert validate_characterisedIndicator_model({}, 'impacts') is True

    with open(f"{fixtures_path}/indicator/characterisedIndicator-methodModel/valid.json") as f:
        data = json.load(f)
    assert validate_characterisedIndicator_model(data, 'impacts') is True


@patch(f"{class_path}.get_methodModels", return_value=models)
def test_validate_characterisedIndicator_model_invalid(*args):
    with open(f"{fixtures_path}/indicator/characterisedIndicator-methodModel/invalid.json") as f:
        data = json.load(f)
    assert validate_characterisedIndicator_model(data, 'impacts') == {
        'level': 'error',
        'dataPath': '.impacts[0].methodModel.@id',
        'message': 'is not allowed for this characterisedIndicator',
        'params': {
            'term': {
                '@type': 'Term',
                '@id': 'gwp20'
            },
            'model': {
                '@type': 'Term',
                '@id': 'ipcc2013'
            },
            'allowedValues': models
        }
    }


@patch(f"{class_path}.get_methodModels", return_value=models)
def test_validate_landTransformation_valid(*args):
    # no infrastructure should be valid
    assert validate_landTransformation({}, 'emissionsResourceUse') is True

    with open(f"{fixtures_path}/indicator/landTransformation/valid.json") as f:
        data = json.load(f)
    assert validate_landTransformation({'emissionsResourceUse': data['nodes']}, 'emissionsResourceUse') is True


@patch(f"{class_path}.get_methodModels", return_value=models)
def test_validate_landTransformation_invalid(*args):
    with open(f"{fixtures_path}/indicator/landTransformation/invalid.json") as f:
        data = json.load(f)
    assert validate_landTransformation({'emissionsResourceUse': data['nodes']}, 'emissionsResourceUse') == {
        'level': 'error',
        'dataPath': '.emissionsResourceUse[1].value',
        'message': 'must be less than or equal to land occupation',
        'params': {
            'current': 0.2
        }
    }
