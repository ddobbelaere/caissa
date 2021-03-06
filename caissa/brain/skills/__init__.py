# -*- coding: utf-8 -*-
"""
Caissa voice-controlled personal assistant
Copyright © 2018  Dieter Dobbelaere

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


class Skill:
    """
    Skill base class

    Every voice-controlled skill must subclass this class.
    A skill is contained in Caissa's brain and is connected
    to the senses via the brain.
    """

    def __init__(self, brain, args=None):
        """
        Constructor
        """

        # store reference to brain
        self.brain = brain

        # initialize skill
        self.init(args)

    def init(self, args=None):
        """
        Initialize skill
        """

        # override this method in the subclass skill
        pass

    def handle_event(self, e):
        """
        Handle the given event
        """

        # override this method in the subclass skill
        pass

    def say(self, *args, **kwargs):
        """
        Say the given message
        """

        self.brain.say(*args, **kwargs)
