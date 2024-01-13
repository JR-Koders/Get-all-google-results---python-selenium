
# webdriver is the most basic thing we need for a selenium project
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# By helps selecting elements ex: "By.ID"
from selenium.webdriver.common.by import By

# to be able to wait some time
from time import sleep

# Create a new instance of the webdriver, you could also use webdrive.chrome()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

# this query is going to be looked for on google, and the results fetched
query = "whatever you want"

driver.get("https://google.com")

# wait for a few seconds
sleep(5)


# Find the search bar element by name attribute
search_bar = driver.find_element(By.NAME, "q")

# Type "test" into the search bar
search_bar.send_keys("test")
print("sent keys")

# Press Enter to perform the search
search_bar.send_keys(Keys.RETURN)

# Wait for a few seconds (you can adjust the time based on your internet speed)
sleep(5)

print("***Starting the scroll***")

while True: 
    # this scrolls to the bottom of the webpage
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    sleep(.5)

    try:
        # trying to find the "more results" button
        # NOTE: the name of the class will probably be changed by the time you use this script!!!
        # to resolve that issue, just right-click on the "more results" button and copy-paste the class name
        moreResults = driver.find_element(By.CLASS_NAME, "kQdGHd")
        
        print("blocked, clicking on more result button")
        moreResults.click()
    except:
        # if the script couldn't find any "more results" button, it means we reached the bottom of the search
        print("couldn't find any more results button")
        break

sleep(1)


# NOTE: Now it's time to parse the results!!!
from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, "lxml")

# intializing the lists
listOfDiscoveredLinks = []

print("starting analysis", end='\r')
# NOTE: here again, the class name may change, so just right-click on results urls and copy-paste the class name
for link in soup.find_all('a', {'jsname': 'UWckNb'}):
    try:
        listOfDiscoveredLinks.append(link['href'])
    except:
        pass

print("*****************Finished analysis!!!*******************\n")

print("\nnumber of links found:", len(listOfDiscoveredLinks))
print("List of found links:", listOfDiscoveredLinks)






# Close the browser window
driver.quit()



