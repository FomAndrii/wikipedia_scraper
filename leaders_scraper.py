import requests
import json
import re
from bs4 import BeautifulSoup

def get_first_paragraph(url, session):
    print(url)  # Keep this for logging purposes
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')

    first_paragraph = ""
    for p in paragraphs:
        text = p.get_text()
        if text.strip():
            first_paragraph = re.sub(r'\[.*?\]|\(.*?\)|\s+', ' ', text)
            break

    return first_paragraph

def get_leaders():
    root_url = "https://country-leaders.onrender.com"
    cookie_url = f"{root_url}/cookie"
    countries_url = f"{root_url}/countries"
    leaders_url = f"{root_url}/leaders"

    def refresh_cookies():
        return requests.get(cookie_url).cookies

    cookies = refresh_cookies()
    countries = requests.get(countries_url, cookies=cookies).json()
    leaders_per_country = {}

    with requests.Session() as session:
        session.cookies = cookies

        for country in countries:
            try:
                response = session.get(leaders_url, params={"country": country})

                if response.status_code == 401:
                    cookies = refresh_cookies()
                    session.cookies = cookies
                    response = session.get(leaders_url, params={"country": country})

                if isinstance(response.json(), list):
                    leaders = response.json()

                    for leader in leaders:
                        wikipedia_url = leader.get("wikipedia_url")
                        if wikipedia_url:
                            leader["bio"] = get_first_paragraph(wikipedia_url, session)

                    leaders_per_country[country] = leaders

            except (requests.exceptions.RequestException, KeyError, ValueError) as e:
                print(f"An error occurred for {country}: {e}")

    return leaders_per_country

def save(leaders_per_country):
    with open('leaders.json', 'w', encoding='utf-8') as file:
        json.dump(leaders_per_country, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    leaders_per_country = get_leaders()
    save(leaders_per_country)
    print("Scraping completed and data saved to leaders.json")
