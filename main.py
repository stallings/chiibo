
#
# configuration for the application and all the request mapping.
#


# import statements
import webapp2
import homehandler


# the app for the chiibo website
app = webapp2.WSGIApplication([('/', homehandler.HomeHandler)], debug=True)


