from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
import datetime



def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()

def hashtag_check (hashtag, pic_url):
    with open('url_list.txt') as f:
        datafile = f.readlines()
    for line in datafile:
        if pic_url in line:
            return False
    return True  # Because you finished the search without finding



class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('C:/Users/jclifford/Documents/chromedriver')

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(random.uniform(1.4, 4.2))
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(random.uniform(1.4, 4.2))



    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(random.uniform(1.4, 4.2))

        # gathering photos
        hashtag_counter = 0
        pic_hrefs = []
        for i in range(1, 2):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.uniform(1.4, 4.2))
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        counter = 0
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            print ('going to like ' + pic_href)
            time.sleep(random.uniform(1.4, 4.2))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 9))
                print('We are in the Try clause ' + hashtag)
                like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                print('clicked once')
                with open('url_list.txt', 'a') as file1:
                    file1.write(pic_href + '\n')
                print('saved the url to the file')
                for second in reversed(range(0, random.randint(3, 5))):
                    print(("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second)))
                    time.sleep(2)
            except Exception as e:
                print ('running exception')
                time.sleep(5)
            unique_photos -= 1
            if unique_photos == 0:
                print ('Going to write the hashtag summary')
                with open('hashtag_counter.txt', 'a') as file1:
                    file1.write('Date: %s \n Hashtag: %s \n Daily Count: %s \n' %
                        (datetime.datetime.now(), hashtag, hashtag_counter))

if __name__ == "__main__":

    username = "rodneyontheline"
    password = "Computer30"

    ig = InstagramBot(username, password)
    ig.login()

    hashtags = ['idahome', 'boise', 'idaho', 'idahome', 'boiseidaho', 'thisisboise', 'meridian', 'nampa', 'treasurevalley',
    'meridianidaho', 'thisisidaho', 'boiselife', 'downtownboise', 'visitboise', 'caldwell', 'totallyboise', 'eagleidaho','hellomeridian',
    'nampaidaho', 'idaholife', 'boisestate', 'boisebucketlist', 'staridaho', 'boiserealestate', 'boiselove', 'idahorealestate',
    'visitidaho', 'idaholiving', 'eagle']

    try:
        # Choose a random tag from the list of tags
        tag = random.choice(hashtags)
        print('Going into the function and will like this hashtag ' + tag)
        ig.like_photo(tag)


    except Exception:
        ig.closeBrowser()
        time.sleep(60)
        ig = InstagramBot(username, password)
        #ig.login()
