#webscraping imports
import configparser
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller

#email imports
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logging.basicConfig(filename='script.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def configure_driver():
    config = configparser.ConfigParser()
    config_file_path = 'config.ini'
    
    try:
        config.read(config_file_path)

        chromium_path = config.get('Paths','chromium_path')

        #options
        chromedriver_autoinstaller.install()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.binary_location = chromium_path

        #defining location of driver
        driver = webdriver.Chrome(options=options)

        return driver
    except (configparser.NoSectionError, configparser.NoOptionError, FileNotFoundError):
        print("Error reading config.ini or chromium_path not found.")
        print("Please configure chromium in terminal using the command: ski-chromium-config")
        return None 

def scrape_data(driver):
    url = 'https://www.skiutah.com/snowreport'

    driver.get(url)

    try:
        resort_names = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div/div/div[2]/div/div[*]/div/div[1]/div[2]/h2/a")
        resort_open = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div/div/div[2]/div/div[*]/div/div[2]/div[1]/div/strong[1]")
        resort_base = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div/div/div[2]/div/div[*]/div/div[2]/div[2]/div/div[1]/div[3]/div/span[1]")
        snow24 = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div/div/div[2]/div/div[*]/div/div[2]/div[2]/div/div[1]/div[1]/div/span[1]")
        snow48 = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div/div/div[2]/div/div[*]/div/div[2]/div[2]/div/div[1]/div[2]/div/span[1]")

        # Create a dictionary to store the data
        resort_data = {}

        # Loop through the elements and store in the dictionary
        for resort, open, base, snow_day, snow_day_two in zip(resort_names, resort_open, resort_base, snow24, snow48):
            resort_name = resort.get_attribute("innerText")
            open_date = open.get_attribute("innerText")
            resort_base_info = base.get_attribute("innerText") + " in."
            resort_24hr_snow = snow_day.get_attribute("innerText") + " in."
            resort_48hr_snow = snow_day_two.get_attribute("innerText") + " in."
            
            resort_data[resort_name] = {
                "Opening": open_date,
                "Base depth": resort_base_info,
                "24 hr. snow": resort_24hr_snow,
                "48 hr. snow": resort_48hr_snow
            }
    except ElementNotFound as e:
        logging.error(f"An error occurred during web scraping: {str(e)}")
    
    finally:
        driver.close()

    return resort_data

def configure_email(resort_data, target_resorts):
    # Email config

    config = configparser.ConfigParser()
    config.read('config.ini')

    sender_email = config.get('Email', 'sender_email') 
    sender_password = config.get('Email', 'sender_password') #"vvsf frsu teyn tddi"
    recipient_email = config.get('Email', 'recipient_email') 

    subject = "Ski Resort Data"
    message = ""

    try:

        # update email message
        for resort_name, data in resort_data.items():
            if resort_name in target_resorts:
                message += f"{resort_name}\n"
                for key, value in data.items():
                    message += f"{key}: {value}\n"
                message += "\n"

        #create email
        email = MIMEMultipart()
        email['From'] = sender_email
        email['To'] = recipient_email  #", ".join(recipient_emails)
        email['Subject'] = subject
        email.attach(MIMEText(message, 'plain'))

        # Send the email using Gmail's SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, email.as_string())

        #logging.info("Email sent successfully.")
        print("Email sent successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")

def main():

    target_resorts=[
        "Beaver",
        "Cherry Peak",
        "Park City Mountain",
        "Snowbasin Resort",
        "Sundance Mountain Resort"
    ]

    driver = configure_driver()
    resort_data = scrape_data(driver)    
    configure_email(resort_data, target_resorts)

if __name__ == "__main__":
    main()