"""Intervalle zusammenfassen. Fuelle merge so, dass test_merge_intervals.py besteht.
Aendere NUR diese Datei."""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """Fasst ueberlappende ODER sich beruehrende Intervalle [start, end] zusammen,
    Ergebnis nach start aufsteigend sortiert. Eingabe kann unsortiert sein.
    [1,3] und [3,5] beruehren sich -> [1,5]. Leere Eingabe -> [].
    Die Eingabeliste darf NICHT veraendert werden."""
    if not intervals:
        return []
    # Sortiere Kopie nach Start, um Original nicht zu veraendern
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    result = [sorted_intervals[0]]
    for start, end in sorted_intervals[1:]:
        last_start, last_end = result[-1]
        if start <= last_end:  # ueberlappend ODER beruehrend
            result[-1][1] = max(last_end, end)
        else:
            result.append([start, end])
    return result