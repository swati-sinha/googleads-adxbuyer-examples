#!/usr/bin/python
#
# Copyright 2014 Google Inc. All Rights Reserved.
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

"""This example demonstrates how to retrieve a Creative.

Tags: Creatives.get
"""

__author__ = 'api.msaniscalchi@gmail.com (Mark Saniscalchi)'

import pprint
import sys

from oauth2client.client import AccessTokenRefreshError
import util


def main(ad_exchange_buyer, account_id, buyer_creative_id):
  # Construct the request.
  request = ad_exchange_buyer.creatives().get(
      accountId=account_id,
      buyerCreativeId=buyer_creative_id)

  # Execute request and print response.
  pprint.pprint(request.execute())

if __name__ == '__main__':
  try:
    service = util.GetService()

    ACCOUNT_ID = int('INSERT_ACCOUNT_ID')
    BUYER_CREATIVE_ID = 'INSERT_BUYER_CREATIVE_ID'

    if BUYER_CREATIVE_ID == 'INSERT_BUYER_CREATIVE_ID':
      raise Exception('buyer_creative_id not set.')
  except IOError, ex:
    print 'Unable to create adexchangebuyer service - %s' % ex
    print 'Did you specify the key file in util.py?'
    sys.exit()
  except AccessTokenRefreshError, ex:
    print 'Unable to create adexchangebuyer service - %s' % ex
    print 'Did you set the correct Service Account Email in util.py?'
    sys.exit()
  except ValueError, ex:
    print 'Unable to create adexchangebuyer service - %s' % ex
    print 'Did you set account_id to an integer?'
    sys.exit()

  main(service, ACCOUNT_ID, BUYER_CREATIVE_ID)
