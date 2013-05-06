from tw2.core.testbase import WidgetTest
from tw2.pygmentize import *


class TestPygmentize(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = Pygmentize
    # Initialization args. go here
    attrs = {}
    params = {'lexer_name': 'python', 'source': 'print "Hello World"'}
    expected = """<div class="highlight" style="background: #f8f8f8"><pre style="line-height: 125%"><span style="color: #008000; font-weight: bold">print</span> <span style="color: #BA2121">&quot;Hello World&quot;</span>\n</pre></div>"""
