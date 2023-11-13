import datetime
import re

from ._types import DataValueTypes, Snak


class WikidataProperties:
    """
    Named constants for Wikidata property names.
    """

    # To see documentation for a particular property, go to
    # https://www.wikidata.org/wiki/Property:<PROPERTY_ID>
    #
    # e.g. https://www.wikidata.org/wiki/Property:P2093
    Operator = "P137"
    AppliesToJurisdiction = "P1001"
    Creator = "P170"
    DescribedAtUrl = "P973"
    DeterminationMethod = "P459"
    AuthorName = "P2093"
    FlickrPhotoId = "P12120"
    FlickrUserId = "P3267"
    Url = "P2699"
    SourceOfFile = "P7482"
    CopyrightLicense = "P275"
    CopyrightStatus = "P6216"
    Inception = "P571"
    PublicationDate = "P577"
    PublishedIn = "P1433"
    SourcingCircumstances = "P1480"


class WikidataEntities:
    """
    Named constants for certain Wikidata entities.
    """

    # To see documentation for a particular property, go to
    # https://www.wikidata.org/wiki/<ENTITY_ID>
    #
    # e.g. https://www.wikidata.org/wiki/Q103204
    Circa = "Q5727902"
    Copyrighted = "Q50423863"
    FileAvailableOnInternet = "Q74228490"
    Flickr = "Q103204"
    GregorianCalendar = "Q1985727"
    PublicDomain = "Q19652"
    StatedByCopyrightHolderAtSourceWebsite = "Q61045577"
    UnitedStatesOfAmerica = "Q30"
    WorkOfTheFederalGovernmentOfTheUnitedStates = "Q60671452"

    # We only map the license types used by Flickypedia -- we should
    # never be creating SDC for e.g. CC BY-NC.
    Licenses = {
        "cc-by-2.0": "Q19125117",
        "cc-by-sa-2.0": "Q19068220",
        "cc0-1.0": "Q6938433",
        "usgov": "Q60671452",
        "pdm": "Q19652",
    }


def to_wikidata_date_value(
    d: datetime.datetime, *, precision: str
) -> DataValueTypes.Time:
    """
    Convert a Python native-datetime to the Wikidata data model.

    See https://www.wikidata.org/wiki/Help:Dates#Precision
    """
    if precision not in ("day", "month", "year"):
        raise ValueError("Unrecognised precision: {precision}")

    # This is the timestamp, e.g. ``+2023-10-11T00:00:00Z``.
    #
    # We zero the hour/minute/second even if we have that precision
    # in our datetime because of a limitation in Wikidata.
    # In particular, as of 12 October 2023:
    #
    #     "time" field can not be saved with precision higher
    #     than a "day".
    #
    # If Wikidata ever relaxes this restriction, we could revisit
    # this decision.
    time_str = {
        "day": d.strftime("+%Y-%m-%dT00:00:00Z"),
        "month": d.strftime("+%Y-%m-00T00:00:00Z"),
        "year": d.strftime("+%Y-00-00T00:00:00Z"),
    }[precision]

    # This is the numeric value of precision used in the Wikidata model.
    #
    # See https://www.wikidata.org/wiki/Help:Dates#Precision
    precision_value = {"day": 11, "month": 10, "year": 9}[precision]

    # This is the numeric offset from UTC in minutes.  All the timestamps
    # we get from Flickr are in UTC, so we can default this to 0.
    timezone = 0

    # These are qualifiers for how many units before/after the given time
    # we could be, execpt they're not actually used by Wikidata.
    # As of 12 October 2023:
    #
    #     We do not use before and after fields and use qualifiers
    #     instead to indicate time period.
    #
    # But the API returns an error if you try to post a date without these,
    # so we include default values.
    before = after = 0

    # This tells Wikidata which calendar we're using.
    #
    # Although this is the default, the API throws an error if you try
    # to store a date without it, so we include it here.
    calendarmodel = (
        f"http://www.wikidata.org/entity/{WikidataEntities.GregorianCalendar}"
    )

    return {
        "value": {
            "time": time_str,
            "precision": precision_value,
            "timezone": timezone,
            "before": before,
            "after": after,
            "calendarmodel": calendarmodel,
        },
        "type": "time",
    }


def to_wikidata_entity_value(*, entity_id: str) -> DataValueTypes.WikibaseEntityId:
    """
    Create a datavalue for a Wikidata entity.
    """
    assert re.match(r"^Q[0-9]+$", entity_id)

    return {
        "value": {
            "id": entity_id,
            "entity-type": "item",
            "numeric-id": int(entity_id.replace("Q", "")),
        },
        "type": "wikibase-entityid",
    }


def to_wikidata_entity_snak(*, property_id: str, entity_id: str) -> Snak:
    """
    Create a snak for a Wikidata entity.
    """
    return {
        "datavalue": to_wikidata_entity_value(entity_id=entity_id),
        "property": property_id,
        "snaktype": "value",
    }
