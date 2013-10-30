from klein import Klein

from twisted.application import strports
from twisted.python import usage
from twisted.web import server


class KleinExample:

    app = Klein()

    @app.route("/")
    def app_root(self, request):

        return "Hello! Please go to /muffins/<muffin> with your favourite type of muffin!"

    @app.route("/muffins/<muffin>")
    def app_muffins(self, request, muffin):

        my_muffins = [
            "chocolate",
            "blueberry",
            "vanilla",
            "LSD-infused"
        ]

        if muffin in my_muffins:
            return "You like %s muffins too? Here, have one!" % (muffin, )
        else:
            return "Sorry, I only have these muffins: " % (",".join(my_muffins), )


class Options(usage.Options):
    optParameters = [
        ["port", "p", "8085"]
    ]

def makeService(options):
    viewer = KleinExample()
    site = server.Site(viewer.app.resource())
    return strports.service(options['port'], site)
