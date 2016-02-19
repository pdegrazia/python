import resources
import requests
import json


class ApiLibrary:
    def __init__(self):
        self.response = None

    def navigate_to(self,section):
        self.response = requests.get(resources.BASE_URL+'/get/%s.json?api_key=%s' % (section,resources.API_KEY))

    def show_response(self):
        data = self.response.json()
        print json.dumps(data,indent=4,sort_keys=True)
        
if __name__ == '__main__':
    conn = ApiLibrary()
    conn.navigate_to('genres')
    conn.show_response()