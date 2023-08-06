import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def replace_spaces(string):
    """
    It replaces all spaces in a string with periods
    
    :param string: The string to be modified
    :return: The string with all spaces replaced with periods.
    """
    return string.replace(" ", ".")

def profile_search(search, remote_url='http://54.36.177.119:4450'):
    """
    It takes a search term as an argument, opens a browser, goes to the quora search page, scrapes the
    usernames and urls of the results, and returns a dictionary with the usernames and urls
    
    :param search: The search term you want to search for
    :return: A dictionary of questions and their urls
    """
    try:
        # Opening a browser and going to the twitch search page.
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Remote(command_executor=remote_url, options=chrome_options)
        url = f"https://www.twitch.tv/search?term={search}&type=channels"
        driver.get(url)
        time.sleep(2)
        
        # Finding all the elements with the class name "ScCoreLink-sc-udwpw5-0 jswAtS tw-link" and
        # then getting the text of each element and the href attribute of each element.
        results = driver.find_elements(By.CLASS_NAME, value=replace_spaces("ScCoreLink-sc-udwpw5-0 jswAtS tw-link"))
        usernames = [element.text for element in results if element.text not in ["Top Clip", "Last Stream", '']]
        urls = [element.get_attribute("href") for element in results if  element.text not in ["Top Clip", "Last Stream", '']]
        
        # Getting the images of the profiles.
        images = driver.find_elements(By.CLASS_NAME, value=replace_spaces("InjectLayout-sc-588ddc-0 iDjrEF tw-image tw-image-avatar"))
        images = [image.get_attribute("src") for image in images if "70x70" not in image.get_attribute("src")]
        
        # Creating a dictionary with the usernames, urls, and images of the profiles.
        values = [{"username": username, "url": url, "image": image} for username, url, image  in zip(usernames, urls, images)]   
        keys = [f"profile {str(index + 1)}" for index, _ in enumerate(usernames)]
        profiles_dict = dict(zip(keys, values))
        
        # It closes the browser.
        driver.quit()
        
        # Logging the search on twitch for the search term.
        logging.info(f"Search on twitch for {search} has been done")
        
        return usernames, urls, images, profiles_dict
    
    except Exception as e:
        logging.error(e)
        logging.error(f"Search on twitch for {search} has failed")
        driver.quit()


#print(profile_search("marouane"))
