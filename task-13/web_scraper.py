"""
Web Scraper using BeautifulSoup
Task 13: Python Developer Internship
"""

import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_quotes():
    """
    Scrapes quotes from quotes.toscrape.com (a scraping practice website)
    Extracts: Quote text, Author, and Tags
    """
    
    url = "http://quotes.toscrape.com/"
    
    try:
        # Fetch HTML content
        print("Fetching data from website...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes
        
        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all quote containers
        quotes = soup.find_all('div', class_='quote')
        
        # List to store scraped data
        data = []
        
        # Extract data from each quote
        for quote in quotes:
            try:
                # Extract text (handle missing tags safely)
                text = quote.find('span', class_='text')
                text = text.get_text() if text else "N/A"
                
                # Extract author
                author = quote.find('small', class_='author')
                author = author.get_text() if author else "N/A"
                
                # Extract tags
                tags = quote.find_all('a', class_='tag')
                tags_list = [tag.get_text() for tag in tags] if tags else []
                tags_str = ', '.join(tags_list)
                
                # Append to data list
                data.append({
                    'quote': text,
                    'author': author,
                    'tags': tags_str
                })
                
            except Exception as e:
                print(f"Error processing a quote: {e}")
                continue
        
        # Save to CSV
        save_to_csv(data)
        
        print(f"\n✅ Successfully scraped {len(data)} quotes!")
        print("📁 Data saved to 'scraped_data.csv'")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching the website: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


def save_to_csv(data):
    """
    Save scraped data to CSV file
    """
    if not data:
        print("⚠️ No data to save!")
        return
    
    try:
        with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
            # Define CSV headers
            fieldnames = ['quote', 'author', 'tags']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # Write headers
            writer.writeheader()
            
            # Write data rows
            writer.writerows(data)
            
    except Exception as e:
        print(f"❌ Error saving to CSV: {e}")


def scrape_links_example():
    """
    Alternative example: Scraping links from a webpage
    """
    url = "http://quotes.toscrape.com/"
    
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract all links
        links = soup.find_all('a')
        
        print("\n🔗 Sample Links Found:")
        for i, link in enumerate(links[:5], 1):  # Show first 5 links
            href = link.get('href', 'N/A')
            text = link.get_text(strip=True) or 'No text'
            print(f"{i}. {text} -> {href}")
            
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    print("=" * 50)
    print("🌐 WEB SCRAPER - TASK 13")
    print("=" * 50)
    
    # Main scraping function
    scrape_quotes()
    
    # Optional: Uncomment to see links example
    # scrape_links_example()
    
    print("\n" + "=" * 50)
    print("✨ Scraping Complete!")
    print("=" * 50)
