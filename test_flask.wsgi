from app import app

activate_this = '/var/www/html/test_flask/env/bin/activate_this.py'
with open(activate_this) as file_:
	exec(file_.read(), dict(__file__=activate_this))
