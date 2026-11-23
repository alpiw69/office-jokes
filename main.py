"""make.fun bounty: Make the AI Judge Laugh: Office Jokes.

Deterministic, no-network program. Writes one one-line joke
(under 200 characters) to /output/entry.txt.
Running twice writes identical bytes.
"""
from pathlib import Path

JOKE = "My calendar invited me to a meeting about meetings, so I declined - and got invited to discuss my decline."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(JOKE, encoding="utf-8")
    print(f"Wrote {OUT} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
