#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    kde4.configure("-DImageMagick_Magick++_LIBRARY=/usr/lib/libMagick++-Q16HDRI.so \
                    -DImageMagick_MagickCore_LIBRARY=/usr/lib/libMagickCore-Q16HDRI.so")

def build():
    kde4.make()

def install():
    kde4.install()
