# Run a script in the cloud to gain Instagram followers

I used Python with the Selenium package to automate liking and commenting on Instagram photos that are marked with specified hashtags. If you want to run this on the Google Compute Engine (so that it can run indefinitely and not on your local computer), perform the following steps:

1. Go [here](https://console.cloud.google.com/compute/instances) to create a Google Compute Engine instance. You will also have to make a project if you don't have one already or if you want this to be separate. If you are new, you can get a free 1 year trial with $300 dollars of credit. Don't use your own money for this because that would be sad! Do all of the standard options. I'm running a Debian GNU/Linux 9 for this project.

2. Wait for it to set up then click SSH to connect to the instance. It will take a hot minute but be patient...

3. Run the following code in the terminal. It should take a few minutes to get set up. Credit to @garywu for this script. (Just press enter when it asks about keyboard configurations.)

```bash
wget https://raw.githubusercontent.com/garywu/gae-selenium/master/install.sh && chmod +x install.sh && ./install.sh &&  ./start_headless.sh && ./demo.py
```

4. Next you'll want to get the script into the app engine. There are many ways to do this, but I found that the easiest for doing something simple like this was to upload the script to a Cloud Storage folder and then port it in. To do this, go to your [console dashboard,](https://console.cloud.google.com/home/dashboard) click the navigation bar in the top left corner, then under the "storage" section, click "browser," and "Create Bucket." Use the standard settings and you should be golden.

5. Download instabotting.py then upload it into your bucket with the "upload files" button.

6. Then, in your Compute Engine instance, run the following: (code credit to Google)

```bash
gsutil cp gs://[BUCKET_NAME]/instabotting.py [OBJECT_DESTINATION]
```
with your respective bucket and file name. Fun fact, you have to take out the brackets when you actually type it! That got me the first time. Also, if you just want to save the file to whatever directory you're in, just use a period as the object destination.

7. Now you will need to export your password as an environmental variable for the program. To do this, run:

```bash
export PASSWORD=[YOUR_PASSWORD]
```

8. Then run the following: (Credit to [this](https://stackoverflow.com/questions/47541472/run-python-script-on-google-cloud-compute-engine) Stack Overflow answer)
```bash
chmod +x instabotting.py
```
and then 
```bash
nohup python ~/instabotting.py &
```

9. And then you're all set! You should be able to close your terminal now and this will run in the background! you can enter the command 
```bash
cat nohup.out
```
to view the error log and see if your program has stopped.

10. If you want to stop the process, run
```bash
ps -ef
```
then find the PID of instabotting.py and run 
```bash
kill [PID]
```
to end it.

11. And that's all you should need to know! You can make sure that it is working on your Instagram account by going to your profile, clicking "settings", then going to "Posts you've liked"

Note: This project is still passively in development. I plan on catching certain errors in the future that have been known to come up so that the bot will continue running after it encounters them. I acually did this on a previous version but I haven't moved it over yet.