###############################################################################
#
# This MobilityDB code is provided under The PostgreSQL License.
#
# Copyright (c) 2019-2022, Université libre de Bruxelles and MobilityDB
# contributors
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose, without fee, and without a written 
# agreement is hereby granted, provided that the above copyright notice and
# this paragraph and the following two paragraphs appear in all copies.
#
# IN NO EVENT SHALL UNIVERSITE LIBRE DE BRUXELLES BE LIABLE TO ANY PARTY FOR
# DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING
# LOST PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION,
# EVEN IF UNIVERSITE LIBRE DE BRUXELLES HAS BEEN ADVISED OF THE POSSIBILITY 
# OF SUCH DAMAGE.
#
# UNIVERSITE LIBRE DE BRUXELLES SPECIFICALLY DISCLAIMS ANY WARRANTIES, 
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS FOR A PARTICULAR PURPOSE. THE SOFTWARE PROVIDED HEREUNDER IS ON
# AN "AS IS" BASIS, AND UNIVERSITE LIBRE DE BRUXELLES HAS NO OBLIGATIONS TO 
# PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS. 
#
###############################################################################
from abc import ABC

from pymeos_cffi.functions import temporal_start_instant, temporal_end_instant, temporal_instant_n, temporal_instants
from .temporal import Temporal


class TemporalInstants(Temporal, ABC):
    """
    Abstract class for representing temporal values of instant set or
    sequence subtype.
    """

    @property
    def start_instant(self):
        """
        Start instant.
        """
        return self.ComponentClass(_inner=temporal_start_instant(self._inner))

    @property
    def end_instant(self):
        """
        End instant.
        """
        return self.ComponentClass(_inner=temporal_end_instant(self._inner))

    def instant_n(self, n: int):
        """
        N-th instant.
        """
        # 1-based
        return self.ComponentClass(_inner=temporal_instant_n(self._inner, n))

    @property
    def instants(self):
        """
        List of instants.
        """
        ts, count = temporal_instants(self._inner)
        return [self.ComponentClass(_inner=ts[i]) for i in range(count)]

