"""Gruppieren und summieren. Fuelle group_sum so, dass test_group_sum.py besteht.
Aendere NUR diese Datei."""


def group_sum(rows: list[dict], key: str, value: str) -> list[tuple]:
    """Gruppiert rows nach rows[i][key], summiert rows[i][value] je Gruppe und
    gibt eine nach key aufsteigend sortierte Liste von (key, summe)-Tupeln zurueck.
    Leere Eingabe -> []. Fehlt in einer Zeile key oder value, wirf KeyError."""
    result = {}
    for row in rows:
        k = row[key]
        v = row[value]
        result[k] = result.get(k, 0) + v
    return sorted(result.items())
