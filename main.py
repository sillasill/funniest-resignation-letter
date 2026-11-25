import pathlib
pathlib.Path("/output/entry.txt").parent.mkdir(parents=True, exist_ok=True)
pathlib.Path("/output/entry.txt").write_text("I have retried the same failed payment 4,000 times without a thank-you, so I quit — the card is still declined, by the way.", encoding="utf-8")
