from bs4 import BeautifulSoup
import requests
import re


url = "https://www.billboard.com/charts/billboard-global-200/"

# Get html site for Billboards Global 200
html_content = requests.get(url).text

# Parse HTML
soup = BeautifulSoup(html_content, "lxml")

# Get the 200 rows with this week's songs
mydivs = soup.find_all("ul", class_= "o-chart-results-list-row")

# Process the text in each row to retrieve individual attributes
for song in mydivs:
    text = song.text            
    spl = text.split("\n")      
    # Remove all whitespace, additionally, some extra text is added when a song is new to the Chart or re-enters it. 
    # Consider adding this data into the DB later
    processed = [re.sub(r"\t","",x) for x in spl if re.sub(r"[\W]*(RE-)*(ENTRY)*(NEW)*","",x) != ''][:3]      
    print(processed)
    position, title, author = processed
    print(position)





