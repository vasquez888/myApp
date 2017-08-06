import os
from flask import Flask, send_from_directory, redirect
from gevent import monkey, pywsgi
monkey.patch_all()


def create_app():
    app = Flask("press_controller")

    # map the root folder to index.html
    @app.route("/")
    def home():
        return redirect("/index.html")

    @app.route("/<path:path>")
    def root(path):
        """
        This is the cheesy way I figured out to serve the Angular2 app created
        by the angular-cli system. It essentially serves everything from
        static/dist (the distribution directory created by angular-cli)
        """
        return send_from_directory(os.path.join(os.getcwd(), "static/dist"),
                                   path)

    return app


if __name__ == "__main__":
    app = create_app()
    server = pywsgi.WSGIServer(("0.0.0.0", 8080), app)
    server.serve_forever()
else:
    app = create_app()
