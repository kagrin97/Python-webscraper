import os
import requests
from bs4 import BeautifulSoup

def get_countries(url):
  result = [];

  iban_result = requests.get(url);

  iban_soup = BeautifulSoup(iban_result.text, "html.parser")

  tbody_rows = iban_soup.find("tbody").find_all("tr");

  for row in tbody_rows:
    row_data = row.find_all("td")
    city = row_data[0].text.capitalize()
    currency = row_data[2].text
    result.append((city, currency))

  return result

def display(countries):   
  print("Hello! Please choose select a country by number:")
  for i in range(0, len(countries)):
    city = countries[i][0]
    print(f"#{i} {city}")


def answer(countries):
  try:
    user_input = int(input("#: "))
    if user_input >= 0 and user_input < len(countries): 
      print(f"You chose {countries[int(user_input)][0]}")
      print(f"The currency code is {countries[int(user_input)][1]}")
      return 
    else:
      print("Choose a number from the list.")
  except:
    print("That wasn't a number.")
  answer(countries)

def main():
  os.system("clear")
  url = "https://www.iban.com/currency-codes"

  countries = get_countries(url)
  
  display(countries)

  answer(countries)
  return


main()