from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the browser
driver = webdriver.Chrome()

# Open the webpage
driver.get("file:///C:/Users/hp/Downloads/Openreach%20NGWFMT-Ethernet_files/Openreach%20NGWFMT-Ethernet.html")

# Find all rows
rows = driver.find_elements(By.CSS_SELECTOR, "div[role='row']")

# Iterate through rows to find the one with 'status' = 'pause'
for row in rows:
    try:
        # Find the 'status' column within the row
        status_cell = row.find_element(By.CSS_SELECTOR, "div[col-id='status'] mat-icon")
        status_text = status_cell.text.strip()

        # Check if the status is 'pause'
        if status_text.lower() == "pause":
            # Find the 'serviceId' column within the same row
            service_id_cell = row.find_element(By.CSS_SELECTOR, "div[col-id='serviceId'] span[ref='eCellValue']")
            service_id = service_id_cell.text.strip()

            print(f"Status: {status_text}, Service ID: {service_id}")
    except Exception as e:
        # Handle cases where the element isn't found in a row
        continue

# Close the browser
driver.quit()
