
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

settings = {
	"email": "handballerj@hotmail.com",
	"password": "12345678910"
}

print("[*] Starting chrome ...")
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=opt)

print("[*] Visit url ...")
driver.get("https://rocket-league.com/login")

print("[*] Accept policy btn ...")
policy_button = driver.find_element(By.ID,"acceptPrivacyPolicy")
policy_button.click()

print("[*] Enter login credentials ...")
email_input = driver.find_element(By.CSS_SELECTOR,"input[type='email']")
email_input.clear()
email_input.send_keys(settings["email"])

pwd_input = driver.find_element(By.CSS_SELECTOR,"input[type='password']")
pwd_input.clear()
pwd_input.send_keys(settings["password"])

print("[*] Submit login ...")
pwd_input.send_keys(Keys.ENTER)
sleep(5)

print("[*] Save page content ...")
fname = "website_{datetime}.html".format(datetime=datetime.now())
with open(fname,"w") as f: f.write(driver.page_source)

print("[*] Click cookie 'agree'-btn ...")
agree_btn = driver.find_element(By.XPATH,"//button/span[text()='AGREE']")
agree_btn.click()
sleep(5)

print("[*] Save page content ...")
fname = "website_{datetime}.html".format(datetime=datetime.now())
with open(fname,"w") as f: f.write(driver.page_source)

print("[*] Click my-trades button ...")
trades_btn = driver.find_element(By.CSS_SELECTOR,"li a[href*='/trades/']")
print(trades_btn)
trades_btn.click()
sleep(5)

print("[*] Detect existing trades ...")
trades = driver.find_element(By.CSS_SELECTOR,"div[class='rlg-trade']")
for i,trade in enumerate(trades):
	time = trade.find_element(By.CSS_SELECTOR,"span[class='rlg-trade__time'] > span").text
	btn = trade.find_element(By.CSS_SELECTOR,"button[class='rlg-trade__bump']")
	print("trade {i}: {time}".format(i=i+1,time=time))

print("[*] Save page content ...")
fname = "website_{datetime}.html".format(datetime=datetime.now())
with open(fname,"w") as f: f.write(driver.page_source)

print("[*] Shutdown chrome ...")
driver.close()

print("[*] Done!")
