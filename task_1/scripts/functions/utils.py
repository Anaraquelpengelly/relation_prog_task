# define a function to find the pattern
import re


def find_pattern(text: str, pattern=str) -> bool:
    """finds a regex pattern a text in a dataset column.

     Args:
         text (str): the text to be searched
         pattern (str): the regex pattern to search

     Returns:
         bool: if the text contains the pattern.

     """
    if re.search(pattern, text):
        return True
    else:
        return False
