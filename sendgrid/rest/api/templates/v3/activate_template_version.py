"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Templates API
  The Twilio SendGrid Templates API allows you to create and manage email templates to be delivered with SendGrid's sending APIs. The templates you create will be available using a template ID that is passed to our sending APIs as part of the request. Each template may then have multiple versions associated with it. Whichever version is set as \"active\" at the time of the request will be sent to your recipients. This system allows you to update a single template's look and feel entirely without modifying your requests to our Mail Send API. For example, you could have a single template for welcome emails. That welcome template could then have a version for each season of the year that's themed appropriately and marked as active during the appropriate season. The template ID passed to our sending APIs never needs to change; you can just modify which version is active.  This API provides operations to create and manage your templates as well as their versions.  Each user can create up to 300 different templates. Templates are specific to accounts and Subusers. Templates created on a parent account will not be accessible from the Subusers' accounts.
 
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


class ActivateTemplateVersion:
    def __init__(self, client) -> None:
        self.client = client

    def send(
        self,
        template_id: str,
        version_id: str,
        on_behalf_of: Optional[str] = None,
    ):
        path = "/v3/templates/{template_id}/versions/{version_id}/activate"
        path = path.format(
            template_id=template_id,
            version_id=version_id,
        )

        headers = values.of(
            {
                "on-behalf-of": on_behalf_of,
            }
        )
        data = None
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
