from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
url = "https://www.jiosaavn.com/artist/s.-p.-balasubrahmanyam-songs/lx5AC5h7LSg_"
driver.get(url)
time.sleep (5)
Language_item = driver.find_elements(By CSS_SELECTOR, "ul.o-list-select > li.o-list-select_item")
for item in Language_item:
    if "selected" not in item.get_attribute("class"):
     
     item.click
     

# try:
#     language_dropdown = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CLASS_NAME, 'language-selector-class'))
#     )
#     language_dropdown.click()
#     select_all_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Select All')]"))
#     )
#     select_all_button.click()
# except Exception as e:
#     print("Error selecting languages:", e)

# while True:
#     try:
#         load_more_button = WebDriverWait(driver, 5).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Load more')]"))
#         )
#         load_more_button.click()
#         time.sleep(2)
#     except:
#         break

# song_links = driver.find_elements(By.CSS_SELECTOR, "a.song-link-class")
# song_urls = [link.get_attribute("href") for link in song_links]

# aditya_music_count = 0

# for song_url in song_urls:
#     driver.get(song_url)
#     time.sleep(2)
    
#     try:
#         copyright_info = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "div.copyright-info-class"))
#         ).text
#         if "Aditya Music" in copyright_info:
#             aditya_music_count += 1
#     except:
#         print(f"Copyright information not found for song: {song_url}")

# print(f"Total songs under 'Aditya Music': {aditya_music_count}")

# driver.quit()