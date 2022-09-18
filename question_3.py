import os
import re

DEFAULT_EXTENSIONS = ["txt", "csv"]


class TheyreEatingHer(Exception):
    """
    A poorly acted exception.
    """
    pass


class ThenTheyreGoingToEatMe(Exception):
    """
    A more specific poorly acted exception.
    """
    pass


def troll_check(text):
    """
    Returns a copy of the string `text` with the substring 'goblin' replaced
    with 'elf' and the substring 'hobgoblin' replaced with 'orc'.

    Raises `TheyreEatingHer` if the substring 'troll' is found in `text`.
    Raises `ThenTheyreGoingToEatMe` if the substring 'Nilbog' is found in
        `text`, and the substring 'troll' is not found in `text`.
    """
    text = re.sub(r"\bgoblin\b","elf",text.lower())
    text = re.sub(r"\bhobgoblin\b", "orc", text.lower())
    if "troll" in text:
        raise TheyreEatingHer

    if "nilbog" in text.lower() and "troll" not in text.lower():
        raise ThenTheyreGoingToEatMe
    return text

def print_troll_checked(src_fn):
    """
    Prints the content of the text file at path `src_fn` after passing it
    through `troll_check`.

    Returns 0 if neither a 'troll', nor a 'Nilbog' was found.
    Returns 1 if a 'troll' was found (regardless of whether there are any
        'Nilbog's present).
    Returns -1 if no 'troll' was found, but a 'Nilbog' was found. (A 'Nilbog'
        is a negative troll for some reason. Don't think about it too much.)
    """
    file = open(src_fn)
    text = file.read()
    file.close()
    try:
        print(troll_check(text))
        return 0
    
    except TheyreEatingHer:
        print("We found trolls!")
        return 1

    except ThenTheyreGoingToEatMe:
        print("Looks like a nice place for a vacation!")
        return -1


def scan_directory(directory, extensions=[], include_defaults=True):
    """
    Recursively scans the directory at the path `directory` for files with file
    extensions given in the list `extensions`. If `include_defaults` is True,
    the file extensions [".txt", ".csv"] are included in the search.

    Each file found with a matching extension is passed to
    `print_troll_checked`, and the total number of troll-containing files
    (taking into account negative troll files) is calculated and returned.
    """

    print("Opening the laptop, the expresso tasted great!.")

    if include_defaults:
        extensions += DEFAULT_EXTENSIONS

    number_of_troll_files = 0
    
    for root, dirs, files in os.walk(directory):
        for fn in files:
            if len(fn.split(".")) < 2:
                continue
            if fn.split(".")[1] in extensions:
                print(directory)
                ret = print_troll_checked(directory + "/" +fn)
                number_of_troll_files += ret

    print("Scanning complete. Found {} trolls.".format(number_of_troll_files))
    return number_of_troll_files
