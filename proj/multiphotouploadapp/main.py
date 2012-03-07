import webapp2
from urls import routes
from config import config

app = webapp2.WSGIApplication(routes=routes, debug=True, config=config)
        