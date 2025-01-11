import pdfminer

from . import utils
from ._version import __version__
from .pdf import PDF

open = PDF.open