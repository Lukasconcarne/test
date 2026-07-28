"""Gruppieren und summieren. Fuelle group_sum so, dass test_group_sum.py besteht.
Aendere NUR diese Datei."""


def group_sum(rows: list[dict], key: str, value: str) -> list[tuple]:
    """Gruppiert rows nach rows[i][key], summiert rows[i][value] je Gruppe und
    gibt eine nach key aufsteigend sortierte Liste von (key, summe)-Tupeln zurueck.
    Leere Eingabe -> []. Fehlt in einer Zeile key oder value, wirf KeyError."""
    totals: dict = {}
    for row in rows:
        if key not in row or value not in row:
            raise KeyError
        group_key = row[key]
        totals[group_key] = totals.get(group_key, 0) + row[value]
    return sorted(totals.items())
