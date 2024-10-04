"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid IP Address Management API
  The Twilio SendGrid IP Address Management API combines functionality that was previously split between the Twilio SendGrid [IP Address API](https://docs.sendgrid.com/api-reference/ip-address) and [IP Pools API](https://docs.sendgrid.com/api-reference/ip-pools). This functionality includes adding IP addresses to your account, assigning IP addresses to IP Pools and Subusers, among other tasks.
 
  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""

import json
from typing import Optional
from sendgrid.exceptions import ApiException
from sendgrid.http.request import Request
from sendgrid.http.response import ApiResponse

from typing import Optional
from sendgrid.rest.api.ip_address_management.v3.models.add_ips_to_ip_pool_request import (
    AddIpsToIpPoolRequest,
)


class AddIpsToIpPool:
    def __init__(self, client) -> None:
        self.client = client

    def send(
        self,
        poolid: str,
        add_ips_to_ip_pool_request: Optional[AddIpsToIpPoolRequest] = None,
    ):
        path = "/v3/send_ips/pools/{poolid}/ips:batchAdd"
        path = path.format(
            poolid=poolid,
        )

        data = None
        if add_ips_to_ip_pool_request:
            data = add_ips_to_ip_pool_request.to_dict()
        request = Request(method="POST", url=path, data=data, headers=headers)
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
