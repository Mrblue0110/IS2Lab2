import sys
from pathlib import Path

# make "backend" importable when running from repo root
sys.path.append(str(Path(__file__).resolve().parents[1] / "backend"))

from app import create_app  # noqa: E402


def test_events_endpoint_returns_list():
    app = create_app()
    client = app.test_client()
    resp = client.get("/api/events")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert {"id", "title", "date"}.issubset(data[0].keys())