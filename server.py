#!/usr/bin/env python
# $Id$

"""pympd - PyMPlayer Server"""

__copyright__ = """
Copyright (C) 2007-2008  The MA3X Project (http://bbs.eee.upd.edu.ph)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import socket
from threading import Thread
try:
    import gobject
    from pymplayer import Server
except ImportError, msg:
    sys.exit(msg)


def main():
    gobject.threads_init()
    try:
        server = Server(port=1025, max_conns=2)
    except socket.error, msg:
        sys.exit(msg)
    server.mplayer.args = sys.argv[1:]
    t = Thread(target=server.start)
    t.setDaemon(True)
    t.start()
    try:
        gobject.MainLoop().run()
    except KeyboardInterrupt:
        pass
    server.stop()
    gobject.MainLoop().quit()


if __name__ == "__main__":
    main()
