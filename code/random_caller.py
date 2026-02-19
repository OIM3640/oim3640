import csv
import random
from pathlib import Path

def load_names(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [row for row in reader if row.get("First") or row.get("Last")]

def format_name(row: dict[str, str]) -> str:
    parts = [row.get("First", "").strip(), row.get("Middle", "").strip(), row.get("Last", "").strip()]
    return " ".join(part for part in parts if part)

def main() -> None:
    csv_path = Path(__file__).resolve().parents[1] / "data" / "2026Spring-OIM3640-01.csv"
    rows = load_names(csv_path)
    if not rows:
        raise SystemExit("No names found in the CSV.")

    selected = random.choice(rows)
    # TODO: Persist the selected name for later review.
    print(format_name(selected))

if __name__ == "__main__":
    main()
