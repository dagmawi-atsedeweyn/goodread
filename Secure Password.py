import datetime
import requests
from bs4 import BeautifulSoup

def digit_sum(number):
    return sum(int(d) for d in str(number))

def shares_digit(num1, num2, num3):
    num1_str = str(num1)
    num2_str = str(num2)
    num3_str = str(num3)
    for c in num1_str:
        if c in num2_str and c in num3_str:
            return True
    return False

for year in range(2012, 2023):
    for month in range(1, 13):
        for day in range(1, 32):
            if digit_sum(year) + digit_sum(month) + digit_sum(day) == 10 and shares_digit(year, month, day) and shares_digit(day, year, year % 10):
                date_str = f"{month:02}/{day:02}/{year}"
                print(f"Searching for book discovered on {date_str}")
                
                # Search for book on Goodreads
                url = f"https://www.goodreads.com/search?q=Brian&t=book&search_type=books&search%5Bfield%5D=on&sort=rating&search_version=service&search%5Bquery%5D={date_str}"
                response = requests.get(url)
                soup = BeautifulSoup(response.content, "html.parser")
                
                # Find the first book result
                results = soup.select(".bookTitle")
                if len(results) > 0:
                    book_title = results[0].text.strip()
                    print(f"Brian discovered the book: {book_title}")
                else:
                    print("No books found for this date.")
