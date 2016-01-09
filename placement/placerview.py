# -*- mode: python; -*-
#
# Copyright 2015 Canonical, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging

from placement.ui import PlacementView
from ubuntui.ev import EventLoop
from ubuntui.frame import Frame

log = logging.getLogger('placement')


class PlacerView(Frame):

    def __init__(self, placement_controller, config):
        self.pv = None
        self.placement_controller = placement_controller
        self.config = config
        super().__init__()

    def update(self, *args, **kwargs):
        if self.pv is None:
            self.pv = PlacementView(
                display_controller=self,
                placement_controller=self.placement_controller,
                config=self.config,
                do_deploy_cb=self.done_cb)
            self.set_header(
                title="Bundle Editor"
            )
            self.set_body(self.pv)
        self.pv.update()
        EventLoop.set_alarm_in(1, self.update)

    def status_error_message(self, message):
        pass

    def status_info_message(self, message):
        pass

    def done_cb(self):
        log.debug("done_cb called")
        EventLoop.exit(0)
