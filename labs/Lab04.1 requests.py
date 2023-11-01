#Lab04.1
#Author Emma Dunleavy

import requests

URL = "http://andrewbeatty1.pythonanywhere.com/books"

#url = "http://google.com"
#response = requests.get(url)
#print (response.text)


#response = requests.get(URL)
#print (response.json())

def readbooks():
    response = requests.get(URL)
# we could do checking for correct response code here
    return response.json()

def readbook(id):
    geturl = URL + "/" + str(id)
    response = requests.get(geturl)
# we could do checking for correct response code here
    return response.json()



if __name__ == "__main__":
    print(readbook())
    print (readbooks())