"""
Test that parses as many .kicad_sch files as we could find.

SPDX-License-Identifier: EUPL-1.2
"""

import os
from time import time

from edea.edea import Project

test_folder = os.path.dirname(os.path.realpath(__file__))
kicad_folder = os.path.join(test_folder, "kicad_projects/kicad6-sch-files")


class TestParser:
    def test_parse_all_sch_files(self):
        for root, dirs, files in os.walk(kicad_folder):

            # don't go into any .git directories.
            if ".git" in dirs:
                dirs.remove(".git")

            for file in files:
                if file.endswith(".kicad_sch"):
                    path = os.path.join(root, file)
                    pro = Project(path)
                    pro.parse()

