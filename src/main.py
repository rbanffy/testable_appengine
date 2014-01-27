import webapp2

DEBUG = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

class SampleIndex(webapp2.RequestHandler):
    "Stub request handler"

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write("helloworld")


application = webapp2.WSGIApplication([
    ('/', SampleIndex),
], debug=DEBUG)
