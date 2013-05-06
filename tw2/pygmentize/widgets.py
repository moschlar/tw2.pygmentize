import tw2.core as twc


class Pygmentize(twc.Widget):
    template = "genshi:tw2.pygmentize.templates.pygmentize"

    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        twc.JSLink(modname=__name__, filename='static/pygmentize.js'),
        twc.CSSLink(modname=__name__, filename='static/pygmentize.css'),
    ]

    @classmethod
    def post_define(cls):
        pass
        # put custom initialisation code here

    def prepare(self):
        super(Pygmentize, self).prepare()
        # put code here to run just before the widget is displayed
