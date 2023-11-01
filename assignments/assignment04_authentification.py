import requests
import urllib.parse
import json
from config import configkey as cfg
from config import configkeyprivate as cfkp

# Add url to be converted to pdf.
targetUrl = "https://en.wikipedia.org"
# Use API key saved in dictionary in seperate .py file to ensure it remains secure. Don't push config.py file to github, add to gitignore.
apiKey = cfg["htmltopdfkey"]
#apiKey = "xxxxxxx"

# Get apiulr from the documentation on the html2pdf.app website.
apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'url': targetUrl,'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)
requestUrl = apiurl +"?" + parsedparams

response = requests.get(requestUrl)
print (response.status_code)

result = response.content
with open("document.pdf", "wb") as handler:
    handler.write(result)

