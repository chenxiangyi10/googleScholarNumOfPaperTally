import requests
from bs4 import BeautifulSoup
import urllib3
import re
urllib3.disable_warnings()

def get_num_papers(topic, start_year, end_year):
  # Initialize a dictionary to store the results
  results = {}
  
  # Iterate over the years
  for year in range(start_year, end_year+1):
    # Set the URL to search for the topic in the given year
    url = f"https://scholar.google.com/scholar?q={topic}&hl=en&as_sdt=0%2C5&as_ylo={year}&as_yhi={year}"
    
    # Make the request and parse the response
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract the number of results
    result_text = soup.find_all("div", class_="gs_ab_mdw")
    num_results = int(re.sub(r'[^\d]', '',result_text[1].text.split()[1] )) 
    
    # Save the result in the dictionary
    results[year] = num_results
  
  return results

# Example usage
results = get_num_papers('"machine learning"', 2010, 2023)
print(results)
