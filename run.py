from backend_flask import create_app
from backend_flask.configapp import Config

if __name__ == "__main__":
  app = create_app(Config)
  app.run(debug=True,port=8000)