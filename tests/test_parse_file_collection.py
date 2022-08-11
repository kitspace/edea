"""
Test that parses as many .kicad_sch files as we could find.

SPDX-License-Identifier: EUPL-1.2
"""

import os
import re

from edea.edea import Project

test_folder = os.path.dirname(os.path.realpath(__file__))
kicad_folder = os.path.join(test_folder, "kicad_projects/kicad6-file-collection")

kicad_pcb_files = []
for root, dirs, files in os.walk(kicad_folder):
    # don't go into any .git directories.
    if ".git" in dirs:
        dirs.remove(".git")

    for file in files:
        if file.endswith(".kicad_pcb"):
            path = os.path.join(root, file)
            kicad_pcb_files.append(path)


def test_parse_file_collection():
    assert len(kicad_pcb_files) > 0
    for pcb_path in kicad_pcb_files:
        sch_path = re.sub(r"\.kicad_pcb$", ".kicad_sch", pcb_path)
        pro = Project(sch_path, pcb_path)
        pro.parse()
