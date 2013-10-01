#!/usr/bin/python
# -*- coding: utf-8 -*-
##
# axis_collection.py: Represents a collection of axis-devices.
##
# © 2013 Steven Casagrande (scasagrande@galvant.ca).
#
# This file is a part of the InstrumentKit project.
# Licensed under the AGPL version 3.
##
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
##
##

## FEATURES ####################################################################

from __future__ import division

## IMPORTS #####################################################################

import abc

from instruments.abstract_instruments import Instrument
from instruments.util_fns import ProxyList
from axis_controller import Axis

## CLASSES #####################################################################

class AxisList(ProxyList, AxisCollection):
    
    def __init__(self, parent, proxy_cls, valid_set):
        super(AxisList, self).__init__(parent, proxy_cls, valid_set)

class AxisCollection(object):
    
    def __init__(self, axis_list):
        if isinstance(axis_list, AxisList):
            self._is_root = True
        elif isinstance(axis_list, AxisCollection):
            self._is_root = False
        else:
            raise TypeError('AxisCollection init parameter must be of type '
                            'AxisList or AxisCollection, instead received '
                            '{}.'.format(type(axis_list)))
        self._axis_list = axis_list
        
    ## PROPERTIES ##
    
    @property
    def axis(self):
        return self._axis_list
        