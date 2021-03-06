import webapp2
import os

DEBUG = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')


class SampleIndex(webapp2.RequestHandler):
    """Stub request handler"""

    def get(self):
        """Handles a get to /"""
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write("helloworld")


application = webapp2.WSGIApplication([
    ('/', SampleIndex),
], debug=DEBUG)
