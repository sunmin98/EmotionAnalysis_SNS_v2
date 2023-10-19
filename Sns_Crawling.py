미완 수정 필요!!

# import instaloader
# from instaloader import Profile, Post
#
# instance = instaloader.Instaloader()
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import urllib.request
# import ssl
# import requests
# from selenium import webdriver
# #import re
# import time
# from selenium.webdriver.common.by import By
# import pandas as pd
# from bs4 import BeautifulSoup
# import instaloader
# from instaloader import Profile, Post
#
# instance = instaloader.Instaloader()
#
# driver = webdriver.Chrome()
# options = Options()
# options.add_experimental_option('detach', True)  # 브라우저가 바로 닫힘 방지
# options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 불필요한 에러메세지 삭제
#
# driver.get('https://www.instagram.com')
# time.sleep(1)
# # 인스타그램 로그인을 위한 계정 정보
# email = "sunmin980130@gmail.com"
# password = "!Sunmin980130"
# input_id = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(email)
# input_pw = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(password, Keys.ENTER)
# print("로그인 완료")
#
# insta_ID=input()
# instance.download_profile(profile_name=insta_ID, profile_pic=False, max_count=5)