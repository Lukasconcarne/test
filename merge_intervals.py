"""Intervalle zusammenfassen. Fuelle merge so, dass test_merge_intervals.py besteht.
Aendere NUR diese Datei."""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """Fasst ueberlappende ODER sich beruehrende Intervalle [start, end] zusammen,
    Ergebnis nach start aufsteigend sortiert. Eingabe kann unsortiert sein.
    [1,3] und [3,5] beruehren sich -> [1,5]. Leere Eingabe -> [].
    Die Eingabeliste darf NICHT veraendert werden."""
    raise NotImplementedError
