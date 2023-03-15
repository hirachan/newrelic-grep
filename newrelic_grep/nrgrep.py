from __future__ import annotations
from typing import Optional
import sys
import os
import json
import datetime
import requests

URL = "https://api.newrelic.com/graphql"
API_KEY = os.environ["NR_API_KEY"]
ACCOUNT_ID = os.environ["NR_ACCOUNT_ID"]


def _escape_like(value: str) -> str:
    return value.replace("'", "\\'").replace("%", "\\%")


def _escape(value: str) -> str:
    return value.replace("'", "\\'")


def build_nrql(
        pattern: str,
        since: Optional[str] = None, until: Optional[str] = None,
        conditions: list[str] = [],
        regex: bool = False,
        limit: int = 0
    ) -> str:
    if not since:
        _since = "3 DAYS AGO"
    else:
        since += "20000101000000"[len(since):]
        _since = datetime.datetime.strptime(
            since, "%Y%m%d%H%M%S").strftime("'%Y-%m-%d %H:%M:%S +0900'")

    _limit = "MAX" if limit == 0 else str(limit)

    query = "SELECT * FROM Log WHERE message"
    if regex:
        query += f" RLIKE r'{_escape(pattern)}'"
    else:
        query += f" LIKE '%{_escape_like(pattern)}%'"
    for cond in conditions:
        key, val = cond.split(":")
        query += f" AND {key}='{_escape(val)}'"
    query += f" LIMIT {_limit} SINCE {_since}"
    if until:
        until += "20000101000000"[len(until):]
        _until = datetime.datetime.strptime(
            until, "%Y%m%d%H%M%S").strftime("'%Y-%m-%d %H:%M:%S +0900'")
        query += f" UNTIL {_until}"

    return query


def query(
        pattern: str,
        since: Optional[str],
        until: Optional[str],
        verbose: bool = False,
        attributes: list[str] = [],
        conditions: list[str] = [],
        regex: bool = False,
        limit: int = 0
    ) -> None:
    query = build_nrql(pattern, since, until, conditions, regex, limit)

    params = {
        "query": """
            {
              actor {
                account(id: %s) {
                  nrql(query: "%s", timeout: 120) {
                    results
                  }
                }
              }
            }
        """ % (ACCOUNT_ID, query)
    }

    if verbose:
        sys.stderr.write(f"NRQL: {query}\n")
        sys.stderr.write("GraphQL:")
        sys.stderr.write(params["query"])
        sys.stderr.write("\n")

    headers = {
        "Content-Type": "application/json",
        "API-Key": API_KEY,
    }

    r = requests.post(URL, json.dumps(params), headers=headers)

    res = r.json()

    if not res["data"]["actor"]["account"]["nrql"]:
        sys.stderr.write("\n".join([_["message"] for _ in res["errors"]]))
        sys.stderr.write("\n")
        sys.exit(2)

    for log in res["data"]["actor"]["account"]["nrql"]["results"][::-1]:
        for attribute in attributes:
            print(log.get(attribute, ""), end=":")
        else:
            print(log["message"])
