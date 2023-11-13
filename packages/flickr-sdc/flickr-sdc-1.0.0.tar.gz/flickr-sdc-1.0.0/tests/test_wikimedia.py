import json

import pytest

from flickr_sdc import WikimediaSdcApi, NotFoundException


class TestGetStructuredData:
    def test_it_throws_if_page_does_not_exist(self, api: WikimediaSdcApi) -> None:
        with pytest.raises(NotFoundException):
            api.get_structured_data(page_id="-1")

    def test_can_get_structured_data(self, api: WikimediaSdcApi) -> None:
        actual = api.get_structured_data(page_id="M82559264")

        with open("tests/fixtures/expected_responses/sdc_M82559264.json") as infile:
            expected = json.load(infile)

        assert actual == {"lastrevid": 815799018, "statements": expected}


class TestCanUpdateStatement:
    def test_it_throws_if_page_does_not_exist(self, api: WikimediaSdcApi) -> None:
        resp = api.update_statement(
            statement_id="M138765501$F1460C84-9A20-4EA1-B203-82E30F4BEB3E",
            update_statement={
                "mainsnak": {
                    "datavalue": {
                        "type": "wikibase-entityid",
                        "value": {
                            "entity-type": "item",
                            "numeric-id": 19125117,
                            "id": "Q19125117",
                        },
                    },
                    "property": "P275",
                    "snaktype": "value",
                },
                "qualifiers": {
                    "P459": [
                        {
                            "datavalue": {
                                "type": "wikibase-entityid",
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 61045577,
                                    "id": "Q61045577",
                                },
                            },
                            "property": "P459",
                            "snaktype": "value",
                        }
                    ]
                },
                "qualifiers-order": ["P459"],
                "type": "statement",
            },
            summary="Add a qualifier for copyright license source",
            baserevid=820417926,
        )

        assert resp == {"revisionid": 820421461}
