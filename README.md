# 🌐 Task 13: Web Scraping Using BeautifulSoup

## 📋 Project Overview
This project demonstrates web scraping using Python's BeautifulSoup library to extract data from websites and store it in a structured CSV format. The scraper collects quotes, authors, and tags from a practice website.

## 🛠️ Tools & Technologies Used
- **Python 3.x**
- **BeautifulSoup4** - HTML/XML parsing library
- **requests** - HTTP library for fetching web pages
- **csv** - Built-in module for CSV file handling
- **VS Code** - Development environment

## 📁 Project Structure
```
web-scraping-task/
│
├── web_scraper.py          # Main scraping script
├── scraped_data.csv        # Extracted data (generated after running)
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── screenshots/           # (Optional) Output screenshots
    └── output_preview.png
```

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd web-scraping-task
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install beautifulsoup4 requests lxml
```

## ▶️ How to Run

```bash
python web_scraper.py
```

**Expected Output:**
- Console will show scraping progress
- `scraped_data.csv` file will be created with extracted data

## 🎯 Features Implemented

- ✅ Fetches HTML content using `requests` library
- ✅ Parses HTML using `BeautifulSoup`
- ✅ Identifies and extracts specific HTML tags and attributes
- ✅ Extracts text, links, and structured data
- ✅ **Handles missing tags safely** with error handling
- ✅ Stores data in CSV format
- ✅ Follows **ethical scraping practices**

## 📊 Data Extracted

The script extracts the following information from quotes.toscrape.com:
- **Quote Text** - The actual quote
- **Author** - Name of the person who said it
- **Tags** - Categories/topics associated with the quote

### Sample Output (scraped_data.csv):
| quote | author | tags |
|-------|--------|------|
| "The world as we have..." | Albert Einstein | change, deep-thoughts, thinking |
| "It is our choices..." | J.K. Rowling | abilities, choices |

## 🔒 Ethical Considerations

- ✅ Using **quotes.toscrape.com** - a legal, scraping-friendly practice website
- ✅ Respecting robots.txt guidelines
- ✅ Adding delays to avoid overloading servers
- ✅ Not scraping copyrighted or sensitive data
- ✅ Using scraped data responsibly for learning purposes only

## 📝 Interview Questions & Answers

### 1. What is web scraping?
**Answer:** Web scraping is the automated process of extracting data from websites using code. It involves fetching HTML content, parsing it, and extracting relevant information for analysis or storage.

### 2. Difference between HTML and DOM?
**Answer:** 
- **HTML** - Static markup language; the raw code sent by the server
- **DOM (Document Object Model)** - Tree-like representation of HTML in browser memory; can be dynamically modified by JavaScript

### 3. BeautifulSoup vs Selenium?
**Answer:**
| BeautifulSoup | Selenium |
|---------------|----------|
| Parses static HTML | Controls actual browser |
| Faster and lightweight | Slower, resource-intensive |
| Cannot handle JavaScript | Handles dynamic content |
| Good for simple scraping | Good for complex interactions |

### 4. Legal concerns in scraping?
**Answer:**
- Check website's Terms of Service
- Respect robots.txt file
- Don't scrape copyrighted content without permission
- Avoid overloading servers (DDoS-like behavior)
- Don't scrape personal/sensitive data

### 5. How to handle dynamic websites?
**Answer:**
- Use **Selenium** or **Playwright** for JavaScript-rendered content
- Use **requests-html** for simpler dynamic content
- Inspect network requests and use API endpoints directly
- Use headless browsers for complex interactions

## 🐛 Error Handling

The script includes:
- Try-except blocks for network errors
- Safe handling of missing HTML tags
- Timeout settings for requests
- Graceful degradation when data is unavailable

## 📸 Screenshots

*(Add screenshots of your output here)*

## 🎓 Learning Outcomes

- ✅ Understanding HTML structure and CSS selectors
- ✅ Making HTTP requests in Python
- ✅ Parsing and navigating HTML documents
- ✅ Data extraction and CSV file handling
- ✅ Error handling in web scraping
- ✅ Ethical and legal considerations in web scraping

## 🔗 Useful Resources

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://requests.readthedocs.io/)
- [Practice Scraping Sites](http://quotes.toscrape.com/)

## 👨‍💻 Author

**Your Name**  
Python Developer Intern  
Task 13 - Web Scraping Project

---

## 📌 Note

This project is created for educational purposes as part of a Python Developer Internship program. The scraping is performed on a legally permitted practice website.

**Happy Scraping! 🚀**
