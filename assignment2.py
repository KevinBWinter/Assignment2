import re
import socket
 
class Assignment2:
    def __init__(self, year):
        self.year = year
    def tellAge(self, currentYear):
        age = currentYear - self.year
        print(f"Your age is {age}")
    def listAnniversaries(self):
        currentYear = 2024
        yearsPassed = currentYear - self.year
        anniversaries = []
        for i in range(10, yearsPassed + 1, 10):
            anniversaries.append(i)
        return anniversaries
    def modifyYear(self, n):
        year_str = str(self.year)

    
        first_part = year_str[:2] * n

        x = (self.year*2)
        
        select_str = str(x)
        second_part = ''.join([select_str[i] for i in range(len(select_str)) if i % 2 == 0])

        return first_part + second_part
    @staticmethod
    def checkGoodString(string):
        if len(string) < 9:
            return False
 
      
        if not string[0].islower():
            return False
 
     
        if len(re.findall(r'\d', string)) != 1:
            return False
 
        return True
    @staticmethod
    def connectTcp(host, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
          
            sock.connect((host, port))
 
        
            sock.close()
 
            return True
        except:
            return False

 
 
x = Assignment2(1996)
 
x.tellAge(2024)
 
y = x.listAnniversaries()
print(y)
 
ret = x.modifyYear(3)
print(ret)
 
ret = Assignment2.checkGoodString("f1obar0more")
print(ret)  # Should print False
 
ret = Assignment2.checkGoodString("foobar0more")
print(ret)  # Should print True
 
retval = Assignment2.connectTcp("www.google.com", 80)
if retval:
    print("Connection established correctly")
else:
    print("Some error")
 
