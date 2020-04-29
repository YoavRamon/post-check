from tabulate import tabulate
import requests
import argparse
import pprint
import json
import os

class EnvDefault(argparse.Action):
    def __init__(self, envvar, required=True, default=None, **kwargs):
        if not default and envvar:
            if envvar in os.environ:
                default = os.environ[envvar]
        if required and default:
            required = False
        super(EnvDefault, self).__init__(default=default, required=required, 
                                         **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-pn', '--package-number', type=str, required=True, help='Package number, you may use the PKG environment variable as well', 
                        action=EnvDefault, envvar="PKG")
    parser.add_argument('-ih', '--is-heb', action='store_true', required=False, help='Print in hebrew')
    parser.add_argument('-pj', '--print-json', action='store_true', required=False, help='Print json instead of table')
    parser.add_argument('-cf', '--cookie-file', type=str, required=False, default='cookie.json', help='Cookie file')

    return parser.parse_args()


def _get_state_list(item_code, request_key, verification_key, is_heb):
    url = "https://mypost.israelpost.co.il/umbraco/Surface/ItemTrace/GetItemTrace"
    payload = f"itemCode={item_code}{'&lcid=1037' if is_heb else ''}&__RequestVerificationToken={request_key}"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': f'__RequestVerificationToken={verification_key};',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)


def _check_response(response):
    if response['ReturnCode'] != 0:
        print(f"Got the following error: {response['ErrorDescription']}")
        return False
    else:
        return True


def _print_response(response, print_json):
    if print_json:
        pprint.pprint(response)
    else:
        print(tabulate(tabular_data=response['Result']['itemcodeinfo']['InfoLines'],
                       headers=response['Result']['itemcodeinfo']['ColumnHeaders'],
                       tablefmt="plain",
                       stralign='right'))


if __name__ == "__main__":
    args = _parse_args()

    cookie = json.load(open(args.cookie_file))
    post_response = _get_state_list(args.package_number, cookie['request_key'], cookie['verification_key'], args.is_heb)
    if _check_response(post_response):
        _print_response(post_response, args.print_json)
    else:
        print('Failed to get package information')
