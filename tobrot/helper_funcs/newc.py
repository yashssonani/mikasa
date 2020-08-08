from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException
from selenium.webdriver import ActionChains
import time
import os
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


resolution = {
    "0": "same",
    "1": "hd1080p",
    "2": "480p",
    "3": "hd720p",
    "4": "360p"}
for i in range(0, 5):
    print(resolution[str(i)])

def convert_file(file_path,reso,size,audio):
    #driver = webdriver.Chrome()
    driver.get('https://convert-video-online.com/')
    driver.find_element_by_xpath('//*[@id="upload_button"]/input').send_keys(file_path)

    return convert(driver,reso,size,audio)

def convert_link(link,reso,size,audio):

    #driver = webdriver.Chrome()
    driver.get('https://convert-video-online.com/')

    time.sleep(2)

    # To send link

    driver.find_element_by_id('open_link').click()
    time.sleep(1)


    while True:
        try:
            alert = driver.switch_to.alert
            break
        except NoAlertPresentException or UnexpectedAlertPresentException:
            time.sleep(1)
        driver.find_element_by_id('open_link').click()

    time.sleep(2)
    # link = 'https://uploadbot.gq/dl/712808666/_Cleo_One_Punch_Man_2nd_Season_01_Dual_Audio_10bit_1080p_x265_.mkv'
    alert.send_keys(link)
    alert.accept()

    # Set resolution
    # reso = 'hd1080p'
    return convert(driver, reso, size, audio)

def convert(driver,reso,size,audio):
    while True:
        try:
            file_details = driver.find_element_by_class_name('file_details').text
            break
        except:
            time.sleep(2)

    print('link loaded')
    print(file_details)
    time.sleep(1)

    # open settings
    driver.find_element_by_class_name('button_2_inner_2').click()
    time.sleep(2)

    # set slider
    min_size = driver.find_element_by_class_name('minValueLegend').text
    max_sise = driver.find_element_by_class_name('maxValueLegend').text

    print(min_size, max_sise)

    min_int = float(min_size.split(' ')[0])
    max_int = float(max_sise.split(' ')[0])
    print(min_int,max_int)
    # approxsize = int(input('Reduce size in : '))
    approxsize = size

    if approxsize < min_int:
        slider_val = 0
    elif approxsize >= max_int:
        slider_val = 300
    else:
        slider_val = int((approxsize - min_int) * 300 / (max_int - min_int))


    slider = driver.find_element_by_id('slider_button')
    driver.execute_script("arguments[0].setAttribute('style',arguments[1])", slider, 'left: '+str(slider_val) + 'px')
    print(str(slider_val) + 'px')
    # set resolution

    # set resolution
    driver.find_element_by_id('preset_dropdown').click()
    driver.find_element_by_id(reso).click()

    if audio:
        driver.find_element_by_id('no_audio').click()
        time.sleep(5)

    driver.find_element_by_id('converter').click()

    while True:
        try:
            print(driver.find_element_by_class_name('button_4 button_4_active').text)
        except NoSuchElementException:
            break


    a = driver.find_element_by_xpath('//*[@id="download_file_link"]')
    print('Converting', end='')
    while a.get_attribute('href') == 'https://convert-video-online.com/#':
        print('.',end='')
        time.sleep(5)

    download_link = a.get_attribute("href")
    print(download_link)

    driver.quit()
    return download_link

#convert_link('https://de4.seedr.cc/ff_get/720211987/Prison.Break.S05E01.720p.HDTV.2CH.x265.HEVC.mkv?st=k8i4n_3Sisf9GXFD9ytmPg&e=1596946787','same',600,True)
