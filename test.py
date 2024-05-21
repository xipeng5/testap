import json
import random
import time
import requests
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.common import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from mhttp.ProxyRetriever import get_http_proxy
from mhttp.ProxyRetriever import fetch_content_from_proxy
from mhttp.ProxyRetriever import get_http_proxy_to_time
from bean.AppleCountry import CountryEnum
from presenter.AppleSumbmitBtn import input_content
from moudel.emailmd.EmailRegister import send_register_email
from bean.NameGenerator import get_generate_user_name
from bean.PasswordGenerator import get_generate_password
from seleniumbase import Driver
from seleniumbase import SB
from random import randint, seed
from fake_useragent import UserAgent
from selenium_stealth import stealth

def get_apple_account_id():
    try:
        time.sleep(3)
        apple_registration_url = "https://appleid.apple.com/account"

        proxy_host = 'customer-baf7303aede-country-US:38b2d569@proxy.shenlongproxy.com:31212'
        args = '"--lang=en-US","--disable-web-security","--disable-gpu","--no-sandbox","--disable-dev-shm-usage","--disable-features=NetworkService","--disable-features=VizDisplayCompositor","--disable-software-rasterizer"'
        start_time = time.time()
        ua = UserAgent()
        while True:
            random_user_agent = ua.chrome
            if "Windows" not in random_user_agent:
                print(random_user_agent)
                continue
            break
        driver = Driver(uc=True, headless=False, uc_subprocess=True, uc_cdp_events=True, uc_cdp=True,
                        log_cdp=True, log_cdp_events=True, undetectable=True, chromium_arg=args,
                        swiftshader=True, agent=random_user_agent, proxy=proxy_host)

        driver.set_window_rect(randint(4, 720), randint(8, 410), 700, 900)
        driver.uc_open_with_reconnect(apple_registration_url, reconnect_time=10)
        stop_time = time.time()

        number='4435439820'
        first_name, last_name = get_generate_user_name()
        driver_password = get_generate_password()
        # email = send_register_email(proxy_host)
        email = ''
        input_content(driver, first_name, last_name, driver_password, number, email)

        print("seleniumbase time:", stop_time - start_time)

        time.sleep(5000)


    except Exception as e:
        print(f"错误: {e}")
    finally:
        # 不论是否发生异常，最后都关闭浏览器窗口
        # driver.quit()
        pass


def input_content(driver,user,name,password,number,email):
    # 姓氏和名字的级别 1是姓氏  2是名字
    common_xpath = '(//div[@role="main"]/div[@class="flow-section account-info-section"]/div[@class="container-xs centered"]/div[@class="form-table"]//div[@class="column large-6 medium-6 small-6"])'
    driver.type(f'{common_xpath}[1]//input', user)
    driver.type(f'{common_xpath}[2]//input', name)
    # 输入出生日期
    random_birthday = str(generate_birthday())
    driver.type('(//div[@role="main"]/div[@class="flow-section account-info-section"]//div[@class="row"])[2]//input',
                random_birthday)
    email='cimdxoqap00123@gmail.com'
    # number='2312593263'
    # 邮箱地址
    driver.type('((//div[@role="main"]/div[@class="flow-section"])[1]//input)[1]',email)
    # 输入密码
    driver.type('((//div[@role="main"]/div[@class="flow-section"])[1]//input)[2]', password)
    # 确认密码
    driver.type('((//div[@role="main"]/div[@class="flow-section"])[1]//input)[3]', password)
    # 输入电话号码
    driver.type('((//div[@role="main"]/div[@class="flow-section"])[2]//input)[1]', number)


if __name__ == '__main__':
    get_apple_account_id()


POST /account/validate HTTP/1.1
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: keep-alive
Content-Length: 1011
Content-Type: application/json
Cookie: idclient=web; dslang=GB-EN; site=GBR; aidsp=B87469363B9109ABC87843A161FD98988DC892ADEE1F43F00F9502E1547839E5767DFACED25F9D188AEB3DCD6DAFA9236680EABBD3DB341AD0AE1D63AFA2B6ED1AE20407A2399BC7193F79A23A57CEC285AF6E89EF486582A41504F1B131186322B486B3567CECF03187731B0C5CF2306F01F65724110EA5; geo=US; aid=7CCF09F14E7DE5325D723E42594EF63B
Host: appleid.apple.com
Origin: https://appleid.apple.com
Referer: https://appleid.apple.com/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36
X-APPLE-HC: 1:12:20240521064707:0ccfad9fd7704f362a39c54a412303f5::1446
X-Apple-Api-Key: cbf64fd6843ee630b463f358ea0b707b
X-Apple-I-FD-Client-Info: {"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36","L":"en-GB","Z":"GMT+08:00","V":"1.1","F":".ta44j1e3NlY5BNlY5BSmHACVZXnNA9J1dJxOTrOHQxQkmbFVDJhCixGMuJjkW5BN8Qs.xLB.Tf1XbFaDK1cDvmWUW1zIq5BNlY5CGWY5BOgkLT0XxU..8rt"}
X-Apple-I-TimeZone: Asia/Shanghai
X-Apple-ID-Session-Id: B87469363B9109ABC87843A161FD98988DC892ADEE1F43F00F9502E1547839E5767DFACED25F9D188AEB3DCD6DAFA9236680EABBD3DB341AD0AE1D63AFA2B6ED1AE20407A2399BC7193F79A23A57CEC285AF6E89EF486582A41504F1B131186322B486B3567CECF03187731B0C5CF2306F01F65724110EA5
X-Apple-Request-Context: create
X-Requested-With: XMLHttpRequest
scnt: AAAA-0I4NzQ2OTM2M0I5MTA5QUJDODc4NDNBMTYxRkQ5ODk4OERDODkyQURFRTFGNDNGMDBGOTUwMkUxNTQ3ODM5RTU3NjdERkFDRUQyNUY5RDE4OEFFQjNEQ0Q2REFGQTkyMzY2ODBFQUJCRDNEQjM0MUFEMEFFMUQ2M0FGQTJCNkVEMUFFMjA0MDdBMjM5OUJDNzE5M0Y3OUEyM0E1N0NFQzI4NUFGNkU4OUVGNDg2NTgyQTQxNTA0RjFCMTMxMTg2MzIyQjQ4NkIzNTY3Q0VDRjAzMTg3NzMxQjBDNUNGMjMwNkYwMUY2NTcyNDExMEVBNXwxMwAAAY-Z9gAd1PJMG_V-EouI-WjIJiV84MluNULXTgsUJ28ACsStRjyOe0pRe4gLEAANJjIALggxopUbHQvfXmx985f370og0WADcLfNuHQw-yM-Hr3cMkg
sec-ch-ua: "Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"


返回信息
{
  "service_errors" : [ {
    "code" : "-34607001",
    "title" : "Could Not Create Account",
    "message" : "Your account cannot be created at this time.",
    "suppressDismissal" : false
  } ],
  "hasError" : true
}
