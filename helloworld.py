import os
from flask import Flask
app = Flask(__name__)

import lupa
import requests

@app.route("/<path:path>")
def hello(path):
    lua = lupa.LuaRuntime()
    src = requests.get("https://gist.github.com/raw/{0}".format(path))
    app = lua.eval("""
function()
    {0}
end
""".format(src.text))
    return app()

if __name__ == "__main__":
    app.run('0.0.0.0', int(os.environ.get("PORT", 5000)), debug=True)