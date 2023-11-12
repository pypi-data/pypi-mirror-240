from datetime import * 
import requests
from urllib.parse import unquote
import json

CLASSCHARTS_URL = "https://www.classcharts.com"

def hasTimePassed(past: datetime, seconds: int):
    return not datetime.now(past.tzinfo) - past < timedelta(0,seconds) 

class Client:
    def __init__(self,api_base: str):
        self.studentId = 0
        self.sessionId = ""
        self.lastPing = datetime.now()
        self.API_BASE = api_base
        self.PING_INTERVAL = 3
        self.session = requests.Session()
    
    def makeApiRequest(self,path: str,updateSession: bool,data):
        if (updateSession and self.lastPing and hasTimePassed(self.lastPing, self.PING_INTERVAL)):
            self.updateInformation()

        response = self.session.post(
            url=path,
            headers={"Authorization": "Basic " + self.sessionId},
            data=data
        )        
        
        return response
    
    def getApiResponse(self,path: str, updateSession: bool):
        if (updateSession and self.lastPing and hasTimePassed(self.lastPing, self.PING_INTERVAL)):
            self.updateInformation()

        print(self.sessionId)
        response = self.session.get(
            url=path,
            headers={"Authorization": "Basic " + self.sessionId,     
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            },
        )        
        
        return response
    
    def getJsonResponseWithField(self,path: str, fields: str):
        response = self.getApiResponse(self.API_BASE + "/" + path + "/" + str(self.studentId) + fields,True)        
        return response.json()["data"]
    def getJsonResponse(self, path: str):
        return self.getJsonResponseWithField(path,"")
    
    def getNewSessionId(self, pingJson):
        if ("meta" not in pingJson): return
        if ("session_id" not in pingJson["meta"]): return

        print(pingJson)

        self.sessionId = pingJson["meta"]["session_id"]
        self.lastPing = datetime.now()

    def updateStudentId(self, pingJson):
        if ("data" not in pingJson): return
        
        data = pingJson["data"]

        if ("user" not in data): return
        if ("id" not in data["user"]): return

        self.studentId = data["user"]["id"]        

    def updateInformation(self):
        response = self.makeApiRequest(self.API_BASE + "/ping",False,"")
        responseJson = response.json()

        self.getNewSessionId(responseJson)
        self.updateStudentId(responseJson)


class StudentClient(Client):
    def __init__(self, studentCode: str, dateOfBirth: str):
        super().__init__(CLASSCHARTS_URL + "/apiv2student")

        self.studentCode = studentCode
        self.dateOfBirth = dateOfBirth

    def login(self):
        if (self.studentCode == None or self.studentCode == ""): raise Exception("Student Code not provided")

        formData = {
            "code": self.studentCode,
            "dob": self.dateOfBirth,
            "remember_me": 1
        }

        self.session.cookies.clear()

        response = self.session.post(
            url=CLASSCHARTS_URL + "/student/login",
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
            },   
            data=formData,
            allow_redirects=False
        )        

        if ("set-cookie" not in response.headers): return

        cookie = json.loads(unquote(response.cookies.items()[1][1]))

        self.sessionId = cookie["session_id"]
        self.lastPing = datetime.now()
        self.updateInformation()