import os
import stat
import requests
from zipfile import ZipFile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

CHROME_URL = "https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-41/stable-headless-chromium-amazonlinux-2017-03.zip"
CHROMEDRIVER_URL = "https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip"

CHROME_FILE = "/tmp/headless-chromium"
CHROMEDRIVER_FILE = "/tmp/chromedriver"

if not os.isfile(CHROMEDRIVER_FILE):
	print("[*] Download chrome as ZIP file ...")
	req = requests.get(CHROME_URL)
	print("[*] Save ZIP file to /tmp dir ...")
	with open(CHROME_FILE+".zip","wb") as f:
		f.write(req.content)
	print("[*] Unzipping chrome binary ...")
	with ZipFile(CHROME_FILE+".zip","r") as zf:
		zf.extractall()
	print("[*] Make chrome binary executable ...")
	os.chmod(CHROME_FILE,os.stat(CHROME_FILE).st_mode | stat.S_IEXEC)

	print("[*] Download chromedriver as ZIP file ...")
	req = requests.get(CHROMEDRIVER_URL)
	print("[*] Save ZIP file to /tmp dir ...")
	with open(CHROMEDRIVER_FILE+".zip","wb") as f:
		f.write(req.content)
	print("[*] Unzipping chromedriver binary ...")
	with ZipFile(CHROMEDRIVER_FILE+".zip","r") as zf:
		zf.extractall()
	print("[*] Make chromedriver binary executable ...")
	os.chmod(CHROMEDRIVER_FILE,os.stat(CHROMEDRIVER_FILE).st_mode | stat.S_IEXEC)
	
print("[*] Starting selenium chrome-browser ...")
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--no-sandbox")
opt.binary_location(CHROME_FILE)
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_FILE,options=opt)

def get(url):
	driver.get(url)
	result = driver.page_content
	driver.close()
	return result
