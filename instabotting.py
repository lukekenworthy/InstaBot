import selenium
from pyvirtualdisplay import Display
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
import os

# Input the respective username, password, and hashtags
USERNAME = "luke_kenworthy"
PASSWORD = os.environ.get("PASSWORD")
HASHTAG_LIST = ["justinbieber", "allium", "underratedvegetable", "leeks"]
AVERAGE_COMMENT_FREQUENCY = 80
followedAccounts = set()

display = Display(visible=0, size=(1200, 800))
display.start()

browser = selenium.webdriver.Chrome("/mnt/c/users/luke kenworthy/documents/chromedriver_win32 (1)/chromedriver.exe")
# selenium.webdriver.Chrome()
# selenium.webdriver.Chrome("/mnt/c/users/luke kenworthy/documents/chromedriver_win32 (1)/chromedriver.exe")

def main():
    login(USERNAME, PASSWORD)
    print("logged in!")
    while True:
        for hashtag in HASHTAG_LIST:
            goToHashTagPage(hashtag)
            print("at hash page!")
            goToTopPicsOnHashPage()
            print("commented!")

# Logs into Instagram
def login (username, password):
    browser.get("https://www.instagram.com/accounts/login/")

    time.sleep(.87)

    fillUsername = browser.find_element_by_xpath("//*[@aria-label='Phone number, username, or email']")
    fillUsername.send_keys(username)

    time.sleep(.34)

    fillPassword = browser.find_element_by_xpath("//*[@aria-label='Password']")
    fillPassword.send_keys(password)

    time.sleep(.24)

    clickLogin = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/span/button")
    clickLogin.click()

    time.sleep(.89)

# Goes to the page that explores hashtags on Instagram
def goToHashTagPage (hashtag):
    lowerHashtag = hashtag.lower() + "/"
    newURL = "https://www.instagram.com/explore/tags/" + lowerHashtag
    browser.get(newURL)


def goToTopPicsOnHashPage():
    global fileCounter
    counter = 0
    limit = random.randrange(7, 12)
    childLinks = browser.find_elements_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div//a")
    if childLinks:
        for element in childLinks:
            if element:
                try:
                    global followedAccounts
                    actions = ActionChains(browser)
                    actions.move_to_element(element).perform()

                    time.sleep(1.34)

                    element.click()

                    time.sleep(.87)

                    # Prevent commenting on multiple posts by the same creator
                    postCreator = browser.find_elements_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]//a")
                    if postCreator:
                        account = postCreator[0].text
                        if account not in followedAccounts:
                            likePic()
                            time.sleep(random.randrange(AVERAGE_COMMENT_FREQUENCY - 30, AVERAGE_COMMENT_FREQUENCY + 30))
                        followedAccounts.add(account)

                    # Prevents set from getting too big. Int theory you should be able to have millions of elements and be safe
                    # but might as well empty it after a thousand anyway.
                    if len(followedAccounts) > 1000:
                        followedAccounts = set()

                    browser.back()

                    time.sleep(1.03)

                    counter += 1
                    if counter >= limit:
                        break
                except selenium.common.exceptions.StaleElementReferenceException:
                    print("Failure 1")
                    break
            else:
                print("Failure 2")
                break

def likePic():
    like = browser.find_elements_by_class_name("coreSpriteHeartOpen")
    if like:
        like[0].click()
        print("Successful like")

    time.sleep(1.12)

if __name__ == "__main__":
    main()