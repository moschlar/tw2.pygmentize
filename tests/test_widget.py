from tw2.core.testbase import WidgetTest
from tw2.pygmentize import *


class TestPygmentizeName(WidgetTest):
    widget = Pygmentize
    attrs = {}
    params = {'lexer_name': 'Python', 'source': 'print "Hello World"'}
    expected = """<div class="highlight" style="background: #f8f8f8"><pre style="line-height: 125%"><span style="color: #008000; font-weight: bold">print</span> <span style="color: #BA2121">&quot;Hello World&quot;</span>\n</pre></div>"""


class TestPygmentizeAlias(WidgetTest):
    widget = Pygmentize
    attrs = {}
    params = {'lexer_name': 'py', 'source': 'print "Hello World"'}
    expected = """<div class="highlight" style="background: #f8f8f8"><pre style="line-height: 125%"><span style="color: #008000; font-weight: bold">print</span> <span style="color: #BA2121">&quot;Hello World&quot;</span>\n</pre></div>"""


class TestPygmentizeMIME(WidgetTest):
    widget = Pygmentize
    attrs = {}
    params = {'lexer_name': 'text/x-python', 'source': 'print "Hello World"'}
    expected = """<div class="highlight" style="background: #f8f8f8"><pre style="line-height: 125%"><span style="color: #008000; font-weight: bold">print</span> <span style="color: #BA2121">&quot;Hello World&quot;</span>\n</pre></div>"""


class TestPygmentizeFilename(WidgetTest):
    widget = Pygmentize
    attrs = {}
    params = {'filename': 'hello.py', 'source': 'print "Hello World"'}
    expected = """<div class="highlight" style="background: #f8f8f8"><pre style="line-height: 125%"><span style="color: #008000; font-weight: bold">print</span> <span style="color: #BA2121">&quot;Hello World&quot;</span>\n</pre></div>"""


class TestPygmentizeBoth(WidgetTest):
    widget = Pygmentize
    attrs = {}
    params = {'lexer_name': 'python', 'filename': 'hello.py', 'source': 'print "Hello World"'}
    expected = """<div class="highlight" style="background: #f8f8f8"><pre style="line-height: 125%"><span style="color: #008000; font-weight: bold">print</span> <span style="color: #BA2121">&quot;Hello World&quot;</span>\n</pre></div>"""
