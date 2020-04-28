import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
mobile_number = input("Enter a Number with country code prefix (India : 911234567890): ")
text = str(input("Enter the message (Don't Leave extra space): "))
text = text.replace(" ","%20")
count = int(input("Enter the number of times you want to send the message : " ))
if(count == 0):
    print("By default it send the message once")
driver.get("https://web.whatsapp.com/send?phone="+mobile_number+"&text="+text+"&source=&data=&app_absent=")
input("Press ENTER key after scanning the code : ")
print("Go back to the browser and leave it open")
try:
    element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_35EW6"))
            )
finally:
    pass
submit_button = driver.find_element_by_class_name("_35EW6")
submit_button.click()
for i in range(0,count-1):
    text_box = driver.find_element_by_class_name("_2WovP")
    text_box.send_keys(text)
    submit_button = driver.find_element_by_class_name("_35EW6")
    submit_button.click()
print("Sent"+text+"to"+mobile_number)    
print("No of times message sent : ",count)