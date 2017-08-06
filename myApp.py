# in c9.io:  sudo pip3 install flask
# in c9.io:  do: sudo pip3 install gevent.

# to commit:
# git add .
# git commit -m "glorious comment"
# git push -u origin master
# then in c9.io: clone the github in the workspace settings.
# in c9.io: git pull origin master

import os
from flask import Flask, send_from_directory, redirect
from gevent import monkey, pywsgi
from myAPI import x
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


    # the return can only be a string as far as I know.
    @app.route('/get_testing', methods=['GET'])
    def get_testing():
        return x

    return app

if __name__ == "__main__":
    app = create_app()
    server = pywsgi.WSGIServer(("0.0.0.0", 8080), app)  # 8080 req'd for c9.io
    server.serve_forever()
else:
    app = create_app()
