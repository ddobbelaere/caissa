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

import logging
import queue
import time

from .events import *


class Brain:
    """
    The brain of Caissa
    
        - interacts with senses
        - holds skills
        - controls the interactions between skills and senses
    """
    
    def __init__(self, hearing, sense, speech):
        """
        Constructor
        """
        
        # store references to senses
        self.hearing = hearing
        self.sense = sense
        self.speech = speech
        
        # initialize event queue
        self._event_queue = queue.Queue()
        
        # initialize logger
        self.logger = logging.getLogger(__name__)
        
        # initialize all skills
        self._init_skills()
        
        # start senses
        self.sense.start(self.event_queue)
    
    @property
    def event_queue(self):
        """
        Return reference to event queue
        """
        
        return self._event_queue
    
    def _init_skills(self):
        """
        Initialize all skills
        """
        
        pass
    
    def think_forever(self):
        """
        Think forever
        """
        
        while True:
            # process the next event
            e = self.event_queue.get()
            
            if type(e) is TextInputEvent:
                self.logger.debug("Processing text input event \"{}\"".format(e.text))
                
                if e.text == "exit":
                    import sys
                    sys.exit(0)
