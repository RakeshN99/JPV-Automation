import os
import time
import imaplib
import email
from email.header import decode_header
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv

load_dotenv()

def enter_otp_on_website(url, delay):
    time.sleep(delay)  # Add delay before opening the website
    options = Options()
    #options.headless = False
    options.add_argument ('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    # options.add_argument('--disable-extensions')
    # options.add_argument('--disable-blink-features=AutomationControlled')
    
    #driver = webdriver.Chrome(options=options)
    #options.add_argument('--headless=new')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)
        time.sleep(2)

        email_input = driver.find_element(By.CSS_SELECTOR, "#email")
        email_input.clear()
        email_input.send_keys(EMAIL)

        verify_button = driver.find_element(By.CSS_SELECTOR, "#button")
        verify_button.click()
        time.sleep(5)  # Adjust this if page loads faster

        otp = get_otp_from_email()
        if otp:
            otp_input = driver.find_element(By.CLASS_NAME, "frm-control")
            otp_input.clear()
            otp_input.send_keys(otp)

            submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-black")
            submit_button.click()
            time.sleep(3)
            
            remove_button = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/button")
            remove_button.click()
            time.sleep(3)

            upload_resume = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div[1]/div/div/div/div[1]/input")

            file_path = "C:/Users/THARUN_H/OneDrive/Desktop/EXCEL2WORD/Spira code@tmp/triec-monitoring-crm/resumes/Venera Suleyman, Resume.doc"
            upload_resume.send_keys(file_path)


            resume_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-orange")
            resume_button.click()
            time.sleep(30)
            
            next_button = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[2]/form/div[2]/div/div/div/button[3]")
            next_button.click()
            time.sleep(3)
            print(f"Resume upload successful for URL: {url}")
        else:
            print(f"Failed to fetch OTP for URL: {url}")
            send_failure_email()

    except Exception as e:
        print(f"Error processing URL {url}: {e}")
    finally:
        driver.quit()



if _name_ == "_main_":
    urls = [os.getenv("CRM_URL")]
    with ThreadPoolExecutor(max_workers=len(urls)) as executor:
        # Add incremental delay for each URL
        delays = [i * 30 for i in range(len(urls))]  # 30 seconds apart
        executor.map(enter_otp_on_website, urls, delays)