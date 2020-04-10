# Copyright 2019 QuantRocket LLC - All Rights Reserved
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

from trading_calendars import register_calendar_type, register_calendar_alias
from trading_calendars.calendar_utils import (
    default_calendar_names,
    _default_calendar_aliases,
    _default_calendar_factories
)
from .exchange_calendar_aeb import AEBExchangeCalendar
from .exchange_calendar_asx import ASXExchangeCalendar
from .exchange_calendar_bm import BMExchangeCalendar
from .exchange_calendar_bux import BUXExchangeCalendar
from .exchange_calendar_bvl import BVLExchangeCalendar
from .exchange_calendar_bvme import BVMEExchangeCalendar
from .exchange_calendar_cboe import CBOEExchangeCalendar
from .exchange_calendar_ebs import EBSExchangeCalendar
from .exchange_calendar_enextbe import ENEXTBEExchangeCalendar
from .exchange_calendar_fwb import FWBExchangeCalendar
from .exchange_calendar_globex import GlobexExchangeCalendar
from .exchange_calendar_iceus import ICEUSExchangeCalendar
from .exchange_calendar_kse import KSEExchangeCalendar
from .exchange_calendar_lse import LSEExchangeCalendar
from .exchange_calendar_mexi import MEXIExchangeCalendar
from .exchange_calendar_moex import MOEXExchangeCalendar
from .exchange_calendar_nyse import NYSEExchangeCalendar
from .exchange_calendar_ose import OSEExchangeCalendar
from .exchange_calendar_sbf import SBFExchangeCalendar
from .exchange_calendar_sehk import SEHKExchangeCalendar
from .exchange_calendar_sehkntl import SEHKNTLExchangeCalendar
from .exchange_calendar_sfb import SFBExchangeCalendar
from .exchange_calendar_sgx import SGXExchangeCalendar
from .exchange_calendar_tse import TSEExchangeCalendar
from .exchange_calendar_tsej import TSEJExchangeCalendar
from .exchange_calendar_vse import VSEExchangeCalendar
from .exchange_calendar_wse import WSEExchangeCalendar

_quantrocket_ibkr_calendar_factories = {
    "AEB": AEBExchangeCalendar,
    "ASX": ASXExchangeCalendar,
    "BM": BMExchangeCalendar,
    "BUX": BUXExchangeCalendar,
    "BVL": BVLExchangeCalendar,
    "BVME": BVMEExchangeCalendar,
    "CBOE": CBOEExchangeCalendar,
    "EBS": EBSExchangeCalendar,
    "ENEXT.BE": ENEXTBEExchangeCalendar,
    "FWB": FWBExchangeCalendar,
    "GLOBEX": GlobexExchangeCalendar,
    "ICEUS": ICEUSExchangeCalendar,
    "KSE": KSEExchangeCalendar,
    "LSE": LSEExchangeCalendar,
    "MEXI": MEXIExchangeCalendar,
    "MOEX": MOEXExchangeCalendar,
    "NYSE": NYSEExchangeCalendar,
    "OSE": OSEExchangeCalendar,
    "SEHK": SEHKExchangeCalendar,
    "SEHKNTL": SEHKNTLExchangeCalendar,
    "SBF": SBFExchangeCalendar,
    "SFB": SFBExchangeCalendar,
    "SGX": SGXExchangeCalendar,
    "TSE": TSEExchangeCalendar,
    "TSEJ": TSEJExchangeCalendar,
    "VSE": VSEExchangeCalendar,
    "WSE": WSEExchangeCalendar,
}

_quantrocket_ibkr_calendar_aliases = {
    "NASDAQ": "NYSE",
    "ARCA": "NYSE",
    "AMEX": "NYSE",
    "BATS": "NYSE",
    "IEX": "NYSE",
    "PINK": "NYSE",
    "ENEXT": "ENEXT.BE",
    "SEHKSZSE": "SEHKNTL",
}

_quantrocket_mic_aliases = {

    # Other US Mics
    "XNAS": "XNYS",
    "ARCX": "XNYS",
    "XASE": "XNYS",
    "BATS": "XNYS",
    "PINX": "XNYS",
    "PSGM": "XNYS",
    "OTCB": "XNYS",
    "OTCQ": "XNYS",
    "OTCM": "XNYS",
}

quantrocket_calendar_factories = {}

for name, calendar in _quantrocket_ibkr_calendar_factories.items():
    register_calendar_type(name, calendar, force=True)
    quantrocket_calendar_factories[name] = calendar


for alias, real_name in _quantrocket_ibkr_calendar_aliases.items():
    register_calendar_alias(alias, real_name, force=True)
    quantrocket_calendar_factories[alias] = quantrocket_calendar_factories[real_name]

for alias, real_name in _quantrocket_mic_aliases.items():
    register_calendar_alias(alias, real_name, force=True)
    quantrocket_calendar_factories[alias] = _default_calendar_factories[real_name]

all_calendar_names = list(quantrocket_calendar_factories.keys()) + \
    default_calendar_names + list(_default_calendar_aliases.keys())

all_calendar_names = list(set(all_calendar_names))
all_calendar_names.sort()
