import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class LocaleHandler(tornado.web.RequestHandler):
    def get(self, locale):
        self.locale = tornado.locale.get(locale)
        self.render("index.html", product=1, author='Wai Foong', view=1234)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/([^/]+)/about-us", LocaleHandler),
    ], template_path='templates/')


if __name__ == "__main__":
    tornado.locale.load_translations('locale/')

    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
