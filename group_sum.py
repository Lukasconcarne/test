"""Gruppieren und summieren. Fuelle group_sum so, dass test_group_sum.py besteht.
Aendere NUR diese Datei."""


def group_sum(rows: list[dict], key: str, value: str) -> list[tuple]:
    """Gruppiert rows nach rows[i][key], summiert rows[i][value] je Gruppe und
    gibt eine nach key aufsteigend sortierte Liste von (key, summe)-Tupeln zurueck.
    Leere Eingabe -> []. Fehlt in einer Zeile key oder value, wirf KeyError."""
    if not rows:
        return []
    
    result = {}
    for row in rows:
        # Prüfe ob key und value im Dictionary vorhanden sind
        if key not in row or value not in row:
            raise KeyError(f"Missing key '{key}' or value '{value}' in row")
        
        group_key = row[key]
        group_value = row[value]
        
        if group_key not in result:
            result[group_key] = group_value
        else:
            result[group_key] += group_value
    
    # Sortiere nach key und gebe als Liste von Tupeln zurück
    return sorted(result.items())