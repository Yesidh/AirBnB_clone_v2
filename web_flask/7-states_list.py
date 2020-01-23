#!/usr/bin/python3
"""
   Your web application must be listening on 0.0.0.0, port 5000
   You must use storage for fetching data from the storage engine (FileStorage
       or D   BStorage) => from models import storage and storage.all(...)
   After each request you must remove the current SQLAlchemy Session:
   Declare a method to handle @app.teardown_appcontext
   Call in this method storage.close()
   Routes:
    /states_list: display a HTML page: (inside the tag BODY)
     H1 tag: “States”
     UL tag: with the list of all State objects present in DBStorage sorted by
          name (A->Z) tip
     LI tag: description of one State: <state.id>: <B><state.name></B>
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(self):
    """Method tho handle teardown"""

    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    """method"""

    my_list = storage.all('State').values()
    return render_template('7-states_list.html', _list=my_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
