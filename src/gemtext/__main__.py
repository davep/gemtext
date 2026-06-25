"""A simple parser to show how the library works."""

##############################################################################
# Python imports.
import fileinput

##############################################################################
# Local imports.
from gemtext import Gemtext


##############################################################################
def parse_input() -> None:
    """Parse the input from stdin or files and print the parsed Gemtext."""
    with fileinput.input() as gemtext:
        for gem_line in Gemtext("".join(gemtext)).content:
            print(f"{gem_line!r}")


##############################################################################
if __name__ == "__main__":
    parse_input()


### __main__.py ends here
