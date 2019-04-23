from bottle import Bottle, response, request
import os
from bottle import route, run, template,view

"""
test web application in bottle/templates
"""

@route('/about')
def about():

    result =  "<p>Your IP address is:" + request.remote_addr + "</p>"
    result += "<p>Your browser is: " + request.environ['HTTP_USER_AGENT'] + "</p>"

    return result





index_html = ''' Testing bottle for web app! Test input: <strong>{{ author }}</strong>.'''


@route('/templates/')
@view('/templates/')
def index():
  info={ 'title':'hi there!',
        'content':'hello!'
        }
  return template('index2.tpl',templatepage='test.pl', variable=info )

@route('/test')
@view('/test')
def index(): 
  return template('index.tpl',variable='some content', headertitle='test header page' )


@route('/')
def index():
    return template(index_html, author='Test 123!')


@route('/name/<name>')
def name(name):
    return template(index_html, author=name)

    
if __name__ == '__main__': 
    port = int(os.environ.get('PORT', 80))
    run(host='0.0.0.0', port=port, debug=True)
    
    
