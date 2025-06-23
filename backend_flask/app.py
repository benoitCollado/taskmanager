#from flask import Flask
#from .routes.task import task_bp
#from .routes.tasklist import tasklist_bp
#from .database import Base, engine
#from flask_cors import CORS
#import sys
#sys.path.append(".")

#app = Flask(__name__)
#CORS(app)

#Base.metadata.create_all(bind=engine)
#app.register_blueprint(task_bp, url_prefix="/api/")
#app.register_blueprint(tasklist_bp, url_prefix="/api/")

#if __name__ == '__main__':
#  app.run(debug=True, port=8000)

    