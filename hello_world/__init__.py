from flask import Flask
app = Flask(__name__)

import hello_world.views # noqa    -linter ignoruje sprawdzanie tej linii
