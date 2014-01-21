import webapp2
import settings


class SampleIndex(webapp2.RequestHandler):
    """Stub request handler"""

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write("helloworld")


application = webapp2.WSGIApplication([
    ('/', SampleIndex),
], debug=settings.DEBUG)
