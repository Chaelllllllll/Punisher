import random
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

with open('names.json', 'r') as json_file:
    names = json.load(json_file)

website_url = input("Enter the website URL: ")
name_input_id = input("Enter the name input ID: ")
password_input_id = input("Enter the password input ID: ")

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

driver = webdriver.Chrome()

while True:
    for name in names:
        driver.get(website_url)

        name_input = driver.find_element("id", name_input_id)
        password_input = driver.find_element("id", password_input_id)

        random_password = generate_random_password()

        name_input.send_keys(name)
        password_input.send_keys(random_password)

        print(f"Submitting: Name - {name}, Password - {random_password}")

        password_input.submit()

driver.quit()
