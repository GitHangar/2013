#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "libXaw3d-%s" % get.srcVERSION()

def setup():
    autotools.configure("--disable-static \
                         --enable-arrow-scrollbars \
                         --enable-gray-stipples \
                         --enable-multiplane-bitmaps")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())

    pisitools.dodoc("ChangeLog","COPYING","README","src/README.XAW3D")
