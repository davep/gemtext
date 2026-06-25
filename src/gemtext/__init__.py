"""Provides tools for working with Gemtext."""

##############################################################################
# Python imports.
from importlib.metadata import version

######################################################################
# Main library information.
__author__ = "Dave Pearson"
__copyright__ = "Copyright 2026, Dave Pearson"
__credits__ = ["Dave Pearson"]
__maintainer__ = "Dave Pearson"
__email__ = "davep@davep.org"
__version__: str = version("gemtext")
__licence__ = "MIT"

##############################################################################
# Local imports.
from .parser import (
    Gemtext,
    Heading,
    Line,
    Link,
    ListItem,
    Paragraph,
    PreFormatted,
    Quote,
)

##############################################################################
# Exports.
__all__ = [
    "Gemtext",
    "Heading",
    "Line",
    "Link",
    "ListItem",
    "Paragraph",
    "PreFormatted",
    "Quote",
]

### __init__.py ends here
