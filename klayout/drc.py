"""GF180MCU DRC with the open PDK's KLayout deck (gf180mcuD, no density): the violated rules and counts.

    uv run python pdk/gf180/klayout/drc.py GDS TOP RUN_DIR

The deck: ``$GF180_OPEN_PDK`` (default ~/Documents/libs/gf180mcu-open-pdk)/gf180mcuD/libs.tech/klayout/tech/drc
(``gf180mcu.drc``: variant gf180mcuD, five metals, 11 kA top metal, MIM option B; every deck but
density, which a block alone fails).
"""

from __future__ import annotations

import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

from klayout import rdb

DECK = (
    Path(os.environ.get("GF180_OPEN_PDK", "~/Documents/libs/gf180mcu-open-pdk")).expanduser()
    / "gf180mcuD/libs.tech/klayout/tech/drc"
)
DECKS = "all,-density"  # the deck's tags: every rule deck but the coverage checks
THREADS = 8


def drc(gds: Path, top: str, run_dir: Path) -> dict[str, int]:
    """The violated rules and their counts; raises when the deck is missing or writes no report."""

    if not (DECK / "gf180mcu.drc").is_file():
        raise FileNotFoundError(f"no GF180MCU DRC deck at {DECK}: set GF180_OPEN_PDK to the open PDK's install")
    run_dir = Path(run_dir).resolve()
    run_dir.mkdir(parents=True, exist_ok=True)
    report = run_dir / "gf180mcu.lyrdb"
    report.unlink(missing_ok=True)
    command = [
        "klayout",
        "-b",
        "-zz",
        "-r",
        str(DECK / "gf180mcu.drc"),
        "-rd",
        f"input={Path(gds).resolve()}",
        "-rd",
        f"report={report}",
        "-rd",
        f"topcell={top}",
        "-rd",
        "variant=gf180mcuD",
        "-rd",
        "run_mode=deep",
        "-rd",
        f"threads={THREADS}",
        "-rd",
        f"decks={DECKS}",
    ]
    done = subprocess.run(command, check=False, capture_output=True, text=True, cwd=run_dir)
    (run_dir / "run_drc.log").write_text(done.stdout + done.stderr)
    if done.returncode != 0 or not report.exists():
        raise RuntimeError(f"KLayout DRC failed or wrote no report; see {run_dir / 'run_drc.log'}")
    db = rdb.ReportDatabase("")
    db.load(str(report))
    counts: Counter[str] = Counter()
    for item in db.each_item():
        counts[db.category_by_id(item.category_id()).name()] += 1
    return dict(counts)


if __name__ == "__main__":
    violations = drc(Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3]))
    for rule, n in sorted(violations.items()):
        print(f"{rule:24s} {n}")
    print("DRC clean" if not violations else f"DRC: {len(violations)} rules violated")
