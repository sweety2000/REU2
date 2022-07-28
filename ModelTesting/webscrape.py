from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import io
import requests

    #REPLACE WITH YOUR OWN DIRECTORIES

    #WRITING FUNCTION 

def write_urls(urls, name):
    folder = os.path.join(#MAIN DATA COLLECTION, name)
    folder = os.path.join(folder, 'urls.txt')
    file = open(folder, 'w')
    for item in urls: 
        # %s\n writes each item to a new line
            file.write(item + '\n')
        print('file written')
        file.close()
    #INTIALIZE BROWSER, SCROLL, SAVE URLS 

def int_browser(term, wb):
    #start page
    #find searchbar and type element from data
    wb.get('https://www.google.com/imghp?tbm=isch')
    elem = wb.find_element(By.NAME, 'q')
    elem.send_keys(term + Keys.RETURN)
    
def scroll_to_end(wb):
     #saves document height
    old_max = wb.execute_script("return document.body.scrollHeight")
    while True: 
        #scrolls down to current bottom 
        wb.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #wait for page to load 
        time.sleep(2)
        new_max = wb.execute_script("return document.body.scrollHeight")

        #check to see if reached end of page
        if new_max == old_max:
            print("finished scroll")
            break
        #if not, continue
        old_max = new_max

def img_url_scrape(max_images, search, wb):
    int_browser(search, wb)
    scroll_to_end(wb)
    

    #ensures no duplicates
    url_set = set() 
    #dups = 0
    #index = 0 
    
    #quality control for while loop 
    ##while (len(url_set) + dups) < max_images:
    index = len(url_set) + dups
    placeholders = wb.find_elements(By.CLASS_NAME, "Q4LuWd")
        
    for img in placeholders[index:max_images]:
        try: 
            img.click()

        except:
            continue

        images = wb.find_elements(By.CLASS_NAME, "n3VNCb")
        
        for image in images: 
            current_size = len(url_set)
            if image.get_attribute('src') and 'http' in image.get_attribute('src'): 
                url_set.add(image.get_attribute('src'))
                if current_size == len(url_set):
                    max_images += 1 
                    dups += 1
                    break
    return url_set

#DOWNLOAD IMAGES


def img_download(name):
    direc = os.path.join(#directory, name)
    folder = os.path.join(direc, 'urls.txt')
    i = 0
    with open(folder, "r") as fb: 
        for i in range(100):
            line = fb.readline().rstrip('\n')
            try: 
                url = requests.get(line)
                new_file = os.path.join(direc, name + str(i) + '.png')
                with open(new_file, "wb") as new_f:
                    new_f.write(url.content)
                    new_f.close()
            except: 
                continue



        fb.close()


#intialize webbrowser first
browser = webdriver.Chrome()
CATEGORIES = [#SAMPLE ITEMS]
def main(max_images, list_of_names, wb):
    for name in list_of_names: 
        url_set = img_url_scrape(max_images, name, wb)
        write_urls(url_set, name)
        img_download(name)
    print('------------function has finished------------')
        
main(100, CATEGORIES, browser)
