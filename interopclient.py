import requests
import ast
baseurl = "http://localhost:8000"
username = "testuser"
password = "testpass"


class Connection():

    def __init__(self):
        self.loginsucess = False
        self.s = requests.Session()
        data = {"username":username, "password":password}
        loginurl = "/api/login"
        try:
            self.login = self.s.post(baseurl+loginurl, data=data)
            self.loginsucess = True
            pass
        except Exception as e:
            print("Failed to login to interop server")
            pass


    def getobstacleinfo(self):
        ob = self.s.get(baseurl+"/api/obstacles")
        objects = ast.literal_eval(ob.text)
        return objects

    def updatetelemetry(self, tele):
	print("Updating telemetry")
	print(tele)
        tl = self.s.post(baseurl+"/api/telemetry", tele )
	print(dir(tl))
	print(tl.status_code)
