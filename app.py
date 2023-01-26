from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time, os

def SpamAsked(userid, msg, thread):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--incognito')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    url = f'https://asked.kr/{userid}'
    driver.get(url)
    time.sleep(1)
    for i in range(thread):
        try:
            driver.find_element(By.ID, "ask_content").send_keys(msg)
            time.sleep(0.5)
            driver.find_element(By.CLASS_NAME, "ask_bottom_buttom").click()
            time.sleep(2)
            driver.switch_to.alert.accept()
            time.sleep(0.3)
            print(f'{i + 1} 회차 도배를 진행하고 있습니다.')
        except Exception as e:
            print(e)
            break
    driver.quit()

def main():
    os.system("color B")
    print('딜레이는 기본적으로 가장 안정적으로 도배할 수 있게 설정되어 있습니다.')
    print('=====================================')
    ids = input("아이디를 입력하세요 : ")
    thread = int(input("횟수를 입력하세요 : "))
    msg = input("메시지를 입력하세요 : ")
    print('=====================================')

    SpamAsked(ids, msg, thread)

main()