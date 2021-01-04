# Copyright 2021 QuantRocket LLC - All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import time
from pytz import timezone
from trading_calendars.exchange_calendar_xnys import XNYSExchangeCalendar

class USExtendedHoursExchangeCalendar(XNYSExchangeCalendar):
    """
    A calendar for extended hours which runs from 4 AM to 8 PM.
    """

    name = "us_extended_hours"
    country_code = "US"
    tz = timezone('America/New_York')


    open_times = ((None, time(4, 1)),)
    close_times = ((None, time(20)),)
