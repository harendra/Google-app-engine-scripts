# -*- coding: utf-8 -*-
"""URL definitions."""
import webapp2

routes = [
    (r'/upload','fileupload.FileuploadHandler.FileuploadHandler'),
    (r'/downloader','fileupload.FileuploadHandler.FileDownloadHandler'),

]

'''
    (r'/login','authentication.Authenticator.LoginRedirector'),
    (r'/loginerror','authentication.Authenticator.LoginIncorrectHandler')
'''