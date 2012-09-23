#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoconf()
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install('SUBDIRS="brctl doc"')

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "README", "doc/FAQ", "doc/HOWTO")
