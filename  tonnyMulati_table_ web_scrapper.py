import requests
from bs4 import BeautifulSoup
import pandas as pd
from gtts import gTTS
from gtts.tokenizer import pre_processors
import pygame

# Make a GET request to the Wikipedia page you want to scrape
url = input('Enter page url.eg: https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States: ')

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(e)
    exit()

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table on the page (in this case, the table of US national parks)
table = soup.find('table', class_='wikitable sortable')

# Use Pandas to read the HTML table into a DataFrame
df = pd.read_html(str(table))[0]

# To say the first few rows of the DataFrame to make sure it worked use
# text = str(df.head())
# Say all the content in all the rows
text = str(df)
tts = gTTS(text, lang='en', slow=False, pre_processor_funcs=[pre_processors.abbreviations, pre_processors.end_of_line]) 
# Save the audio in an mp3 file
filename = 'good.mp3'
tts.save(filename)

# Play the audio
pygame.init()
pygame.mixer.music.load(filename)
pygame.mixer.music.play()

# Wait for the audio to be played
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
