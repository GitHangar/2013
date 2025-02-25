#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/cute-giraffe", "*")
    pisitools.dosym("/usr/share/cute-giraffe/PyQt-giraff.pyw", "/usr/bin/cute-giraffe")

    pisitools.dodoc("COPYING","README")
