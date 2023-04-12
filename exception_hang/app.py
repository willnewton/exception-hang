import falcon

class RuntimeErrorResource:
    def on_get(self, req, resp):
        raise RuntimeError

class BaseExceptionResource:
    def on_get(self, req, resp):
        raise BaseException

def create_app():
    app = falcon.App()
    app.add_route("/runtime_error", RuntimeErrorResource())
    app.add_route("/base_exception", BaseExceptionResource())
    return app
