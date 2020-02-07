#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import versioneer

setup(
    name='quantrocket-trading-calendars',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Trading calendars for QuantRocket-supported exchanges',
    maintainer='QuantRocket LLC',
    maintainer_email='support@quantrocket.com',
    url='https://github.com/quantrocket-llc/ib-trading-calendars',
    license='Apache 2.0',
    packages=['quantrocket_trading_calendars'],
    entry_points = {
        'console_scripts': ['exchange-status=quantrocket_trading_calendars.status:main'],
    },
    install_requires=[
        'trading_calendars>=1.11.0'
    ]
)
