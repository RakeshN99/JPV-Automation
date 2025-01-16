from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///C:/Users/hp/Downloads/Openreach%20NGWFMT-Ethernet_files/Openreach%20NGWFMT-Ethernet.html")

def finding_service_ids():
    service_ids = []
    rows = driver.find_elements(By.CSS_SELECTOR, "div[role='row']")
    for row in rows:
        try:
            if "disableColCss" in row.get_attribute("class"):
                continue  
            # Find the 'status' column within the row
            status_cell = row.find_element(By.CSS_SELECTOR, "div[col-id='status'] mat-icon")
            status_text = status_cell.text.strip()
            # Check if the status is 'pause'
            if status_text.lower() == "pause":
                # Find the 'serviceId' column within the same row
                service_id_cell = row.find_element(By.CSS_SELECTOR, "div[col-id='serviceId'] span[ref='eCellValue']")
                service_id = service_id_cell.text.strip()
                service_ids.append(service_id)
        except Exception as e:
            continue
    return service_ids

if __name__ == "__main__":
    service_ids = finding_service_ids()
    print("Service IDs with 'pause' status:", service_ids)  # Print the list of service IDs
    driver.quit()  # Close the browser
