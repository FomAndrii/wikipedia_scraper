# **My first scraper project**
## **Titels**
*Intro*  
***WARNING!!! Info for Coaches: my mistakes, obsticales***  
*VENV*  
*Codes, queries, promts*  
*Saving and testing results*  

## ***Intro***
In this project, I was guided step by step through the process of:
- creating a self-contained development environment
- retrieving some information from an API (a website for computers)
- leveraging it to scrape a website that does not provide an API
- saving the output for later processing

In this poject I query an API for a list of countries and their past leaders.
Then I extract and clean their short bio from Wikipedia.
As final step, I save the data to disk.

I studied more deeper topics such as **scraping**, **data structures**, **regular expressions**, **concurrency** and **file handling**.

## ***Info for Coaches: my mistakes, obsticales***
I could not resolve:
- How to clean the first paragraph from double spaces and other special simbols.
- How to scraper the first paragraph in French
- Some of my peaces of codes are bigger then should be
- I had some obsticales with the launching **python3 leaders_scraper.py**. I queried **python leaders_scraper.py**

## ***VENV***
Creating a clean environment
I used the venv command to create a new environment called wikipedia_scraper_env.
I activate it by .\venv\Scripts\activate

## *Codes, queries, promts*
I used the requests external library through the **import** keyword.  
I used the **get()** method to connect to this endpoint: https://country-leaders.onrender.com/status.  
I dealed with JSON and Cookies.  
I got the actual data from the API.  
I queried the **/leaders** endpoint.  
I created a **get_leaders()** function without/with parameter.  
I used the **beautiful soup 4** external library.  
I loaded the output of my **get_text()** function.  
I used the **prettify()** function.  
I used regular expressions as **regex**  
After this I put it all together  
  # I did it not alone, but with my friend ChatGPT. Yes, I am guilty. Sorry, please  

## ***Saving and testing results***
I saved everything in **leaders_scraper.py** file and launched with **python leaders_scraper.py**.
After several manipulations with Python and libraries on my PC I received NOT ideal, but result.
