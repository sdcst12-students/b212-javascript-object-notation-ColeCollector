#!python3
import requests
import json

# we can use requests to retrieve json encoded data from the internet
# there are different methods that we can retrieve the data with: POST and GET
# You can google the difference between POST and GET requests


# Use the json encoded data that is retrieved from this website and print out the weekly menu
# You will need to decipher the json decoded data to determine what information the 
# dictionary object contains


class task2:
    import json
    def __init__(self):
        req = requests.get('http://sdcaf.hungrybeagle.com/menu.php')
        data = json.loads(req.text)

        for i in data['menu']:
            menu = list(i.values())
            print(" ")
            for i in range(1,len(menu)-1):
                print(menu[i])
            
task2()
            