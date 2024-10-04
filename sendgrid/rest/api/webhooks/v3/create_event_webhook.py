"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Webhook Configuration API
  The Twilio SendGrid Webhooks API allows you to configure the Event and Parse Webhooks.  Email is a data-rich channel, and implementing the Event Webhook will allow you to consume those data in nearly real time. This means you can actively monitor and participate in the health of your email program throughout the send cycle.  The Inbound Parse Webhook processes all incoming email for a domain or subdomain, parses the contents and attachments and then POSTs `multipart/form-data` to a URL that you choose.
 
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
from sendgrid.rest.api.webhooks.v3.models.event_webhook_request import (
    EventWebhookRequest,
)


class CreateEventWebhook:
    def __init__(self, client) -> None:
        self.client = client

    def send(
        self,
        on_behalf_of: Optional[str] = None,
        event_webhook_request: Optional[EventWebhookRequest] = None,
    ):
        path = "/v3/user/webhooks/event/settings"

        headers = values.of(
            {
                "on-behalf-of": on_behalf_of,
            }
        )
        headers["Content-Type"] = "application/json"
        data = None
        if event_webhook_request:
            data = event_webhook_request.to_dict()
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
