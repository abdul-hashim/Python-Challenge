#!/usr/bin/env python
# coding: utf-8

# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import pymongo

def scrape():

    # Open Browser


    executable_path = {'executable_path': 'C:/Users/Aboody/Chromedriver/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    # Latest news of Mars

    # Visit URL
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Find the title names
    all_results = soup.find('li', class_='slide')
    # Loop through captured data                     
    for result in all_results:
        news_title = result.find('h3').text
        news_p = result.find('div', class_='rollover_description_inner').text
        print(f"{news_title}")
        print("")
        print(f"{news_p}")


    # Featured Image of Mars

    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    # Iterate through all pages
    for x in range(1):
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all elements that contain needed information
        results = soup.find('footer')
        imgAddress = results.find('a', class_="button fancybox")['data-fancybox-href']
        featured_image_url = "https://www.jpl.nasa.gov" + imgAddress
        try:
            browser.click_link_by_partial_text('more_button')
            
        except:
            print("Scraping Complete")


    # Gather Weather From Twitter

    # Visit URL
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    # Parse HTML with Beautiful Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain needed information
    mars_weather = soup.find('div', class_="js-tweet-text-container").text.strip()


    #Mars Facts

    # Visit URL and convert data into a table
    url = 'https://space-facts.com/mars/'
    table = pd.read_html(url)
    # Convert data from web into a DF
    df = table[0]
    # Fix DF Headers
    df.columns= ["Features", "Value"]
    # Convert DF to HTML
    html_df = df.to_html()


    # Get Dictionary of Images and Titles

    # Visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    # Parse HTML with Beautiful Soup
    html = browser.htm
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain Mars information
    items = soup.find_all('div', class_="item")
    items_list= []
    items_dict= dict()
    for item in items:
        img = "https://astrogeology.usgs.gov/" + item.find('img', class_='thumb')['src']
        title = item.find('img', class_='thumb')['alt']
        items_list.append({'title':title,'img_url':img})


    Main_Dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "fact_table": html_df,
        "hemisphere_images": items_list
    }

    return Main_Dict