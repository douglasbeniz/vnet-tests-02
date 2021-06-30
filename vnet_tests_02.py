"""An example Python module."""

from typing import List

def join(values: List[int], delimiter: str) -> str:
    """Produce a string where subsequent items are separated by delimiter."""
    generatedString: str = ""
    # For each x integer in values check if should be added to resulted string with delimiter or not
    for item in values:
    	if generatedString == "":	# do not put delimiter before first item
    		generatedString = str(item)
    	else:
    		generatedString += delimiter + str(item)
    return generatedString
