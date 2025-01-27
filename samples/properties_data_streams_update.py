#!/usr/bin/env python

# Copyright 2021 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Analytics Admin API sample application which updates the data
stream.

See https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/properties.dataStreams/update
for more information.
"""
# [START analyticsadmin_properties_data_streams_update]
from google.analytics.admin import AnalyticsAdminServiceClient
from google.analytics.admin_v1alpha.types import DataStream
from google.protobuf.field_mask_pb2 import FieldMask


def run_sample():
    """Runs the sample."""

    # !!! ATTENTION !!!
    #  Running this sample may change/delete your Google Analytics account
    #  configuration. Make sure to not use the Google Analytics property ID from
    #  your production environment below.

    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID (e.g. "123456") before running the sample.
    property_id = "YOUR-GA4-PROPERTY-ID"

    # TODO(developer): Replace this variable with your data stream ID
    #  (e.g. "123456") before running the sample.
    stream_id = "YOUR-DATA-STREAM-ID"

    update_data_stream(property_id, stream_id)


def update_data_stream(property_id, stream_id):
    """Updates the data stream."""
    client = AnalyticsAdminServiceClient()
    # This call updates the display name of the data stream, as indicated by
    # the value of the `update_mask` field. The data stream to update is
    # specified in the `name` field of the `dataStream` instance.
    data_stream = client.update_data_stream(
        data_stream=DataStream(
            name=f"properties/{property_id}/dataStreams/{stream_id}",
            display_name="This is an updated test data stream",
        ),
        update_mask=FieldMask(paths=["display_name"]),
    )

    print("Result:")
    print(data_stream)


# [END analyticsadmin_properties_data_streams_update]


if __name__ == "__main__":
    run_sample()
