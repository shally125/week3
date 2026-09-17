# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///

"""Fetch Hong Kong's annual GHG data once and cache the raw JSON in data/.

    uv run fetch.py

The cached file makes the project reproducible and lets plot.py run offline.
Delete the file only when you intentionally want to fetch a newer edition.
"""

from pathlib import Path

import requests

URL = (""https://cnsd.gov.hk/wp-content/uploads/pdf/"
       "greenhouse_gas_emissions_and_carbon_intensity.json")      # CHANGE ME
FILE = "greenhouse-gas-emissions-and-carbon-intensity.json"                          # CHANGE ME: say what it is,
                                                                      # keep the publisher's extension
HERE = Path(__file__).parent
DATA = HERE / "data"


def fetch(url: str, path: Path) -> Path:
    """Fetch *url* once and save the publisher's reply byte-for-byte at *path*."""
      if path.exists():
        print(
            f"data/{path.name} is already here ({path.stat().st_size} bytes). "
            "Delete it to fetch a newer edition."
        )
        return path

    DATA.mkdir(exist_ok=True)
    print(f"asking {url}")
    reply = requests.get(
        url,
        timeout=60,
        headers={"User-Agent": "SD5913 PolyU student carbon visualisation"},
    )
    reply.raise_for_status()
    path.write_bytes(reply.content)
    print(f"saved data/{path.name} ({path.stat().st_size} bytes). Now: git add data")
    return path


if __name__ == "__main__":
    fetch(URL, DATA / FILE)
