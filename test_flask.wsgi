import sys 
import logging 

logging.basicConfig(stream=sys.stderr) 
sys.path.insert(0,"/var/www/html/test_flask") 

from app import app as application 
application.secret_key = '7wU5oQhA3cihhYpOtkyvLNb5OzEixfww'