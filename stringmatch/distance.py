from typing import Optional

import Levenshtein


class Distance:
    """Contains functions for calculating the levenshtein distance between strings."""

    def distance(self, string1: str, string2: str) -> Optional[int]:
        """Returns the levenshtein distance between two strings.

        Parameters
        ----------
        string1 : str
            The first string to compare.
        string2 : str
            The second string to compare.

        Returns
        -------
        Optional[int]
            The levenshtein distance between the two strings.

        Examples
        --------
        >>> distance("stringmatch", "strmatch")
        3
        >>> distance("stringmatch", "something different")
        14
        """
        return Levenshtein.distance(string1, string2) if string1 and string2 else None

    def distance_list(self, string: str, string_list: list[str]) -> list[Optional[int]]:
        """Returns the levenshtein distance for a string and a list of strings.

        Parameters
        ----------
        string : str
            The string to compare.
        string_list : list[str]
            The list of strings to compare to.

        Returns
        -------
        list[Optional[int]]
            The levenshtein distances between the two strings.

        Examples
        --------
        >>> distance_list("stringmatch", ["strmatch", "something different"])
        [3, 14]
        """
        return [self.distance(string, s) for s in string_list]
