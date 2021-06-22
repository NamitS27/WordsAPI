from selenium import webdriver
import time
import json

def get_meaning(searchterm):
    """ 
    Fetches the meaning of the word specified
    
    :param searchterm: the word for which you want to fetch the meaning
    :return: json object of the meaning 
    """

    # finds the input field by id in the webpage
    sbox = driver.find_element_by_id('word')
    sbox.clear() # clears the input field
    sbox.send_keys(searchterm) # enters the word specified in the input field

    # find the 'CALL THE API' button 
    submit = driver.find_element_by_id("getWord")
    submit.click() # invoking the click event on the button

    # waiting for the results to come
    time.sleep(1)

    # find the code tag in the webpage where the meaning of the word (result) is present
    code = driver.find_element_by_tag_name("code")

    # condition if the meaning is not found
    if code.text == "No results for that word.":
        return {
            'word':searchterm
        }

    # converting the meaning of the word from string to json
    meaning = json.loads(code.text)

    # returning the meaning of word in json formart
    return meaning

if __name__=="__main__":
    # URL for the Words API webpage containing a free (try it) option where one can search meaning of the provided word
    webpage = r"https://www.wordsapi.com/"

    '''
    Specifying the particular version of chrome driver for the particular version of the chrome installed in your system
    You can download chrome from here > https://www.google.com/chrome/
    You can download the specific chrome driver wrt to the versin of the chrome from here > https://chromedriver.chromium.org/downloads
    '''
    options = webdriver.ChromeOptions()
    chrome_driver_binary = "chromedriver.exe" # change the path of the chrome driver (ignore if in the same folder)
    driver = webdriver.Chrome(chrome_driver_binary)

    # opening the url in chrome
    driver.get(webpage)

    # Example
    word = "example" # changes this as per the requirements
    print(get_meaning(word))