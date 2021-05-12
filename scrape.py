from selenium import webdriver

DRIVER_PATH = '/Users/daan/Library/Mobile Documents/com~apple~CloudDocs/GitHub project/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.chambresdhoteszoeken.nl')

# url = driver.find_element_by_name('a').herf
all_links = driver.find_elements_by_tag_name('a')

for x in all_links:
    print(x.get_attribute('href'))
driver.quit()
 