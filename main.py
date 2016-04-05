import time
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool
import json

reload(sys)
sys.setdefaultencoding('utf8')


stat_free=0
stat_using=1
p_num = 2
pool = ThreadPool(p_num)
M_browser = {}
l_name=[]

try:
    with open("test.json") as json_file:
        M_name = json.load(json_file)
except:
    M_name = {}



for i in range(p_num):
    browser = webdriver.Chrome()
    browser.get('http://www.google.com')
    M_browser[i] = {"browser" : browser, "using" : stat_free}


with open("University.txt", "r") as f_input:
    for line in f_input:
        line = line.strip()
        f = line.split("\t")
        name = f[1]
        l_name.append(name)
        if name not in M_name:
            M_name[name] = {"lock" : 0, "address" : None}


def checkName(idx):
    name = l_name[idx]
    out = "NA"
    browser = None
    browserIdx = stat_free


    address_text = M_name[name]["address"]
    if (address_text is None) or (address_text == "NA"):
        while 1:
            for Idx in range(p_num):
                if M_browser[Idx]['using'] == stat_free:
                    M_browser[Idx]['using'] = stat_using
                    browser = M_browser[Idx]['browser']
                    browserIdx = Idx
                    break
            if browser is not None:
                break

        try:
            search = browser.find_element_by_name('q')
            browser.get_screenshot_as_file('images/%d/%s.0.png' % (browserIdx, name))
            search.clear()
            browser.get_screenshot_as_file('images/%d/%s.1.png' % (browserIdx, name))
            search.send_keys(name)
            browser.get_screenshot_as_file('images/%d/%s.2.png' % (browserIdx, name))
            search.send_keys(Keys.RETURN) # hit return after you enter search text
            # sleep for 3 seconds so you can see the results
            browser.get_screenshot_as_file('images/%d/%s.3.png' % (browserIdx, name))
            time.sleep(1)
            browser.get_screenshot_as_file('images/%d/%s.4.png' % (browserIdx, name))
            time.sleep(1)
            browser.get_screenshot_as_file('images/%d/%s.5.png' % (browserIdx, name))
            time.sleep(1)
            browser.get_screenshot_as_file('images/%d/%s.6.png' % (browserIdx, name))
            try:
                l_1 = browser.find_element_by_class_name('_Xbe')
                out = l_1.text
            except:
                pass
        except:
            pass
        print("%d\t%d\t%s\t%s" % (idx, browserIdx, name, out))
        while 1:
            if M_name[name]["lock"] == 0:
                break

        M_name[name]["lock"] = 1
        M_name[name]["address"] = out
        M_name[name]["lock"] = 0

        M_browser[browserIdx]['using'] = stat_free
        browser.get_screenshot_as_file('images/%d/%s.7.png' % (browserIdx, name))

    return out


result = pool.map(checkName, range(len(l_name)))
pool.close()
pool.join()

with open('test.json', "w") as outfile:
    json.dump(M_name, outfile)

for browserIdx in range(p_num):
    browser = M_browser[browserIdx]['browser']
    browser.quit()
