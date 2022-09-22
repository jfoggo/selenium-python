from fastapi import FastAPI
import api.selenium_browser as browser

app = FastAPI()

@app.get("*")
def send_get_request(url : str = "https://api.myip.com"):
	print("[*] Send get request to: "+url)
	try:
		res = {
			"status": True,
			"response": browser.get()
		}
	except Exception as e:
		res = {
			"status": False,
			"error": str(e)
		}
	return res
