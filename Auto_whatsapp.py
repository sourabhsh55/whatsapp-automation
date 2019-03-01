from selenium import webdriver

driver = webdriver.Chrome('F:\chrome_ka_driver\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

name=input('enter the name of user : ')
msg=input('enter the message : ')
count=int(input('how many times you wanna send the msg : '))

input('enter key after scanning the QR code:-)')

user=driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_2S1VP')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
