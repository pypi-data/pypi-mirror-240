import sys
import argparse
import subprocess as sp
import json
import time
import requests
from typing import List, Dict, Any, Union


def post_json(
    url: str,
    json_or_str: Union[str, Dict[str, Any]],
    target_status: List[int] = list(range(200, 300)),
    retry: int = 0,
    sleep: float = 1,
    factor: float = 2.0,
    sleep_max: float = 0.0,
    stdout=None,
    stderr=None,
) -> requests.Response:
    """
    This call always returns a `requests.Response`, even if an exception is raised.
    Thses two fields are always set:
    - response.status_code (Contains the HTTP status code or `1` if an exception was raised.)
    - response.reason (Contains the HTTP message or the raised exception message.)
    """
    stdout = stdout or sys.stdout
    stderr = stderr or sys.stderr

    try:
        json_key = "json"
        if isinstance(json_or_str, str):
            json_key = "data"

        r = requests.post(url, **{json_key: json_or_str})

    except requests.exceptions.RequestException as e:
        if e.response:
            r = e.response
        else:
            r = requests.Response()
            r.status_code = 1
            r.reason = f"{e}"

    if retry != 0 and r.status_code not in target_status:
        if retry > 0:
            sleep_duration = round(sleep, 2)

            stderr.write(
                f"HTTP POST request failed. Retry in {sleep_duration} seconds\n"
            )

            time.sleep(sleep_duration)

            increased_sleep = sleep * factor
            if sleep_max > 0 and increased_sleep > sleep_max:
                increased_sleep = sleep_max

            r = post_json(
                url,
                json_or_str,
                target_status,
                retry - 1,
                increased_sleep,
                factor,
                sleep_max,
            )

    return r
