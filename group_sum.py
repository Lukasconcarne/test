"""Gruppieren und summieren. Fuelle group_sum so, dass test_group_sum.py besteht.
Aendere NUR diese Datei."""


def group_sum(rows: list[dict], key: str, value: str) -> list[tuple]:
    """Gruppiert rows nach rows[i][key], summiert rows[i][value] je Gruppe und
    gibt eine nach key aufsteigend sortierte Liste von (key, summe)-Tupeln zurueck.
    Leere Eingabe -> []. Fehlt in einer Zeile key oder value, wirf KeyError."""
    result: dict = {}
    for row in rows:
        k = row[key]        # KeyError bei fehlendem key
        v = row[value]      # KeyError bei fehlendem value
        if k in result:
            result[k] += v
        else:
            result[k] = v
    return sorted(result.items())
