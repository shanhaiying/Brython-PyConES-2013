from browser import html, doc as document
from Dialog import *
from ProgressBar import *
from Slider import *

def add_stylesheet():
    _link=html.LINK(Href='/src/Lib/ui/css/smoothness/jquery-ui-1.10.3.custom.min.css')
    _link.rel='stylesheet'

    doc <= _link     # document doesn't work here.. :( must use doc 
