import sys
import argparse
import subprocess as sp
import json
import time
import requests
from typing import List, Dict, Any, Optional

RETRY_HANDLER_ARG_NAMES = [
    "target_status",
    "retry",
    "sleep",
    "factor",
    "sleep_max",
    "stdout",
    "stderr",
]


def get_requests_args(local_values, args_to_get):
    return [local_values[a] for a in args_to_get]


def get_requests_kwargs(local_values, args_to_get):
    d = {k: v for k, v in local_values.items() if k in args_to_get}
    return {**d, **local_values["kwargs"]}


def get_retry_handler_kwargs(local_values):
    return {k: v for k, v in local_values.items() if k in RETRY_HANDLER_ARG_NAMES}


def retry_handler(
    requests_call_func,
    requests_call_args,
    request_call_kwargs,
    target_status: List[int] = list(range(200, 300)),
    retry: int = 0,
    sleep: float = 1,
    factor: float = 2.0,
    sleep_max: float = 0.0,
    stdout=None,
    stderr=None,
) -> requests.Response:
    try:
        # This is the requests function (requests.get, requests.post, ...)
        r = requests_call_func(*requests_call_args, **request_call_kwargs)

    except requests.exceptions.RequestException as e:
        if e.response:
            r = e.response
        else:
            r = requests.Response()
            r.reason = f"{e}"
        r.status_code = 1

    if retry != 0 and r.status_code not in target_status:
        stdout = stdout or sys.stdout
        stderr = stderr or sys.stderr

        if retry > 0:
            sleep_duration = round(sleep, 2)

            stderr.write(f"HTTP request failed. Retry in {sleep_duration} seconds\n")

            time.sleep(sleep_duration)

            increased_sleep = sleep * factor
            if sleep_max > 0 and increased_sleep > sleep_max:
                increased_sleep = sleep_max

            r = retry_handler(
                requests_call_func,
                requests_call_args,
                request_call_kwargs,
                target_status=target_status,
                retry=retry - 1,
                sleep=increased_sleep,
                factor=factor,
                sleep_max=sleep_max,
            )
    return r


def get(
    url: str,
    params: Optional[Any] = None,
    # mewo args
    target_status: List[int] = list(range(200, 300)),
    retry: int = 0,
    sleep: float = 1,
    factor: float = 2.0,
    sleep_max: float = 0.0,
    stdout=None,
    stderr=None,
    # kwargs for requests package args.
    **kwargs,
) -> requests.Response:
    """
    This call always returns a `requests.Response`, even if an exception is raised.
    Thses two fields are always set:
    - response.status_code (Contains the HTTP status code or `1` if an exception was raised.)
    - response.reason (Contains the HTTP message or the raised exception message.)
    """
    local_values = locals()
    requests_args = get_requests_args(local_values, ["url"])
    requests_kwargs = get_requests_kwargs(local_values, ["params"])
    retry_handler_kwargs = get_retry_handler_kwargs(local_values)

    return retry_handler(
        requests.get, requests_args, requests_kwargs, **retry_handler_kwargs
    )


# NOTE: put and post are identical here.


def post(
    url: str,
    json: Optional[Dict[str, Any]] = None,
    data: Optional[str] = None,
    # mewo args
    target_status: List[int] = list(range(200, 300)),
    retry: int = 0,
    sleep: float = 1,
    factor: float = 2.0,
    sleep_max: float = 0.0,
    stdout=None,
    stderr=None,
    # kwargs for requests package args.
    **kwargs,
) -> requests.Response:
    """
    This call always returns a `requests.Response`, even if an exception is raised.
    Thses two fields are always set:
    - response.status_code (Contains the HTTP status code or `1` if an exception was raised.)
    - response.reason (Contains the HTTP message or the raised exception message.)
    """
    local_values = locals()
    requests_args = get_requests_args(local_values, ["url"])
    requests_kwargs = get_requests_kwargs(local_values, ["json", "data"])
    retry_handler_kwargs = get_retry_handler_kwargs(local_values)

    return retry_handler(
        requests.post, requests_args, requests_kwargs, **retry_handler_kwargs
    )


# NOTE: put and post are identical here.


def put(
    url: str,
    json: Optional[Dict[str, Any]] = None,
    data: Optional[str] = None,
    # mewo args
    target_status: List[int] = list(range(200, 300)),
    retry: int = 0,
    sleep: float = 1,
    factor: float = 2.0,
    sleep_max: float = 0.0,
    stdout=None,
    stderr=None,
    # kwargs for requests package args.
    **kwargs,
) -> requests.Response:
    """
    This call always returns a `requests.Response`, even if an exception is raised.
    Thses two fields are always set:
    - response.status_code (Contains the HTTP status code or `1` if an exception was raised.)
    - response.reason (Contains the HTTP message or the raised exception message.)
    """
    local_values = locals()
    requests_args = get_requests_args(local_values, ["url"])
    requests_kwargs = get_requests_kwargs(local_values, ["json", "data"])
    retry_handler_kwargs = get_retry_handler_kwargs(local_values)

    return retry_handler(
        requests.put, requests_args, requests_kwargs, **retry_handler_kwargs
    )
