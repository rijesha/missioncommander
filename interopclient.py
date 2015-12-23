import requests
import ast
baseurl = "http://localhost:8000"
username = "testuser"
password = "testpass"


class Connection():

    def __init__(self):
        self.s = requests.Session()
        data = {"username":username, "password":password}
        loginurl = "/api/login"
        try:
            login = self.s.post(baseurl+loginurl, data=data)
            pass
        except Exception as e:
            print("failed to login")
            raise


    def getobstacleinfo(self):
        ob = self.s.get(baseurl+"/api/obstacles")
        objects = ast.literal_eval(ob.text)
        return objects
