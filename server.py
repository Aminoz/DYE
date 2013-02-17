'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Project : AskDYE.com - Does it Exist?
Name    : Donald Hui
Date    : 12:58 AM Feb 17 2013

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./static/html/main.html")

class CreateDye(tornado.web.RequestHandler):
    def post(self):
        question = self.get_argument('question', default=None) 
        print "yay"  

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/ask", CreateDye),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "/static/"}),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
