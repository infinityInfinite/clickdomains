from bs4 import BeautifulSoup
import requests

'''
List of errors{
 Aws error
 blank
 repeated
}

'''

def test():
    req = requests.get("https://battlebreakers-live-cdn.ol.epicgames.com/")
    aws_error(req)

def aws_error(req):
    contents = req.text
    soup = BeautifulSoup(contents,"xml")
    code = soup.find('Code')
    if code:
        return True
    else:
        return False

def blank(req):
    contents = req.text
    if req.txt == "":
        return True
    else:
        return False
    

test()
    
