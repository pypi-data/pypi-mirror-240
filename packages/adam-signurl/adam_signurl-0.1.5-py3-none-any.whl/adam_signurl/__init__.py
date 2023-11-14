
__version__ = "0.0.1"
try:
    from adam_signurl import Adam_SignUrl
except ImportError:
    pass

try:
    from adam_signurl.adam_signurl import Adam_SignUrl  
except ImportError:
    pass    