import json
from typing import Dict, Optional, Union

import httpx

from ._types import GetSdcResponse, NewStatement, UpdateSdcResponse, validate_typeddict


class WikimediaSdcApi:
    def __init__(self, client: httpx.Client) -> None:
        self.client = client

    def _request(
        self,
        *,
        method: str,
        params: Optional[Dict[str, str]] = None,
        data: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None,
    ) -> httpx.Response:
        resp = self.client.request(
            method,
            url="https://commons.wikimedia.org/w/api.php",
            params=params,
            data=data,
            timeout=timeout,
        )

        # When something goes wrong, we get an ``error`` key in the response.
        #
        # Detect this here and throw an exception, so callers can assume
        # there was no issue if this returns cleanly.
        #
        # See https://www.mediawiki.org/wiki/Wikibase/API#Response
        try:
            raise UnknownWikimediaApiException(resp)
        except KeyError:
            pass

        return resp

    def _get(self, params: Dict[str, str]) -> httpx.Response:
        return self._request(method="GET", params=params)

    def _post(
        self, data: Dict[str, Union[str, int, bool]], timeout: Optional[int] = None
    ) -> httpx.Response:
        return self._request(
            method="POST",
            data={**data, "token": self.get_csrf_token()},  # type: ignore
            timeout=timeout,
        )

    def get_csrf_token(self) -> str:
        """
        Get a CSRF token from the Wikimedia API.

        This is required for certain API actions that modify data in
        Wikimedia.  External callers are never expected to use this,
        but functions from this class will call it when they need a token.

        See https://www.mediawiki.org/wiki/API:Tokens
        """
        resp = self._get(
            params={
                "action": "query",
                "meta": "tokens",
                "type": "csrf",
                "format": "json",
            }
        )

        return resp.json()["query"]["tokens"]["csrftoken"]  # type: ignore

    def get_structured_data(self, *, page_id: str) -> GetSdcResponse:
        """
        Retrieve the structured data for a file on Wikimedia Commons.

        See https://commons.wikimedia.org/wiki/Commons:Structured_data
        See https://www.wikidata.org/w/api.php?modules=wbgetentities&action=help

        """
        try:
            resp = self._get(
                params={
                    "action": "wbgetentities",
                    "sites": "commonswiki",
                    "ids": page_id,
                    "format": "json",
                }
            )
        except UnknownWikimediaApiException as exc:
            if exc.code == "no-such-entity":
                raise NotFoundException(f"Could not find a page with ID {page_id}")
            else:  # pragma: no cover
                raise

        page = resp.json()["entities"][page_id]

        result = {
            "lastrevid": page["lastrevid"],
            "statements": page["statements"],
        }

        return validate_typeddict(result, model=GetSdcResponse)

    def update_statement(
        self,
        *,
        statement_id: str,
        update_statement: NewStatement,
        summary: str,
        baserevid: int
    ) -> UpdateSdcResponse:
        """
        Update a single statement for a file on Wikimedia Commons.

        This is useful when you want to edit an existing file on Commons,
        for example adding qualifiers to an existing statement.

        Note: this function *requires* that you pass the ID of the
        revision you're modifying, or it will fail.

        See https://www.wikidata.org/w/api.php?action=help&modules=wbsetclaim

        """
        resp = self._post(
            data={
                "action": "wbsetclaim",
                "claim": json.dumps({"id": statement_id, **update_statement}),
                "summary": summary,
                "bot": True,
                "baserevid": baserevid,
                "format": "json",
            }
        )

        return {"revisionid": resp.json()["pageinfo"]["lastrevid"]}


class WikimediaApiException(Exception):
    pass


class UnknownWikimediaApiException(WikimediaApiException):
    def __init__(self, resp: httpx.Response) -> None:
        error_info = resp.json()["error"]

        self.code = error_info.get("code")
        self.error_info = error_info
        super().__init__(error_info["info"])


class NotFoundException(WikimediaApiException):
    """
    Thrown when you try to look up something that doesn't exist.
    """

    pass
