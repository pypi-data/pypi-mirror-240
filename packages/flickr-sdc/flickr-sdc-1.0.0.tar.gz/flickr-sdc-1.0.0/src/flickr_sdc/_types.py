"""
Definitions for Wikidata structured data entities.

We don't do any validation beyond the structure of the types --
this allows us to write type-checked Python, which makes it much
easier to write certain operations.

e.g. we can compare two snaks (one we want to write, one that exists)
and be sure we know what fields are/aren't defined, rather than
writing overly defensive code at every step.

These types aren't as strict as Wikidata itself, but we're not
trying to replace Wikidata validation, just allow ourselves to
write sensible validation logic.
"""

from typing import Any, Dict, List, Literal, NotRequired, TypedDict, TypeVar, Union

from pydantic import ConfigDict, TypeAdapter


# Definitions for the Wikidata entities that we create as part of
# this library for new photos.
#
# Notable, these entities omit a couple of fields on the main entities,
# in particular rank and ID.
#
# This is based on the table structured as described in
# https://www.wikidata.org/wiki/Help:Wikidata_datamodel


# -> datavalue
#
#     -> type: wikibase-entityid
#        value:
#          entity type: item
#          numeric-id
#
#     -> type: string
#        value (string/image/url)
#
#     -> type: time
#        value
#          time
#          precision
#          before
#          after
#          timezone
#          calendarmodel
#
#     -> type: globecoordinate
#          latitude
#          longitude
#          precision
#          globe
#          altitude (not documented but present in data model)
#
#     -> type: quantity
#          amount
#          lowerBound (not yet seen in responses)
#          upperBound (not yet seen in responses)
#          unit
#
#     -> type: monolingualtext
#          text
#          language
#
class Value:
    WikibaseEntityId = TypedDict(
        "WikibaseEntityId",
        {"entity-type": Literal["item"], "id": str, "numeric-id": int},
    )
    Time = TypedDict(
        "Time",
        {
            "time": str,
            "precision": int,
            "before": int,
            "after": int,
            "timezone": int,
            "calendarmodel": str,
        },
    )
    GlobeCoordinate = TypedDict(
        "GlobeCoordinate",
        {
            "latitude": float,
            "longitude": float,
            "precision": float,
            "globe": str,
            "altitude": Literal[None],
        },
    )
    Quantity = TypedDict("Quantity", {"amount": str, "unit": str})
    MonolingualText = TypedDict("MonolingualText", {"text": str, "language": str})


class DataValueTypes:
    WikibaseEntityId = TypedDict(
        "WikibaseEntityId",
        {"type": Literal["wikibase-entityid"], "value": Value.WikibaseEntityId},
    )
    String = TypedDict("String", {"type": Literal["string"], "value": str})
    Time = TypedDict("Time", {"type": Literal["time"], "value": Value.Time})
    GlobeCoordinate = TypedDict(
        "GlobeCoordinate",
        {"type": Literal["globecoordinate"], "value": Value.GlobeCoordinate},
    )
    Quantity = TypedDict(
        "Quantity", {"type": Literal["quantity"], "value": Value.Quantity}
    )
    MonolingualText = TypedDict(
        "MonolingualText",
        {"type": Literal["monolingualtext"], "value": Value.MonolingualText},
    )


DataValue = Union[
    DataValueTypes.WikibaseEntityId,
    DataValueTypes.String,
    DataValueTypes.Time,
    DataValueTypes.GlobeCoordinate,
    DataValueTypes.Quantity,
    DataValueTypes.MonolingualText,
]


# -> snak
#
#    -> property: pxx
#    -> snaktype: value / somevalue / novalue
#    -> (datavalue) ->
#
class Snak(TypedDict):
    property: str
    snaktype: Literal["value", "somevalue", "novalue"]
    datavalue: NotRequired[DataValue]
    hash: NotRequired[str]


# -> claims
#
# pxx
#   0..*
#     id
#     rank
#     type = statement
#     mainsnak -> snak
#     (qualifiers-order)
#     (qualifiers)
#     (references)
#
# We don't use references for Flickr SDC, but we should make sure we never
# delete references which have been saved by other users/tools.
#
NewStatement = TypedDict(
    "NewStatement",
    {
        "type": Literal["statement"],
        "mainsnak": Snak,
        "qualifiers-order": NotRequired[List[str]],
        "qualifiers": NotRequired[Dict[str, List[Snak]]],
    },
)


class ExistingStatement(NewStatement):
    id: str
    rank: str


class NewClaims(TypedDict):
    claims: List[NewStatement]


ExistingClaims = Dict[str, List[ExistingStatement]]


# Definitions for classes and functions in this library.


class GetSdcResponse(TypedDict):
    lastrevid: int
    statements: ExistingClaims


class UpdateSdcResponse(TypedDict):
    revisionid: int


T = TypeVar("T")


def validate_typeddict(t: Any, model: type[T]) -> T:
    """
    Check that some data matches a TypedDict.

    We use this to check that the structured data we receive
    from Wikimedia matches our definitions, so we can use it
    in type-checked Python.

    See https://stackoverflow.com/a/77386216/1558022
    """
    model.__pydantic_config__ = ConfigDict(extra="forbid")  # type: ignore
    TypedDictValidator = TypeAdapter(model)
    return TypedDictValidator.validate_python(t, strict=True)
