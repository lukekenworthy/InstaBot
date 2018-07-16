from selenium import webdriver
import time
import random
from selenium.webdriver.common.action_chains import ActionChains

# hi

USERNAME = "ilovecutedogs"  # Add your Instagram username here
PASSWORD = "cuteDogsAreGr9"  # Add your Instagram password here
HASHTAG_LIST = ["notcats", "dogs", "puppies", "cute", "cutedogs"]  # Add the hashtags you want to comment on

# Add a list of phrases you want to comment
COMMENT_LIST = ["Wow!", "Love this!!!", "Amazing", "Astounding!", "incredible!", "So great!!!"]

# Average amount of time you want to wait between comments. (It's recommended that this is a low number so
# you reduce the likelihood of your account getting flagged.
AVERAGE_COMMENT_FREQUENCY = 80

# Input the directory location of your webdriver.
BROWSER = webdriver.Chrome("C:\\Users\\Luke Kenworthy\\Documents\\chromedriver.exe")

commentListLength = len(COMMENT_LIST)
fileCounter = 0
followedAccounts = []

def main():
    BROWSER.get('http://www.instagram.com')
    login(USERNAME, PASSWORD)
    while True:
        for hashtag in HASHTAG_LIST:
            goToHashTagPage(hashtag)
            goToTopPicsOnHashPage()

# Logs into Instagram
def login (username, password):
    goToSignIn = BROWSER.find_element_by_link_text("Log in")
    goToSignIn.click()

    time.sleep(.87)

    fillUsername = BROWSER.find_element_by_xpath("//*[@aria-label='Phone number, username, or email']")
    fillUsername.send_keys(username)

    time.sleep(.34)

    fillPassword = BROWSER.find_element_by_xpath("//*[@aria-label='Password']")
    fillPassword.send_keys(password)

    time.sleep(.24)

    clickLogin = BROWSER.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/span/button")
    clickLogin.click()

    time.sleep(.89)

# Goes to the page that explores hashtags on Instagram
def goToHashTagPage (hashtag):
    lowerHashtag = hashtag.lower() + "/"
    newURL = "https://www.instagram.com/explore/tags/" + lowerHashtag
    BROWSER.get(newURL)

# Goes to between six and nine of the most recent images in a hashtag and calls commentOnPicAndLike on each one
def goToTopPicsOnHashPage():
    global fileCounter
    counter = 0
    limit = random.randrange(6, 9)
    childLinks = BROWSER.find_elements_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div//a")
    if childLinks:
        for element in childLinks:
            if element:
                try:
                    global followedAccounts
                    actions = ActionChains(BROWSER)
                    actions.move_to_element(element).perform()

                    time.sleep(1.34)

                    element.click()

                    time.sleep(.87)

                    postCreator = BROWSER.find_elements_by_xpath("/html/body/div[3]/div/div[2]/div/article/header/div[2]//a")
                    if postCreator:
                        account = postCreator[0].text
                        if account not in followedAccounts:
                            commentOnPicAndLike()
                            time.sleep(random.randrange(AVERAGE_COMMENT_FREQUENCY - 30, AVERAGE_COMMENT_FREQUENCY + 30))
                        followedAccounts.append(account)


                    BROWSER.back()

                    fileCounter += 1
                    fileName = "screenshot" + str(fileCounter) + ".png"
                    BROWSER.save_screenshot(fileName)

                    time.sleep(1.03)

                    counter += 1
                    if counter >= limit:
                        break
                except StaleElementReferenceException:
                    break
            else:
                break

# Once on a post, comments on it and likes it
def commentOnPicAndLike():
    randInt = random.randrange(0, commentListLength - 1)

    like = BROWSER.find_elements_by_xpath("/html/body/div[3]/div/div[2]/div/article/div[2]//a")
    if like:
        like[0].click()

    comment = BROWSER.find_elements_by_xpath("/html/body/div[3]/div/div[2]/div/article//textarea")
    if comment:
        comment[0].clear()

    commentAgain = BROWSER.find_elements_by_xpath("/html/body/div[3]/div/div[2]/div/article//textarea")
    if commentAgain:
        commentAgain[0].send_keys(COMMENT_LIST[randInt])

        time.sleep(.33)

        commentAgain[0].send_keys(u'\ue007')


if __name__ == "__main__":
    main()