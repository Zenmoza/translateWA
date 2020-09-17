import pyautogui
from PIL import Image
import pytesseract
import time
from googletrans import Translator
import re
import sys
import pyautogui
import requests

pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract-ocr\tesseract'

trans = Translator()

while True:
     
     a = pyautogui.screenshot(region=(336,921,610,70))
     text = pytesseract.image_to_string(a)
     text = re.sub(r"\d.*","",text)
 
     if re.search(r">yutub (.*)",text):
        parsed = re.search(r">yutub (.*)",text).group(1)
        query = 'https://www.youtube.com/results?search_query={}'.format(parsed)
        req = requests.get(query).text
 
        try:
            link=re.findall(r'yt-lockup-content"><h3 class="[^\"]+\"><a href=\"([^\"]+)\"',req)
            link_="https://www.youtube.com"+str(link[0])
            print(link_)
            pyautogui.moveTo(439,1014)
            pyautogui.click()
            printed = '{}'.format(link_)
            pyautogui.typewrite("tunggu sebentar...")
            pyautogui.hotkey("enter")
            pyautogui.moveTo(439,1014)
            pyautogui.click()
            pyautogui.typewrite(printed)
            time.sleep(5)
            pyautogui.hotkey("enter")
        except Exception as e:
            print(e)
        
     if re.search(r">translate (\w+) (\w+) (.+)",text):
        parsed = re.search(r">translate (\w+) (\w+) (.+)",text)
        src = parsed.group(1)
        dest = parsed.group(2)
        tl = parsed.group(3)
        if re.search(r"ja", dest):
            try:
                payload = trans.translate(tl, dest=dest).extra_data['translation'][1][2].encode('utf-8')
                pyautogui.moveTo(439,1014)
                pyautogui.click()
                printed = 'Halo, hasil terjemahan kamu adalah : {}'.format(payload)
                pyautogui.typewrite(printed)
                pyautogui.hotkey("enter")
                
            except Exception as e:
                print(e)
                pyautogui.moveTo(439,1014)
                pyautogui.click()
                printed = "Terjadi kesalahan... coba cek exception yang terekam dalam log..."
                pyautogui.typewrite(printed)
                pyautogui.hotkey("enter")
        else:
            try:
                payload = trans.translate(tl, dest=dest).text
                pyautogui.moveTo(439,1014)
                pyautogui.click()
                printed = 'Halo, hasil terjemahan kamu adalah : {}'.format(payload)
                pyautogui.typewrite(printed)
                pyautogui.hotkey("enter")
            except Exception as e:
                pyautogui.moveTo(439,1014)
                pyautogui.click()
                printed = "Terjadi kesalahan... coba cek exception yang terekam dalam log..."
                pyautogui.typewrite(printed)
                pyautogui.hotkey("enter")
     time.sleep(0.5)
