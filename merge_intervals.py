"""Intervalle zusammenfassen. Fuelle merge so, dass test_merge_intervals.py besteht.
Aendere NUR diese Datei."""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """Fasst ueberlappende ODER sich beruehrende Intervalle [start, end] zusammen,
    Ergebnis nach start aufsteigend sortiert. Eingabe kann unsortiert sein.
    [1,3] und [3,5] beruehren sich -> [1,5]. Leere Eingabe -> [].
    Die Eingabeliste darf NICHT veraendert werden."""
    if not intervals:
        return []
    
    # Make a copy to avoid mutation
    intervals = [list(interval) for interval in intervals]
    
    # Sort by start
    intervals.sort(key=lambda x: x[0])
    
    result = []
    current = intervals[0]
    
    for interval in intervals[1:]:
        # Check if overlapping or touching (current[1] >= next[0])
        if current[1] >= interval[0]:
            # Merge: update end to max
            current[1] = max(current[1], interval[1])
        else:
            result.append(current)
            current = interval
    
    result.append(current)
    return result