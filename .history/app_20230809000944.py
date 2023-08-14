from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo()

@app.route("/")
def index():
  return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True)