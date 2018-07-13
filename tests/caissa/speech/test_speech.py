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


class TestSpeech:
    """
    Tests for speech module
    """

    def test_speech(self):
        """
        Test the speech class
        """

        from caissa.speech import Speech

        # test the Speech class
        speech = Speech("en")
        speech.say("Hello, my name is Caiissa.")
        speech.say("How are you doing?")

        speech = Speech("nl")
        speech.say("Hallo, ik heet Caïissa.")
        speech.say("Hoe gaat het met U?")
