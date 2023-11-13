__version__ = "1.0.0"


from ._types import (
    DataValue,
    ExistingClaims,
    ExistingStatement,
    NewClaims,
    NewStatement,
    Snak,
    Value,
)
from .structured_data import create_sdc_claims_for_flickr_photo
from .wikidata import WikidataEntities, WikidataProperties
from .wikimedia import (
    WikimediaSdcApi,
    WikimediaApiException,
    UnknownWikimediaApiException,
    NotFoundException,
)


__all__ = [
    "create_sdc_claims_for_flickr_photo",
    "DataValue",
    "ExistingClaims",
    "ExistingStatement",
    "NewClaims",
    "NewStatement",
    "NotFoundException",
    "Snak",
    "UnknownWikimediaApiException",
    "Value",
    "WikimediaApiException",
    "WikimediaSdcApi",
    "WikidataEntities",
    "WikidataProperties",
]
