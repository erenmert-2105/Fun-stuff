from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os
from pathlib import Path
import pathlib
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#%%

#Sadece iterest,my_lang ve my_type ı değiştirin

# my_lang :"TURKISH","ENGLISH","DUTCH","RUSSIAN","CHINESESIMPLIFIED","JAPANESE","CHINESEtRADITIONAL"
# interest : your user name
# my_type : "Text Plain (txt)", "Micrasoft Word (docx)" , "Microsoft Excel (xlsx)"


interest="C:/Users/meren/"     
# what is text lang           
my_lang="TURKISH"
# which type of output you want
my_type="Microsoft Excel (xlsx)"



#%%

def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)


def img_to_text(interest,my_type,my_lang):



    
    
    img=interest+"Desktop/img.jpg"
    img2=interest+"Desktop/img.png"
    dowload_loc=interest+"Downloads"
    dowload_loc2=interest+"Desktop"
    
    """
    opt=Options()
    opt.add_argument("--window-size=1920,1080");
    opt.add_argument("--start-maximized");
    opt.add_argument("--headless")
    """
    #☻driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=opt)
    driver = webdriver.Chrome()
     
     
    # get geeksforgeeks.org
    driver.get("https://www.onlineocr.net")
     
    # get element
    element = driver.find_element(By.XPATH,("//*[@id='fileupload']"))
    
    try:
        element.send_keys(img)
    except:
        element.send_keys(img2)
    
    #%%
    
    elementlang=driver.find_element(By.XPATH,
                                    ("/html/body/form/div[6]/div/div/div/div[1]/div[3]/div[2]/div/div/div[1]/table/tbody/tr[2]/td/select[1]"))
    lang=Select(elementlang)
    lang.select_by_visible_text(my_lang)
    
    
    elemnttypee=driver.find_element(By.XPATH,
                                    ("/html/body/form/div[6]/div/div/div/div[1]/div[3]/div[2]/div/div/div[1]/table/tbody/tr[2]/td/select[2]"))
    typee=Select(elemnttypee)
    typee.select_by_visible_text(my_type)
    
    #%%
    
    convert_button = driver.find_element(By.XPATH,
        "/html/body/form/div[6]/div/div/div/div[1]/div[3]/div[2]/div/div/div[2]/input")
    convert_button.click()
    
    #%%
    x=0
    while x==0:
        try:
            driver.find_element(By.ID,"MainContent_lnkBtnDownloadOutput").click()
            time.sleep(2)
            x=1
            print("True")
        except:
            print("False")
            time.sleep(1)
            x=0
            
    driver.close()
    
    
    my_file=newest(dowload_loc)
    
    Path(my_file).rename("my_file.xlsx")


img_to_text(interest,my_type,my_lang)







