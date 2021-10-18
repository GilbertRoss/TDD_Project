from scraper import loadPage, parsePage
import pytest
import requests

class TestClass:
    def testEmptyAuthor(self):
        with pytest.raises(Exception) as excinfo:
            html = loadPage('', 'Easy on me')
        assert str(excinfo.value) == "Name or Author is empty!"

    def testEmptyName(self):
        with pytest.raises(Exception) as excinfo:
            html = loadPage('Adele', '')
        assert str(excinfo.value) == "Name or Author is empty!"


    def testPageLoad(self):
        html = loadPage('Adele', 'Easy on me')
        assert html.find("Adele")  != -1
    
    def testPageParser(self):
        html = loadPage('Adele', 'Easy on me')
        raw_data = parsePage(html)
        assert raw_data.find('[Verse 1]') != -1 

    ### testing api 

    def testApiEquals200(self):
        response = requests.post("http://localhost:8080", data={'name':'Easy on me', 'author':'Adele'})
        assert response.status_code == 200

    def testApiEqualJsonContent(self):
         response = requests.post("http://localhost:8080", data={'name':'Easy on me', 'author':'Adele'})
         assert response.headers["Content-Type"] == "application/json"

    def testApiEqualNoCache(self):
         response = requests.post("http://localhost:8080", data={'name':'Easy on me', 'author':'Adele'})
         assert response.headers["Cache-Control"] == "no-cache"
    
    def testApiContent(self):
        response = requests.post("http://localhost:8080", data={'name':'Easy on me', 'author':'Adele'})
        response_body = response.json()
        assert response_body['lyrics'].find("[Verse 1]") != -1
