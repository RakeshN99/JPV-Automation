from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
import time
url="https://www.w3schools.com/"

def simple():
    options=Options()
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("start-maximized")
    
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)    
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#navbtn_exercises").click()
        time.sleep(4)
        
    except Exception as e:
        print(e)
    finally:
        driver.quit()
        
if __name__ == "__main__":
    simple()
