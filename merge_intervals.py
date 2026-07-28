"""Intervalle zusammenfassen. Fuelle merge so, dass test_merge_intervals.py besteht.
Aendere NUR diese Datei."""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """Fasst ueberlappende ODER sich beruehrende Intervalle [start, end] zusammen,
    Ergebnis nach start aufsteigend sortiert. Eingabe kann unsortiert sein.
    [1,3] und [3,5] beruehren sich -> [1,5]. Leere Eingabe -> [].
    Die Eingabeliste darf NICHT veraendert werden."""
    if not intervals:
        return []

    # Sortiere eine Kopie, um die Eingabe nicht zu verändern
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    
    merged = []
    for interval in sorted_intervals:
        if not merged:
            merged.append(list(interval))
        else:
            last = merged[-1]
            # Wenn das aktuelle Intervall das letzte überlappt oder berührt
            if interval[0] <= last[1]:
                last[1] = max(last[1], interval[1])
            else:
                merged.append(list(interval))
    
    return merged
