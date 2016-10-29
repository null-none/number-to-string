#!/usr/bin/python
# -*- coding: utf-8 -*-

from money_decimal2text.script import decimal_to_text
import decimal

int_units = ((u'рубль', u'рубля', u'рублей'), 'm')
exp_units = ((u'копейка', u'копейки', u'копеек'), 'f')

print decimal_to_text(decimal.Decimal('302.19'), int_units=int_units, exp_units=exp_units)
# триста два рубля девятнадцать копеек
