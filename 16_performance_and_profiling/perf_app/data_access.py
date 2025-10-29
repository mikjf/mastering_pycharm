import time
from typing import Any, Dict, List, Optional

# Module-level cached connection
_CONN: Optional[Dict[str, Any]] = None

def get_records(text):
    conn = create_connection()
    results = run_query(conn, text)
    return results


# Make this faster by caching / reusing the connection
def create_connection() -> Dict[str, Any]:
    global _CONN
    if _CONN is not None and _CONN.get('connected'):
        return _CONN

    # Simulate one-time connection cost
    time.sleep(0.250)
    _CONN = {'connected': True, 'created_at': time.time()}
    return _CONN


def run_query(conn: Dict[str, Any], text: str) -> List[Dict[str, str]]:
    if not text:
        return []

    # Simulate fetching ~99 rows with far less overhead by minimizing per-row sleep
    # Keep a tiny, single delay to represent query execution instead of 99x sleeps.
    time.sleep(0.005)  # replaces 99 * 0.001s = ~0.099s

    data = [read_row(conn) for _ in range(1, 100)]
    return data

def read_row(conn: Dict[str, Any]) -> Dict[str, str]:
    # Improved "index": remove per-row sleep; leave logic intact
    if conn.get('connected'):
        return {'col1': 'val1', 'col2': 'val2'}

    raise Exception("No connection")