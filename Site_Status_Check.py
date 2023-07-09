import requests
from selenium import webdriver

url = "https://app.haveloc.com/"

statuses = {
    200: "Website Available",
    301: "Permanent Redirect",
    302: "Temporary Redirect",
    404: "Not Found",
    500: "Internal Server Error",
    503: "Service Unavailable"
}

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")

web_response = requests.models.Response()
web_response.status_code = -1

def notify():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)

    inp = str(input())
    print("OK ",inp)
    driver.quit()

if __name__ == '__main__':
    while(True):
        try:
            web_response = requests.get(url)
            print(url, statuses[web_response.status_code])

            if web_response.status_code == 200:
                print("Status Code: ",web_response.status_code)
                notify()
                break
        except:
            print("Status Code: ",web_response.status_code)
