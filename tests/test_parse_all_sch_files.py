"""
Test that parses as many .kicad_sch files as we could find.

SPDX-License-Identifier: EUPL-1.2
"""

import os

from edea.parser import from_str

test_folder = os.path.dirname(os.path.realpath(__file__))
kicad_folder = os.path.join(test_folder, "kicad_projects/kicad6-sch-files")

skip_files = (
    # these kicad_sch seem to be malformed/unterminated
    "github.com/KiCad/kicad-source-mirror/qa/resources/linux/mimeFiles/kicad/schematicFiles/kicadsch.kicad_sch",
    "gitlab.com/kicad/code/kicad/qa/resources/linux/mimeFiles/kicad/schematicFiles/kicadsch.kicad_sch",
)

kicad_sch_files = []
for root, dirs, files in os.walk(kicad_folder):
    # don't go into any .git directories.
    if ".git" in dirs:
        dirs.remove(".git")

    for file in files:
        if file.endswith(".kicad_sch"):
            path = os.path.join(root, file)

            skip = False
            for skip_file in skip_files:
                if path.endswith(skip_file):
                    skip = True
                    break

            if not skip:
                kicad_sch_files.append(path)


class TestParser:
    def test_parse_all_sch_files(self):
        assert len(kicad_sch_files) > 0
        for path in kicad_sch_files:
            print(f"Parsing {path}")
            with open(path, encoding="utf-8") as sch_file:
                sch = from_str(sch_file.read())
            assert sch is not None
