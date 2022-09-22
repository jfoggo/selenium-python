from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("--headless")
opt.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=opt)

def get(url):
	driver.get(url)
	result = driver.page_content
	driver.close()
	return result
