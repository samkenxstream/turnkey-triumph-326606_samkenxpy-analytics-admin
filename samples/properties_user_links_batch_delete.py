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

"""Google Analytics Admin API sample application which delete the user link for
the Google Analytics 4 property using a batch call.

See https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/properties.userLinks/batchDelete
for more information.
"""
# [START analyticsadmin_properties_user_links_batch_delete]
from google.analytics.admin import AnalyticsAdminServiceClient
from google.analytics.admin_v1alpha.types import (
    BatchDeleteUserLinksRequest,
    DeleteUserLinkRequest,
)


def run_sample():
    """Runs the sample."""

    # !!! ATTENTION !!!
    #  Running this sample may change/delete your Google Analytics account
    #  configuration. Make sure to not use the Google Analytics property ID from
    #  your production environment below.

    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID (e.g. "123456") before running the sample.
    property_id = "YOUR-GA4-PROPERTY-ID"

    # TODO(developer): Replace this variable with your Google Analytics
    #  account user link ID (e.g. "123456") before running the sample.
    property_user_link_id = "YOUR-ACCOUNT-USER-LINK-ID"

    batch_delete_property_user_link(property_id, property_user_link_id)


def batch_delete_property_user_link(property_id, property_user_link_id):
    """Deletes the GA4 property user link using a batch call."""
    client = AnalyticsAdminServiceClient()
    client.batch_delete_user_links(
        BatchDeleteUserLinksRequest(
            parent=f"properties/{property_id}",
            requests=[
                DeleteUserLinkRequest(
                    name=f"properties/{property_id}/userLinks/{property_user_link_id}"
                )
            ],
        )
    )
    print("User link deleted")


# [END analyticsadmin_properties_user_links_batch_delete]


if __name__ == "__main__":
    run_sample()
