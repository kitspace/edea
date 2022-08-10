"""
Test that parses as many .kicad_sch files as we could find.

SPDX-License-Identifier: EUPL-1.2
"""

import os
from time import time

from edea.edea import Project

test_folder = os.path.dirname(os.path.realpath(__file__))
kicad_folder = os.path.join(test_folder, "kicad_projects/kicad6-sch-files")
kicad_sch_files = []
for root, dirs, files in os.walk(kicad_folder):
    # don't go into any .git directories.
    if ".git" in dirs:
        dirs.remove(".git")

    for file in files:
        if file.endswith(".kicad_sch"):
            path = os.path.join(root, file)
            kicad_sch_files.append(path)

class TestParser:
    def test_parse_all_sch_files(self):
        assert len(kicad_sch_files) > 0
        for path in kicad_sch_files:
            pro = Project(path)
            pro.parse()

