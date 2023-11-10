#!/usr/bin/env python

import configparser
import os
from shutil import which
import sys, subprocess

def detect_chromium_path():
    chromium_path = which("chromium-browser")
    if chromium_path is None:
        subprocess.run(["sudo", "apt-get", "update"])
        subprocess.run(["sudo", "apt-get", "install","chromium-browser","-y"])
        chromium_path = which("chromium-browser")
        return chromium_path
    else:
        return chromium_path
    
def config_chromium():
    config = configparser.ConfigParser()
    chromium_path = detect_chromium_path()
    config['Paths'] = {'chromium_path': chromium_path}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    print(f"Chromium path set to: {chromium_path}")

def run_setup_script():
    # Create a new configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Collect user inputs
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password: ")
    recipient_email = input("Enter the recipient's email address: ")

    # Update the configuration file
    config['Email'] = {
        'sender_email': sender_email,
        'sender_password': sender_password,
        'recipient_email': recipient_email
    }

    # Write the updated configuration back to the file
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    run_setup_script()