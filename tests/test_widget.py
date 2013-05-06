from tw2.core.testbase import WidgetTest
from tw2.pygmentize import *

class TestPygmentize(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = Pygmentize
    # Initilization args. go here 
    attrs = {'id':'pygmentize-test'}
    params = {}
    expected = """<div id="pygmentize-test"></div>"""
