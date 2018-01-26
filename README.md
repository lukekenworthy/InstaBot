# InstagramBot
Uses Selenium within Python to automate commenting and liking posts with certain hashtags to gain followers.

To start, you will need to download a webdriver. I used the Google Chrome Webdriver at https://sites.google.com/a/chromium.org/chromedriver/downloads. 
Then, in the code where BROWSER is initiated, you need to input the directory location of your webdriver.
Note, if you use a webdriver other than Chrome's, you will need to use the appropriate Selenium command for that
driver. Besides that, you just need to edit the username, password, comment list, hashtag list, and average comment
frequency as you want the program to function. Once all of the UPPERCASE variables are modified, the program will start 
commenting on and liking photos with the list of comments that you gave on the list of hashtags that you gave. Actual
following results may vary. I was able to average about 2-3 likes per hour, which can add up if you leave it running 
long enough. The program will also add a screenshot of the hashtag page to whatever directory it is saved in after it
has commented. This is useful because it lets you know how many comments and like you have done when you have ran it
AND you can tell if Instagram has stopped allowing you to comment temporarily because it will give a message along the
lines of "You are not allowed to comment" on that page after you have commented.
