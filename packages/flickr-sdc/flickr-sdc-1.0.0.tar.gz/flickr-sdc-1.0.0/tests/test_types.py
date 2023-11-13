import json
from typing import Any, TypedDict

from pydantic import ValidationError
import pytest

from flickr_sdc import ExistingClaims, Snak
from flickr_sdc._types import validate_typeddict


class Shape(TypedDict):
    color: str
    sides: int


@pytest.mark.parametrize(
    "data",
    [
        {"color": "red"},
        {"sides": 4},
        {"color": "red", "sides": "four"},
        {"color": (255, 0, 0), "sides": 4},
        {"color": "red", "sides": 4, "angle": 36},
    ],
)
def test_validate_typeddict_flags_incorrect_data(data: Any) -> None:
    with pytest.raises(ValidationError):
        validate_typeddict(data, model=Shape)


def test_validate_typeddict_allows_valid_data() -> None:
    validate_typeddict({"color": "red", "sides": 4}, model=Shape)


def test_snak_type_matches() -> None:
    data = {
        "snaktype": "value",
        "property": "P1684",
        "hash": "e9d3441f2099aec262278049bb9915eaf3fc20fb",
        "datavalue": {
            "value": {"text": "910", "language": "en"},
            "type": "monolingualtext",
        },
    }

    validate_typeddict(data, model=Snak)


@pytest.mark.parametrize(
    "filename",
    [
        "M76_P1071_entityid.json",
        "M76_P1259_globecoordinate.json",
        "M76_P6790_quantity.json",
        "M74469_P180_monolingualtext.json",
    ],
)
def test_existing_claims_match_type(filename: str) -> None:
    with open(f"tests/fixtures/structured_data/existing/{filename}") as infile:
        existing_statements = json.load(infile)

    validate_typeddict(existing_statements, model=ExistingClaims)
