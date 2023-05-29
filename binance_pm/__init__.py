import hashlib
import hmac
import json
import logging
import time
from base64 import b64encode
from json import JSONDecodeError
from urllib.parse import urlencode

import requests
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15


def get_timestamp():
    return int(time.time() * 1000)


def clean_none_value(d) -> dict:
    out = {}
    for k in d.keys():
        if d[k] is not None:
            out[k] = d[k]
    return out


def encoded_string(query, special=False):
    if special:
        return urlencode(query).replace("%40", "@").replace("%27", "%22")
    else:
        return urlencode(query, True).replace("%40", "@")


def hmac_hashing(secret, payload):
    m = hmac.new(secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256)
    return m.hexdigest()


def rsa_signature(private_key, payload, private_key_pass=None):
    private_key = RSA.import_key(private_key, passphrase=private_key_pass)
    h = SHA256.new(payload.encode("utf-8"))
    signature = pkcs1_15.new(private_key).sign(h)
    return b64encode(signature)


class Error(Exception):
    pass


class ClientError(Error):
    def __init__(self, status_code, error_code, error_message, header):
        # https status code
        self.status_code = status_code
        # error code returned from server
        self.error_code = error_code
        # error message returned from server
        self.error_message = error_message
        # the whole response header returned from server
        self.header = header


class ServerError(Error):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message


class BinanceAPI:

    def __init__(self, api_key, api_secret, base_url):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url

        self.timeout = None
        self.proxies = None
        self.show_header = False
        self.show_limit_usage = False

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json;charset=utf-8",
                "User-Agent": "binance_pm/",
                "X-MBX-APIKEY": api_key,
            }
        )

    def sign_request(self, http_method, url_path, payload=None, special=False):
        if payload is None:
            payload = {}
        payload["timestamp"] = get_timestamp()
        query_string = self._prepare_params(payload, special)
        payload["signature"] = self._get_sign(query_string)
        return self.send_request(http_method, url_path, payload, special)

    def _prepare_params(self, params, special=False):
        return encoded_string(clean_none_value(params), special)

    def _get_sign(self, payload):
        # if self.private_key:
        #     return rsa_signature(self.private_key, payload, self.private_key_pass)
        return hmac_hashing(self.api_secret, payload)

    def send_request(self, http_method, url_path, payload=None, special=False):
        if payload is None:
            payload = {}
        url = self.base_url + url_path
        logging.debug("url: " + url)
        params = clean_none_value(
            {
                "url": url,
                "params": self._prepare_params(payload, special),
                "timeout": self.timeout,
                "proxies": self.proxies,
            }
        )
        response = self._dispatch_request(http_method)(**params)
        logging.debug("raw response from server:" + response.text)
        self._handle_exception(response)

        try:
            data = response.json()
        except ValueError:
            data = response.text
        result = {}

        if self.show_limit_usage:
            limit_usage = {}
            for key in response.headers.keys():
                key = key.lower()
                if (
                        key.startswith("x-mbx-used-weight")
                        or key.startswith("x-mbx-order-count")
                        or key.startswith("x-sapi-used")
                ):
                    limit_usage[key] = response.headers[key]
            result["limit_usage"] = limit_usage

        if self.show_header:
            result["header"] = response.headers

        if len(result) != 0:
            result["data"] = data
            return result

        return data

    def _dispatch_request(self, http_method):
        return {
            "GET": self.session.get,
            "DELETE": self.session.delete,
            "PUT": self.session.put,
            "POST": self.session.post,
        }.get(http_method, self.session.get)

    def _handle_exception(self, response):
        status_code = response.status_code
        if status_code < 400:
            return
        if 400 <= status_code < 500:
            try:
                err = json.loads(response.text)
            except JSONDecodeError:
                raise ClientError(status_code, None, response.text, response.headers)
            raise ClientError(status_code, err["code"], err["msg"], response.headers)
        raise ServerError(status_code, response.text)
