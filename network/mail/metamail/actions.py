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

WorkDir = "metamail-2.7"

def setup():
    autotools.autoreconf ("-fi")
    shelltools.chmod("configure")

    autotools.configure()

def build():

    autotools.make()

def install():

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "CREDITS", "README")

    shelltools.unlink("man/mmencode.1")
    pisitools.doman("man/*", "debian/mimencode.1", "debian/mimeit.1")

