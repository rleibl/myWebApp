# myWebApp
Boilerplate web framework for educational purposes.

* PyCharm (Community Edition)
* Python flask
* javascript

## PyCharm

### Python venv
* Click "Python Interpreter selector" (bottom right)
* new virtual environment

### Flask Setup
* Install Flask at "Python Packages" (bottom leftish)


* Edit/Add Configuration...
* Script Path
  * Select 'flask' from the venv/bin/ directory
* Parameters
  * run
* Environment Variables
  * FLASK_APP=app.py
  * FLASK_ENV=development
  * FLASK_DEBUG=1

### Running
The flask server can now be started using either the run button
or < ctrl >-R

With FLASK_DEBUG enabled, the server will reload whenever a 
file is saved.