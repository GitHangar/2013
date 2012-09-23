#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

def build():
    autotools.make("RCFLAGS=\"%s %s -DINET6\"" % (get.CFLAGS(),get.LDFLAGS()))

def install():
    autotools.rawInstall("prefix=%s/usr" % get.installDIR())
