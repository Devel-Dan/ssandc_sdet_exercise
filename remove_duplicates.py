"""
remove_duplicates.py

provides a function to remove duplicate values while maintaining order
"""


def remove_duplicates(input_arr):
    # seen is our cache
    seen = set()
    result = []

    # loop through each value
    for val in input_arr:
        # check if we have already seen this value
        if val in seen:
            continue
        else:
            # we did not see it, add to our result and cache it
            result.append(val)
            seen.add(val)

    return result
