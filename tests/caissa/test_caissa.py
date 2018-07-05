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


class TestCaissa:
    """
    Test Caissa class
    """

    def test_main(self):
        """
        Test main application
        """

        import subprocess

        args = "--debug"

        proc = subprocess.Popen(
            "/usr/bin/env python3 -m caissa " + args,
            shell=True,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            universal_newlines=True)

        try:
            outs, errs = proc.communicate("quit", timeout=1)

            # check if all went well
            assert "Bringing Caissa to life" in errs

        except subprocess.TimeoutExpired:
            import pytest

            pytest.fail("Process did not exit cleanly (timeout reached)!")


if __name__ == "__main__":
    tester = TestCaissa()
    tester.test_main()
