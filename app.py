'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Project : AskDYE.com - Does it Exist?
Name    : Donald Hui
Date    : 12:58 AM Feb 17 2013

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''

import tornado.ioloop
import tornado.web
from mongoengine import *
from pyes import *

class DYEFactory(object):
    def __init__(self):
        print "eh"

    def MakeDye(self, question, askee, references):
        print "eh"

class DYE(Document):
   question = StringField(max_length=200, required=True) 
   exists   = BooleanField(required=True)
   answered = BooleanField(required=True)
   up_votes = IntField(required=False, default=0)
   down_votes = IntField(required=False, default=0)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./static/html/main.html")
        conn = ES('localhost:9200')
        #conn.create_index("test-index")
        mapping = { 'blah:': {'boost' : 1.0, 'index': 'analyzed',
        'store': 'yes',
        'type': 'string',
        'term_vector' : 'with_positions_offsets'
        }}
        conn.put_mapping('test-type', {'properties':mapping}, ['test-index'])
        conn.refresh()

        print "eh"

class VoteDye(tornado.web.RequestHandler):
    def post(self):
        dye_id = self.get_argument("id", default=None)
        vote = self.get_argument("vote", default=None)

        dye = DYE.find({'id':dye_id})
        if dye:
            if vote:
                dye.update_one(inc_up_votes)
            else:
                dye.update_one(inc_down_votes)
        print "yay"

def find_dye(question):
    print "yay"
    return True

class CreateDye(tornado.web.RequestHandler):
    def post(self):
        question = self.get_argument('question', default=None)
        #we'll need to check if a similar / same question already exists
        print "yay"  

class AnswerDye(tornado.web.RequestHandler):
    def get(self):
        s = solr.SolrConnection('http://example.org:8083/solr')

    def post(self):
        s = solr.SolrConnection('http://example.org:8083/solr')
        print "yay"

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/ask", CreateDye),
    (r"/vote", VoteDye),
    (r"/answer", AnswerDye),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "/static/"}),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
