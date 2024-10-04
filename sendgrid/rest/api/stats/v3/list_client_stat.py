"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Statistics API
  The Twilio SendGrid Statistics API allows you to retrieve the various statistics related to your email program.  Tracking your emails is an important part of being a good sender and learning about how your users interact with your email. This includes everything from clicks and opens to looking at which browsers and mailbox providers your customers use.  SendGrid has broken up statistics in specific ways so that you can get at-a-glance data, as well as the details of how your email is being used.  Category statistics are available for the previous thirteen months only.  See [**Statistics Overview**](https://docs.sendgrid.com/ui/analytics-and-reporting/stats-overview) for more information.
 
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
from sendgrid.rest.api.stats.v3.models.aggregated_by2 import AggregatedBy2


class ListClientStat:
    def __init__(self, client) -> None:
        self.client = client

    def send(
        self,
        on_behalf_of: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        aggregated_by: Optional[AggregatedBy2] = None,
    ):
        path = "/v3/clients/stats"

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
