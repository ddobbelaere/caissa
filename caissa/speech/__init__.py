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

import espeakng
import logging

# TODO: take care of alterations in separate class


class Speech:
    """
    Caissa's speech
    """

    def __init__(self, args):
        """
        Constructor
        """

         # initialize logger
        self.logger = logging.getLogger(__name__)

        # Define preferred voices.
        self.preferred_voices = {
            "en": "english-mb-en1+f4",
            "nl": "dutch-mbrola-2+f4"
        }

        # Instantiate text to speech engines for each language
        self.engines = {lang: espeakng.ESpeakNG() for lang in self.preferred_voices}

        # Set engine settings.
        for lang in self.preferred_voices:
            self.engines[lang].voice = self.preferred_voices[lang]
            self.engines[lang].speed = 100
            self.engines[lang].volume = 200

        # store default language
        self.default_lang = args.language

        assert self.default_lang in self.engines

    def say(self, message, lang=None, sync=False):
        """
        Say the given message
        """

        if lang is None:
            lang = self.default_lang

        text = ""
        if isinstance(message, dict):
            if lang in message:
                text = message[lang]
            else:
                self.logger.warning("Message has no translation for requested language '{}'.".format(lang))
        else: 
            text = message

        self.engines[lang].say(text, sync=sync)
