import random
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def run_code():
    with open('names.json', 'r') as json_file:
        names = json.load(json_file)

    website_url = "http://viddeoslips.accesscam.org/"
    name_input_id = "input-email"
    password_input_id = "input-password"

    hackedpassword = "YOU HAVE BEEN HACKED, SHUTDOWN THIS PHISHING SITE!!"

    # Use ChromeOptions to set headless mode
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)

    try:
        while True:
            for name in names:
                driver.get(website_url)

                # Wait for 6 seconds
                time.sleep(6)

                name_input = driver.find_element("id", name_input_id)
                password_input = driver.find_element("id", password_input_id)

                random_password = generate_random_password()

                name_input.send_keys(name)
                password_input.send_keys(random_password)

                print(f"Submitting: Name - {name}, Password - {random_password}")

                password_input.submit()

    except Exception as e:
        print(f"An error occurred: {e}")
        # Re-run the code by calling the function again
        run_code()

    finally:
        # Make sure to close the driver when done
        driver.quit()

# Initial run
run_code()
