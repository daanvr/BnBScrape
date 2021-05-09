from selenium import webdriver
import re


DRIVER_PATH = '/Users/daan/Library/Mobile Documents/com~apple~CloudDocs/GitHub project/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# driver.get('https://www.chambresdhoteszoeken.nl/listing/villa-orangere-bb-chambres-dhotes/')
driver.get('https://www.chambresdhoteszoeken.nl/listing/villa-hortensia-gite-bb-chambres-dhotes/')

adres = driver.find_element_by_xpath('//*[@id="top"]/div[2]/div/aside/div[2]/div[1]/span').text
print(adres)
phone = driver.find_element_by_xpath('//*[@id="top"]/div[2]/div/aside/div[2]/div[2]/span/a').text
print(phone)
mail = driver.find_element_by_xpath('//*[@id="top"]/div[2]/div/aside/div[2]/div[3]/a').text
print(mail)
website = driver.find_element_by_xpath('//*[@id="top"]/div[2]/div/aside/div[2]/div[4]/a').text
print(website)
price = driver.find_element_by_xpath('//*[@id="top"]/div[2]/div/aside/div[2]/div[5]/span').text
print(price)
region = driver.find_element_by_xpath('//*[@id="top"]/div[2]/div/aside/div[2]/div[6]/span').text
print(region)
js = driver.find_element_by_xpath('//*[@id="top"]/div[2]/div/aside/div[1]/script').get_attribute('innerHTML')
latLng = re.findall("(\d+\.\d+)", js)
print(latLng[2])
print(latLng[3])

driver.quit()

# https://www.chambresdhoteszoeken.nl
# https://www.chambresdhoteszoeken.nl/listing/villa-orangere-bb-chambres-dhotes/
# https://www.scrapingbee.com/blog/selenium-python/
# https://regexr.com
