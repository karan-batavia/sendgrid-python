"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Reverse DNS API
  The Twilio SendGrid Reverse DNS API (formerly IP Whitelabel) allows you to configure reverse DNS settings for your account. Mailbox providers verify the sender of your emails by performing a reverse DNS lookup.  When setting up Reverse DNS, Twilio SendGrid will provide an A Record (address record) for you to add to the DNS records of your sending domain. The A record maps your sending domain to a dedicated Twilio SendGrid IP address. Once Twilio SendGrid has verified that the appropriate A record for the IP address has been created, the appropriate reverse DNS record for the IP address is generated.  Reverse DNS is available for [dedicated IP addresses](https://sendgrid.com/docs/ui/account-and-settings/dedicated-ip-addresses/) only.  You can also manage your reverse DNS settings in the Sender Authentication setion of the [Twilio SendGrid application user interface](https://app.sendgrid.com/settings/sender_auth).  See [**How to Set Up Reverse DNS**](https://sendgrid.com/docs/ui/account-and-settings/how-to-set-up-reverse-dns/) for more information.
 
  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""

import json
from typing import Optional
from sendgrid.base import values
from sendgrid.exceptions import ApiException
from sendgrid.http.request import Request
from sendgrid.http.response import ApiResponse

from typing import Optional


class ListReverseDns:
    def __init__(self, client) -> None:
        self.client = client

    def send(
        self,
        on_behalf_of: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ip: Optional[str] = None,
    ):
        path = "/v3/whitelabel/ips"

        headers = values.of(
            {
                "on-behalf-of": on_behalf_of,
            }
        )
        data = None
        request = Request(method="GET", url=path, data=data, headers=headers)
        response = self.client.send(request)
        if response is None:
            raise ApiException(
                error="CreateAlert creation failed: Unable to connect to server"
            )

        if response.text:
            text = json.loads(response.text)
        else:
            text = ""
        if response.is_success():
            return ApiResponse(
                status_code=response.status_code, model=text, headers=response.headers
            )
        else:
            raise ApiException(
                status_code=response.status_code, error=text, headers=response.headers
            )
