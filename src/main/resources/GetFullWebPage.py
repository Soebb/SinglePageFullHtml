#!/usr/bin/python

import getopt
import os
import pyautogui
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def OpenPageThenSave(page_url, save_to_file):
    cap = DesiredCapabilities().CHROME
    cap["marionette"] = True
    option = Options()
    option.binary_location = "/opt/google/chrome/chrome"    #chrome binary location specified here
    option.add_argument("--no-sandbox") #bypass OS security model
    option.add_argument("--headless")

    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), capabilities=cap, options=option)

    browser.set_page_load_timeout(30)  # seconds

    try:
        browser.get(page_url)
    except:
        print("timeout loading page: ", page_url)

    # To simulate a Save As dialog.
    pyautogui.hotkey('ctrl', 's')

    # Wait for the Save As dialog to load. Might need to increase the wait time on slower machines
    time.sleep(2)

    # File path + name
    # FILE_NAME = 'C:\\path\\to\\file\\file.ext'
    # Type the file path and name is Save AS dialog
    pyautogui.typewrite(save_to_file)

    time.sleep(3)

    # Hit Enter to save
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')

    time.sleep(5)

    browser.quit()


def main(argv):
    page_url = ''
    out_dir = ''
    out_file = ''
    try:
        opts, args = getopt.getopt(argv, "hu:o:f:", ["url=", "dir=", "file="])
    except getopt.GetoptError:
        print('python GetFullWebPage.py -u <page_url> -o <output_dir> -f <output_filename>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('GetFullWebPage.py -u <page_url> -o <output_dir> -f <output_filename>')
            sys.exit()
        elif opt in ("-u", "--url"):
            page_url = arg
        elif opt in ("-o", "--dir"):
            out_dir = arg
        elif opt in ("-f", "--file"):
            out_file = arg

    print('page_url = ', page_url)
    print('out_dir  = ', out_dir)
    print('out_file = ', out_file)

    OpenPageThenSave(page_url, out_dir + os.path.sep + out_file)


if __name__ == "__main__":
    # print('Number of arguments:', len(sys.argv), 'arguments.')
    # print('Argument List:', str(sys.argv))

    opt_list = list(sys.argv)
    if len(opt_list) == 1:
        opt_list.append('-h')

    # print('opt_list = ', opt_list)

    main(opt_list[1:])
