"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Marketing Campaigns Segments 2.0 API
  The Twilio SendGrid Marketing Campaigns Segments V2 API allows you to create, edit, and delete segments as well as retrieve a list of segments or an individual segment by ID.  Segments are similar to contact lists, except they update dynamically over time as information stored about your contacts or the criteria used to define your segments changes. When you segment your audience, you are able to create personalized Automation emails and Single Sends that directly address the wants and needs of your particular audience.  Note that Twilio SendGrid checks for newly added or modified contacts who meet a segment's criteria on an hourly schedule. Only existing contacts who meet a segment's criteria will be included in the segment searches within 15 minutes.  Segments built using engagement data such as \"was sent\" or \"clicked\" will take approximately 30 minutes to begin populating.  Segment samples and counts are refreshed approximately once per hour; they do not update immediately. If no contacts are added to or removed from a segment since the last refresh, the sample and UI count displayed will be refreshed at increasing time intervals with a maximum sample and count refresh delay of 24 hours.  You can also manage your Segments with the [Marketing Campaigns application user interface](https://mc.sendgrid.com/contacts). See [**Segmenting Your Contacts**](https://docs.sendgrid.com/ui/managing-contacts/segmenting-your-contacts) for more information.
 
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
from sendgrid.rest.api.mc_segments_2.v3.models.segment_write_v2 import SegmentWriteV2


class CreateSegment:
    def __init__(self, client) -> None:
        self.client = client

    def send(
        self,
        segment_write_v2: Optional[SegmentWriteV2] = None,
    ):
        path = "/v3/marketing/segments/2.0"

        data = None
        if segment_write_v2:
            data = segment_write_v2.to_dict()
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
