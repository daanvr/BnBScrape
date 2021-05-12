from selenium import webdriver
import re
import csv
import json

DRIVER_PATH = '/Users/daan/Library/Mobile Documents/com~apple~CloudDocs/GitHub project/chromedriver'
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# Todo
# [ ] add exeptions code to catch if data is not available
# [ ] add more robust way of locating, some have dubbel values fot phone, this creates a scuewed data effect
# [ ] detect camping
# [ ] detect no type 

accomodations = {
    # "Domaine de l'Amiral": {
    #     "qid":"", 
    #     "Len":"", 
    #     "Den":"", 
    #     "P31":"", 
    #     "P6375":"", 
    #     "P281":"", 
    #     "P17":"", 
    #     "P1329":"", 
    #     "P968":"", 
    #     "S854":"", 
    #     "P856":"", 
    #     "qal407":"", 
    #     "P625":"", 
    #     "P973":""
    # }
}

def visitPage(url):
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get(url)

    accomodation = {
         "qid": "",
        # "Len":"", 
        # "Den":"", 
        # "P31":"", 
        "P6375":"",
        # "P281":"", 
         "P17": "Q142"
        # "P1329":"", 
        # "P968":"", 
        # "S854":"", 
        # "P856":"", 
        # "qal407":"", 
        # "P625":"", 
        # "P973":""
    }

    def findAdres():
        adres = driver.find_element_by_class_name('contact_address').text
        adres = adres.replace(", Frankrijk","")
        accomodation["P6375"] = adres

        postcode = re.findall("([0-9]{5})", adres)
        accomodation["P281"] = postcode[0]

    def findPhoneNumbers():
        try:
            phone = driver.find_element_by_class_name('contact_phone').find_element_by_tag_name('a').get_attribute('href')
            phone = phone.replace("tel:", "")
            accomodation["P1329"] = phone
        except:
            print("no phone")

        try:
            mobile = driver.find_element_by_class_name('contact_mobile').find_element_by_tag_name('a').get_attribute('href')
            mobile = phone.replace("tel:", "")
            accomodation["P1329bis"] = mobile
        except:
            print("no mobile")

    def findMail():
        mail = driver.find_element_by_class_name('contact_email').find_element_by_tag_name('a').get_attribute('href')
        accomodation["P968"] = mail

    def findOfficalWebsite():
        try:
            website = driver.find_element_by_class_name('contact_website').find_element_by_tag_name('a').get_attribute('href')
            accomodation["P856"] = website
        except:
            print("no website")

 
    # def findPrice():
    #     price = driver.find_element_by_xpath('//*[@id="top"]/div[2]/div/aside/div[2]/div[5]/span').text

    # def findRegion():
    #     region = driver.find_element_by_xpath('//*[@id="top"]/div[2]/div/aside/div[2]/div[6]/span').text

    def findNameRegionDepartmentCityType():
        nameString = driver.find_element_by_class_name('btSingleListingItem').text
        nameAndKeywoordsArray = re.findall("([^|]+)", nameString)
        # print(nameAndKeywoordsArray)
        accomodation["Len"] = nameAndKeywoordsArray[0].strip()
        # print(nameAndKeywoordsArray[-3].strip()) #region
        # print(nameAndKeywoordsArray[-2].strip()) #departement
        # print(nameAndKeywoordsArray[-1].strip()) #ville
        if " Gîtes " in nameAndKeywoordsArray:
            accomodation["P31"] = 'Q1928941' # Gite
        if " Chambres d’hôtes " in nameAndKeywoordsArray:
            accomodation["P31"] = 'Q367914' # BnB

    def findLatLng():
        js = driver.find_element_by_xpath('//*[@id="top"]/div[2]/div/aside/div[1]/script').get_attribute('innerHTML')
        latLng = re.findall("(\d+\.\d+)", js)
        accomodation["P625"] = '@' + latLng[2] + '/' + latLng[3]

    # run functions for al
    findAdres()
    findPhoneNumbers()
    findMail()
    findOfficalWebsite()
    findNameRegionDepartmentCityType()
    findLatLng()


    driver.quit()

    accomodations[accomodation["Len"]] = accomodation
    # print(accomodations)
    print(json.dumps(accomodations, indent=4, sort_keys=True))
    dataToCsv()




def dataToCsv():
    # >>> d = {'hello': 34, 'world': 2999}
    for key, value in accomodations.items():
        print(key, value)
    # ...
    # world 2999
    # hello 34


# works
# visitPage("https://www.chambresdhoteszoeken.nl/listing/villa-hortensia-gite-bb-chambres-dhotes/") # works
# visitPage('https://www.chambresdhoteszoeken.nl/listing/villa-orangere-bb-chambres-dhotes/') # Works
# visitPage('https://www.chambresdhoteszoeken.nl/listing/chateau-de-saint-etienne-bb-saint-gerand-le-puy-chambres-dhotes/') # works
# visitPage('https://www.chambresdhoteszoeken.nl/listing/camping-trezelle/') # works
# visitPage('https://www.chambresdhoteszoeken.nl/listing/chambres-dhotes-dormir-en-route-bb/') # works
# visitPage('https://www.chambresdhoteszoeken.nl/listing/a-la-vieille-ecole-bb-chambres-dhotes/') # works
# visitPage('https://www.chambresdhoteszoeken.nl/listing/aire-de-bief-bb-chambres-dhotes/') # works
# visitPage('https://www.chambresdhoteszoeken.nl/listing/au-chapitre-bed-breakfast-chambres-dhotes/') # works
visitPage('https://www.chambresdhoteszoeken.nl/listing/une-chance-de-la-france-bb-chambres-dhotes/') #works



# visitPage('')

# has problem
# visitPage('https://www.chambresdhoteszoeken.nl/listing/sans-parure/') # 2x phone
# visitPage('https://www.chambresdhoteszoeken.nl/listing/terre-de-lumiere-bb-chambres-dhotes/') # 2x phone
# visitPage('https://www.chambresdhoteszoeken.nl/listing/tiny-house-gite-het-oude-stalletje-bb-chambres-dhotes/')  # 2x phone
# visitPage('https://www.chambresdhoteszoeken.nl/listing/vakantiehuis-murol-gite/')  # 2x phone
# visitPage('https://www.chambresdhoteszoeken.nl/listing/vie-la-vie-bb-chambres-dhotes/')  # 2x phone
# visitPage('https://www.chambresdhoteszoeken.nl/listing/bb-glamping-gite-la-belle-st-fli-chambres-dhotes-gite/') # 2x phone numbers
# visitPage('https://www.chambresdhoteszoeken.nl/listing/atelier-en-route-bb-chambres-dhotes/') # 2x phone
# visitPage('https://www.chambresdhoteszoeken.nl/listing/fontaine-du-pommier-bb-chambres-dhotes/') # 2x phone numbers
# visitPage('https://www.chambresdhoteszoeken.nl/listing/fermette-labeille-bb-chambres-dhotes/') # no website
# visitPage('https://www.chambresdhoteszoeken.nl/listing/chateau-de-blomac-bb-chambres-dhotes/') # no price ==> scew list





with open('new.csv', mode='w') as csv_file:
    fieldnames = [
        "qid", "Len", "Den", "P31", "P6375", "P281", "P17", "P1329", "P968", "S854", "P856", "qal407", "P625", "P973"
    ]
    # fieldnames = [ "qid",   "Len",     "Den",              "P31",          "P6375",        "P281",         "P17",      "P1329",        "P968", "S854",      "P856",             "qal407",               "P625",  "P973"]
    #fieldnames = ["qid",   "label en","Discription en"   ,"Instance of"  ,"Street adres" ,"Postal code",  "country",  "phone number", "mail", "ref URL",   "Offical website",  "language qualifire"    ,"coordinates",        "described at URL"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({
        'Len': 'John Smith',
        'Den': 'Accounting',
        'P31': 'November'
    })
    writer.writerow({'Len': 'wer', 'Den': 'g34g4', 'P31': 'q35h j'})




# https://www.chambresdhoteszoeken.nl
# https://www.chambresdhoteszoeken.nl/listing/villa-orangere-bb-chambres-dhotes/
# https://www.scrapingbee.com/blog/selenium-python/
# https://regexr.com
