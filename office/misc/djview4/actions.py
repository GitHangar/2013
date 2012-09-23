#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

browserPath = "/usr/lib/browser-plugins"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.make("DESTDIR=%s install-djview" % get.installDIR())
    autotools.make("DESTDIR=%s install-nsdejavu" % get.installDIR())

    #Make symbolic link in /opt like all other browser plugins
    pisitools.dosym("%s/nsdejavu.so" % browserPath, "/opt/netscape/plugins/nsdejavu.so")

    #Fix permission
    shelltools.chmod("%s/%s/nsdejavu.so" % (get.installDIR(), browserPath))

    #Install icon
    pisitools.insinto("/usr/share/pixmaps", "desktopfiles/hi32-djview4.png", "djvulibre-djview4.png")

    #Install desktop file
    pisitools.insinto("/usr/share/applications", "desktopfiles/djvulibre-djview4.desktop")

    pisitools.dodoc("COPYING", "COPYRIGHT", "README*")
