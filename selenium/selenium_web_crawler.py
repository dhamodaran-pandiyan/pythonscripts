from selenium import webdriver
import time

DRIVER_PATH = "C:\Drivers\chromedriver.exe"
INPUT_FILE_PATH = "D:\python\somefile.txt"
ENGLISH_SUBTITLE = "English subtitle download for "
GOOGLE_URL = "http://www.google.com"
ST_SCRIPT = "window.open('about:blank', " #"window.open('about:blank', 'tab2');"
END_SCRIPT = ");"

driver = webdriver.Chrome(executable_path = DRIVER_PATH)
f= open(INPUT_FILE_PATH,"r")
itr = 1
for movie_name in f:
    tab = "tab"+str(itr)
    if tab =="tab1":
        driver.get(GOOGLE_URL)
        inputElement = driver.find_element_by_name("q")
        inputElement.send_keys(ENGLISH_SUBTITLE + movie_name )
    else:
        print(tab)
        driver.execute_script(ST_SCRIPT + "'" + tab + "'" + END_SCRIPT)
        driver.switch_to.window(tab)
        driver.get(GOOGLE_URL)
        inputElement = driver.find_element_by_name("q")
        inputElement.send_keys(ENGLISH_SUBTITLE + movie_name )
    itr = itr + 1

f.close()