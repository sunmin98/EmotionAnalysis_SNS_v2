from INSTA_PACKAGE.instaloader import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

instance = instaloader.Instaloader()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os
import shutil

Sns_lists = []
instance = instaloader.Instaloader()
insta_name = str(input("인스타 이름 입력 -> "))
instance.download_profile(profile_name=insta_name, max_count=5, txt_list=Sns_lists)
print("\nSns_lists -> ",Sns_lists)
shutil.rmtree(insta_name)