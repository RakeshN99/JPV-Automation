from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup



options = Options()
options.add_argument("--start-maximized")  
options.add_argument("--disable-notifications")  # Disable pop-ups/notifications

# Set up WebDriver with ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Open the local HTML file
    driver.get("file:///C:/Users/hp/Downloads/Openreach%20NGWFMT-Ethernet_files/Openreach%20NGWFMT-Ethernet.html")
    
    time.sleep(2)
    
    mat_icon = driver.find_element(By.CLASS_NAME, "mat-icon.material-icons.mat-icon-no-color")
    mat_icon = BeautifulSoup.find_parent(By.CLASS_NAME, "mat-icon.material-icons.mat-icon-no-color")
    
    soup = BeautifulSoup(mat_icon, "html.parser")
    element=soup.find('mat-icon.material-icons.mat-icon-no-color',class_= 'content')
    if element:
        innertext = element.get_text(strip=True) 
        print(innertext)
    else:
        print("element not found")  
    # Check the text inside the <mat-icon> element
    icon_text = mat_icon.get_attribute("innerHTML")
    print("Icon text:", icon_text)

    # Verify if the text is "pause"
    if icon_text == "pause":
        print("The icon text is correctly set to 'pause'.")
    else:
        print("The icon text is not 'pause', it is:", icon_text)

finally:
    # Close the browser
    driver.quit()
