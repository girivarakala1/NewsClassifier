from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the BBC News website
driver.get("https://www.bbc.com/news")

# Wait for the page to load, adjust the timeout if needed
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "gel-long-primer")))

# Example: Extract headlines from the page
headlines = driver.find_elements(By.CLASS_NAME, "gs-c-promo-heading__title")

# Print the headlines
for headline in headlines:
    print(headline.text.strip())

# Close the browser window when done
driver.quit()
