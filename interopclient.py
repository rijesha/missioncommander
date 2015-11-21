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
        login = self.s.post(baseurl+loginurl, data=data)

    def getobstacleinfo(self):
        ob = self.s.get(baseurl+"/api/obstacles")
        obdict = ast.literal_eval(ob.text)
        stationary = obdict.get("stationary_obstacles")
        moving = obdict.get("moving_obstacles")h 
        

        
        
        


