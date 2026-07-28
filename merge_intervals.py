"""Intervalle zusammenfassen. Fuelle merge so, dass test_merge_intervals.py besteht.
Aendere NUR diese Datei."""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """Fasst ueberlappende ODER sich beruehrende Intervalle [start, end] zusammen,
    Ergebnis nach start aufsteigend sortiert. Eingabe kann unsortiert sein.
    [1,3] und [3,5] beruehren sich -> [1,5]. Leere Eingabe -> [].
    Die Eingabeliste darf NICHT veraendert werden."""
    if not intervals:
        return []
    # sorted() erstellt eine Kopie -> Eingabe bleibt unveraendert
    ordered = sorted(intervals, key=lambda iv: iv[0])
    merged = [[ordered[0][0], ordered[0][1]]]
    for start, end in ordered[1:]:
        if start <= merged[-1][1]:  # Ueberlappung oder Beruehrung
            if end > merged[-1][1]:
                merged[-1][1] = end
        else:
            merged.append([start, end])
    return merged
