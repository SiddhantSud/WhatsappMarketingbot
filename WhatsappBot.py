from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote 
from time import sleep
import sys

class Whatsappbot:

    def __init__(self):
        self.base_url='https://web.whatsapp.com'
        
    def extraction(self,filename):   
        phone = []
        try:
            with open (filename+".txt") as numbers_file:                    
                for line in numbers_file:
                    line=line.strip()
                    if len (line)==10:                                    
                        phone.append(str(line))
            return phone
        except:
            return "Fail"
        

    def send_messages(self,phone:list,msg:str):
        driver = webdriver.Chrome('./chromedriver')
        msg = quote(msg)
        
        driver.get(self.base_url)
        
        sleep(2)
        login_status=input("Enter 'Done' once logged in \n")
        if(login_status =='Done'):
            for number in phone:
                url = "https://web.whatsapp.com/send?phone=91" + number+ "&text=" + msg
                driver.get(url)
                sleep(5)
                print ('Message sending to '+ str(number)) 
                for i in range(70):
                    try:
                        driver.find_element_by_class_name('_1U1xa').click()
                        driver.execute_script("window.onbeforeunload = function() {};")
                        break
                    except:
                        print("not yet")
                        sleep(1)
                print ('Message sent to '+ str(number))
            print ("Done")

if __name__ == '__main__':

    bot = Whatsappbot()
    while (True):
        filename=input("Enter txt file name without extention \n")
        print(filename)
        phone_number= bot.extraction(filename)
        if(phone_number =="Fail"):
            print("File does not Exist, Try again\n")
        else:
            print("File extracted safely")
            break
    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    data = sys.stdin.read()
    print(data)
    print()
    bot.send_messages(phone_number,data)
