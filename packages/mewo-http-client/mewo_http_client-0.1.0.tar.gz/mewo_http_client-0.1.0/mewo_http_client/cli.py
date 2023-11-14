import argparse
import sys

from . import lib


def validate_arg_given_once(flag_name, value):
    if len(value) > 1:
        sys.stderr.write(f"Error: '--{flag_name}' was given more than once.\n")
        sys.exit(1)


def get_args():
    parser = argparse.ArgumentParser(
        prog="mewo-http-client-post",
        description="Send a mewo service to service POST request.",
        epilog="",
    )

    parser.add_argument("-u", "--url", required=True, action="append")
    parser.add_argument("-j", "--json", required=True, action="append")
    parser.add_argument("-r", "--retry", required=False, type=int)
    parser.add_argument("-p", "--sleep", required=False, type=float)
    parser.add_argument("-c", "--factor", required=False, type=float)
    parser.add_argument("-m", "--sleep_max", required=False, type=float)

    args = {}

    for flag_name, value in vars(parser.parse_args()).items():
        if isinstance(value, list):
            validate_arg_given_once(flag_name, value)
            args[flag_name] = value[0]
        else:
            args[flag_name] = value

    positional_args = [args["url"], args["json"]]

    del args["url"]
    del args["json"]

    kwargs = {k: v for k, v in args.items() if v}

    return positional_args, kwargs


def post_json():
    positional_args, kwargs = get_args()

    r = lib.post_json(*positional_args, **kwargs)

    print(r.status_code, r.reason)
