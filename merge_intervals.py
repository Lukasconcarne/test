"""Intervalle zusammenfassen. Fuelle merge so, dass test_merge_intervals.py besteht.
Aendere NUR diese Datei."""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """Fasst ueberlappende ODER sich beruehrende Intervalle [start, end] zusammen,
    Ergebnis nach start aufsteigend sortiert. Eingabe kann unsortiert sein.
    [1,3] und [3,5] beruehren sich -> [1,5]. Leere Eingabe -> [].
    Die Eingabeliste darf NICHT veraendert werden."""
    if not intervals:
        return []
    
    # Sort intervals by start value (creates a copy, no mutation of original)
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    
    # Initialize result with first interval
    result = [sorted_intervals[0][:]]  # Copy to avoid mutation
    
    for current in sorted_intervals[1:]:
        last = result[-1]
        # Check if current overlaps or touches the last interval
        if current[0] <= last[1]:  # Overlap or touching
            # Merge: update end to max of both ends
            last[1] = max(last[1], current[1])
        else:
            # No overlap, add as new interval (copy to be safe)
            result.append(current[:])
    
    return result
