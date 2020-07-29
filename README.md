# WhatsApp Bulk Messenger :loudspeaker:

## :dart: What it does 
This tool sends messages to all the contacts you give it from a text file on your computer. *The numbers dont have to be saved in your contacts list*

## :rocket: Getting Started 

### :link: Dependencies

1. **Google Chrome** : I expect you've it already installed.
2. **Chromedriver** : Please follow the commands to download Chromedriver or from the [official download page](https://sites.google.com/a/chromium.org/chromedriver/downloads).

    `wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip`
	
	`unzip chromedriver_linux64.zip`
	
	Once downloaded you can configure it by using:
	
	`sudo mv chromedriver /usr/bin/chromedriver`
	
	`sudo chown root:root /usr/bin/chromedriver`
	
	`sudo chmod +x /usr/bin/chromedriver`
	
	_**Process for installing Chromedriver on Windows is also the same as above.**_
	
### :walking: Basic installation 

1. `Git clone` this project from your terminal or download the zip from GitHub web.
2. `cd` to the project folder.
3. Install the requirements using `pip install -r requirements.txt`

### :iphone: Adding Phone Numbers
You can export an excel file containing only the numbers of the people you need to send the message to in txt format.
Make sure the file is in the same directory

### :running: Running
1. When you execute `Whatsappbot.py`, you can enter the file name that contains all the phone numbers.
2.The program will guide you through th rest of the process.
3. Keep your phone ready and ensure you have a stable high speed internet connection to make the process smoooth.

## :stars: Advanced Tips and Tricks

1. You can add individual messages for each contact, however that will require elementary knowledge in Python, this could be done using a file for input, and might be included in future releases.
2. For using country codes other than India but only one country, please change it in the `url` string in `Whatsappbot.py`.
3. For multiple countries, please remove the _91_ from `url` string, and prepend each number directly with the country code, without plus symbol, for example 19876543210, where 1 is prepended for the US.
4. You can use any browser, not just Chrome as long as it has a supporting webdriver and install it manually.

## :dragon: Debugging
This program uses a CSS Selector to find out where exactly to write the message, just like a human would. And that keeps changing over time based on how [WhatsApp Web](web.whatsapp.com) is designed. So all we have to do is update the CSS Selector in the code, by doing the following:

That's it. :smiley:

## :performing_arts: Disclaimer
This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by WhatsApp or any of its affiliates or subsidiaries. This is an independent and unofficial software. The developers claim no responsibility for your use of it.
