*Install latest version of python and download either Chrome or FireFox webdriver. Please find the installation steps in the below link.
https://www.geeksforgeeks.org/selenium-python-introduction-and-installation/


*Make sure you have downloaded the selenium as well as other required packages before you start working on this, you can find the required packages in the "requirements.txt" file.


*Make sure that you have enabled two step verfication for the gmail account that you intend to mail from, after that you create a app password which helps you not to put in your actual password of your gmail account. In order to create a app password, follow the below steps:
Click on profile --> Manage your google account --> Security(Found at left side corner) --> In security, go to Signing in to Google section, under this you will find App passwords(this is visible only if you enabled two step verification) --> A pop-up comes asking for gmail account password --> Under "Select the app and device you want to generate the app password for" section select the app as "Other(custom name)" and then enter the name of your choice and then click on generate.



![Screenshot 2022-04-17 at 4 12 19 PM](https://user-images.githubusercontent.com/60035403/163711019-eee5867a-8f41-4762-9629-cb1345ca724e.png)



*Now you will get the app password and you can use this app password to login, instead of actual password .


*Also make sure that under security section turn on "Access for less secure apps setting" feature, so that you can automate the login process with python very easily without any security related errors.




In this project, I am logging into my college portal to check the availability of the seats for specific courses. I have automated this code using selenium in such a way that, it logs into portal, takes the screenshots of page results by searching for the specific course and then mails those screenshots to a gmail account. For mailing those screenshots to a gmail account, I have automated in such a way that it logs into my gmail account then sends those screenshots through my account.You can refer the below image, for output purposes:


![Screenshot 2022-04-17 at 4 40 31 PM](https://user-images.githubusercontent.com/60035403/163711948-843c53d1-c7df-459d-951c-dd164c129417.png)





Reference links that I have used for doing this project:

https://www.geeksforgeeks.org/selenium-python-tutorial/

https://realpython.com/python-send-email/

https://stackoverflow.com/questions/69875125/find-element-by-commands-are-deprecated-in-selenium

