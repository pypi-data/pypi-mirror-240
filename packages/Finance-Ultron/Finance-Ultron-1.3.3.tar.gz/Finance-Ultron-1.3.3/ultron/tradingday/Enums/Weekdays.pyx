# -*- coding: utf-8 -*-

from ultron.tradingday.Enums._Weekdays cimport Weekdays as ws

cpdef enum Weekdays:
    Sunday = ws.Sunday
    Monday = ws.Monday
    Tuesday = ws.Tuesday
    Wednesday = ws.Wednesday
    Thursday = ws.Thursday
    Friday = ws.Friday
    Saturday = ws.Saturday