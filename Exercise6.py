import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# URL of the webpage
url = "https://www.britannica.com/topic/list-of-prime-ministers-of-Great-Britain-and-the-United-Kingdom-1800350"

# Send a GET request to the URL and store the response
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the section containing the list of prime ministers
pm_section = soup.find("section", id="ref1")

# Find all the <li> tags containing the prime ministers' names and links
pm_list_items = pm_section.find_all("li")

# Prepare lists to store the data
first_names = []
last_names = []
birth_dates = []
affiliations = []

# Loop through each prime minister item to extract the name and link
for pm_item in pm_list_items: 
    # Extract the name and URL (link to the detailed page)
    name_tag = pm_item.find("a")
    name = name_tag.text.strip() if name_tag else ""
    link = name_tag['href'] if name_tag else ""
    
    # Split the name into first and last names
    name_parts = name.split()
    first_name = " ".join(name_parts[:-1]) if len(name_parts) > 1 else ""
    last_name = name_parts[-1] if len(name_parts) > 1 else ""
    
    # Initialize placeholders for birth date and affiliation
    birth_date = ""
    affiliation = ""
    
    # Visit the detailed page for each prime minister
    if link:
        # Send a GET request to the link and store the response 
        pm_response = requests.get(link) 
        pm_soup = BeautifulSoup(pm_response.content, "html.parser") 
        
        # Find the "Quick Facts" section
        facts_section = pm_soup.find("div", class_="facts-list mt-10") 
        if facts_section: 
            # Find all visible and hidden facts
            facts = facts_section.find_all("div", class_="js-fact mb-10 line-clamp clamp-3")
            hidden_facts = facts_section.find_all("div", class_="facts-item-none")
            facts.extend(hidden_facts)
            
            # Extract relevant data from facts
            for fact in facts:
                 # Look for the <dl> inside each fact
                dl = fact.find("dl") 
                if dl:
                    # Extract <dt> for the label
                    label = dl.find("dt").text.strip() if dl.find("dt") else ""  
                    # Extract all <dd> tags
                    value_tags = dl.find_all("dd")  
                
                    # Extract the value(s) for the label "Born"
                    if label.lower() == "born:":
                        raw_birth_info = value_tags[0].text.strip() if value_tags else ""
                        # Remove dots from month abbreviation (e.g., "Oct." -> "Oct")
                        raw_birth_info = raw_birth_info.replace(".", "")
                        # Split date and location
                        birth_parts = raw_birth_info.split(",")
                        
                        if len(birth_parts) >= 2:
                            # Combine the first two parts (e.g., "August 26" and "1676")
                            raw_date = f"{birth_parts[0].strip()} {birth_parts[1].strip()}" 
                            
                            try:
                                # Try parsing with abbreviated month and reformat it as dd.mm.yyyy
                                parsed_date = datetime.strptime(raw_date, "%b %d %Y")
                                birth_date = parsed_date.strftime("%d.%m.%Y")
                            except ValueError:
                                try: 
                                    # Try parsing with full month name and reformat it as dd.mm.yyyy
                                    parsed_date = datetime.strptime(raw_date, "%B %d %Y")
                                    birth_date = parsed_date.strftime("%d.%m.%Y")
                                except ValueError:
                                    # If both formats fail, set the birth date to an empty string
                                    birth_date = ""
                        else:
                            # Set to empty string if the format is unexpected (e.g. only the year is provided)
                            birth_date = ""  
                            
                    # Extract the value(s) for the label "Political Affiliation"
                    if label.lower() == "political affiliation:":
                        # Extract text from all <dd> tags and join them with commas
                        affiliations_list = [tag.text.strip() for tag in value_tags]
                        affiliation = ", ".join(affiliations_list)
                    
    # Append the extracted data to the lists
    first_names.append(first_name)
    last_names.append(last_name)
    birth_dates.append(birth_date)
    affiliations.append(affiliation)

# Create a DataFrame with the collected data
data = pd.DataFrame({
    "First Name": first_names,
    "Last Name": last_names,
    "Date of Birth": birth_dates,
    "Political Affiliation": affiliations
})

# Save the DataFrame to an Excel file (with duplicate rows)
data.to_excel("uk_prime_ministers.xlsx", index=False)

# Save the deduplicated data to an Excel file (without duplicate rows)
deduplicated_data = data.drop_duplicates()
deduplicated_data.to_excel("uk_prime_ministers_deduplicated.xlsx", index=False)

print("Data has been saved to uk_prime_ministers.xlsx and uk_prime_ministers_deduplicated.xlsx")