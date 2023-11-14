__version__ = "1.0.8"

__all__ = ["StatbankClient", "apidata", "apidata_all", "apidata_rotate"]

from statbank.apidata import apidata, apidata_all, apidata_rotate
from statbank.client import StatbankClient
