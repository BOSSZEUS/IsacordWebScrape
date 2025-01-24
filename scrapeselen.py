from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def get_isacord_colors_selenium(color_numbers):
    driver = webdriver.Chrome()  # Use the appropriate driver for your browser
    driver.get("https://isacordthread.com/search.php")
    results = {}

    for color_number in color_numbers:
        print(f"Searching for color number: {color_number}")
        try:
            # Enter the color number
            search_box = driver.find_element(By.CSS_SELECTOR, "#keyword-search")
            search_box.clear()
            search_box.send_keys(color_number)
            search_box.send_keys(Keys.RETURN)
            time.sleep(2)  # Wait for the page to load

            # Extract the color name
            color_name_element = driver.find_element(By.CSS_SELECTOR, "span.itemname")
            color_name = color_name_element.text.strip()
            results[color_number] = color_name
        except Exception as e:
            results[color_number] = f"Error: {e}"

    driver.quit()
    return results

# Example usage
color_numbers = ["4423", "4442", "4442", "4452", "4515", "4531", "4625", "4644", 
    "4776", "5010", "5020", "5050", "5101", "5115", "5210", "5210", 
    "5230", "5233", "5335", "5400", "5411", "5450", "5500", "5510", 
    "5513", "5515", "5531", "5542", "5565", "5610", "5613", "5643", 
    "5650", "5743", "5822", "5830", "5832", "6011", "6031", "6051", "6151"]
results = get_isacord_colors_selenium(color_numbers)
print(results)
