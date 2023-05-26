from bs4 import BeautifulSoup
import requests
import re
from datetime import date
import csv

def process_new(pre_processed):
    pre_processed.insert(3,0)
    pre_processed.append(None)

# Attributes to extract
attributes = ["position", "title", "authors", "last week position", "peak position", "weeks on chart", "chart_date"]

url = "https://www.billboard.com/charts/billboard-global-200/"

# Get html site for Billboards Global 200
html_content = requests.get(url).text

# Parse HTML
soup = BeautifulSoup(html_content, "lxml")

# Get the 200 rows with this week's songs
mydivs = soup.find_all("ul", class_= "o-chart-results-list-row")

# All scraped songs will be stored here
all_songs = []

# Get date the content was scraped in
B200_date = date.today()

# Process the text in each row to retrieve individual attributes
for song in mydivs:
    text = song.text            
    spl = text.split("\n")      
    # Remove all whitespace, additionally, some extra text is added when a song is new to the Chart or re-enters it. 
    # Consider adding this data into the DB later
    processed = [re.sub(r"\t","",x) for x in spl if re.sub(r"[\W]*(RE-)*(ENTRY)*(NEW)*","",x) != '']  

    # New songs do not have a "Last Week Position attribute"
    if len(processed) != 9:
        process_new(processed)

    # Put them in a Key-Value format, potentially used in the future as a JSON object
    packaged = {attrib:value for attrib, value in zip(attributes, processed[:-3])}
    packaged['chart_date'] = B200_date

    all_songs.append(packaged)
    

# Write the results of scraping into a csv with the name of the week it was updated
filename = f'../B200_Weekly/{B200_date}.csv'
    

with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,attributes)
    w.writeheader()
    for song in all_songs:
        w.writerow(song)