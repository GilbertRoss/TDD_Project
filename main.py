from bottle import route, run, post, request, response
from scraper import loadPage, parsePage
import json

@post('/')
def listing_handler():
    author = request.forms.get("author")
    name = request.forms.get("name")
    html = loadPage(author, name)
    data = parsePage(html)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps({'lyrics': str(data)})

run(host='localhost', port=8080)