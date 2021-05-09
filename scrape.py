from selenium import webdriver

DRIVER_PATH = '/Users/daan/Library/Mobile Documents/com~apple~CloudDocs/GitHub project/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.chambresdhoteszoeken.nl')

# url = driver.find_element_by_name('a').herf
all_links = driver.find_elements_by_tag_name('a').herf

print(all_links)
driver.exit()
# .bt_bb_listing_box_inner > a

# h1 = driver.find_element_by_name('h1')

# //*[@id="bt_bb_section609608fa75758"]/div/div/div/div[1]/div/div/div/div/div[2]/div/div[30]/div/a
# #bt_bb_section609608fa75758 > div > div > div > div:nth-child(1) > div > div > div > div > div.bt_bb_featured_listings.bt_bb_featured_listing_image_content.bt_bb_columns_4.bt_bb_gap_normal > div > div:nth-child(30) > div > a