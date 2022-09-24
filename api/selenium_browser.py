from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

print("[*] Starting selenium chrome-browser ...")
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--no-sandbox")
opt.add_argument("--disable-dev-shm-usage")
opt.add_argument("--single-process")
opt.add_argument("--disable-gpu")
opt.add_argument("--disable-dev-tools")
opt.add_argument("--no-zygote")
opt.add_argument("--disable-gpu")
driver = webdriver.Chrome(executable_path=ChromeDriverManager(path="/tmp").install(),options=opt,service_log_path="/tmp")

def get(url):
	driver.get(url)
	result = driver.page_content
	driver.close()
	return result
