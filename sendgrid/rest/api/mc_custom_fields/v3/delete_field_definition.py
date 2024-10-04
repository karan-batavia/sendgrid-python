"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Marketing Campaigns Custom Fields API
  The Twilio SendGrid Marketing Campaigns Custom Fields API allows you to add extra information about your marketing contacts that is relevant to your needs. For example, a fashion retailer might create a custom field for customers' shoe sizes, an ice cream shop might store customers' favorite flavors in a custom field, and you can create custom fields that make sense for your business.  With custom fields, you can also create [segments](https://docs.sendgrid.com/api-reference/segmenting-contacts-v2/) based on custom fields values. Your custom fields are completely customizable to the use-cases and user information that you need.  You can also manage your Custom Fields using the SendGrid application user interface. See [**Using Custom Fields**](https://docs.sendgrid.com/ui/managing-contacts/custom-fields) for more information, including a list of Reserved Fields. You can also manage your custom fields in the [Marketing Campaigns application user interface](https://mc.sendgrid.com/custom-fields).
 
  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""

import json
from sendgrid.exceptions import ApiException
from sendgrid.http.request import Request
from sendgrid.http.response import ApiResponse


class DeleteFieldDefinition:
    def __init__(self, client) -> None:
        self.client = client

    def send(
        self,
        custom_field_id: str,
    ):
        path = "/v3/marketing/field_definitions/{custom_field_id}"
        path = path.format(
            custom_field_id=custom_field_id,
        )

        data = None
        request = Request(method="DELETE", url=path, data=data, headers=headers)
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
