"""Intervalle zusammenfassen. Fuelle merge so, dass test_merge_intervals.py besteht.
Aendere NUR diese Datei."""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """Fasst ueberlappende ODER sich beruehrende Intervalle [start, end] zusammen,
    Ergebnis nach start aufsteigend sortiert. Eingabe kann unsortiert sein.
    [1,3] und [3,5] beruehren sich -> [1,5]. Leere Eingabe -> [].
    Die Eingabeliste darf NICHT veraendert werden."""
    if not intervals:
        return []
    
    # Kopie der Intervalle erstellen und nach Start sortieren
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    
    result = []
    current_start, current_end = sorted_intervals[0]
    
    for start, end in sorted_intervals[1:]:
        if start <= current_end:  # Überlappung oder Berührung
            current_end = max(current_end, end)
        else:
            result.append([current_start, current_end])
            current_start, current_end = start, end
    
    result.append([current_start, current_end])
    return result