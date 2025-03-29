from bs4 import BeautifulSoup
import requests
import csv


fields = ['Дом', 'Област', 'Град', 'Телефон', 'Имейл', 'Директор']

# Create CSV file and write fields
with open('orphanages.csv', newline='', mode='w') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(fields)

for i in range(1,68):

    # Pages 1 through 67
    URL = f'https://nadejdabg.org/orphanages.php?id={i}'

    # Get page
    response = requests.get(URL)
    html_content = response.text
    
    # Parse page
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.table

    # Find all rows in the table
    table_rows = table.find_all("tr")

    # Find information
    tds = []
    main_title = table.find(class_="main_title").text
    for column in table_rows:
        tds.append(column.find_all("td"))

    oblast = tds[3][1].text
    city = tds[5][1].text
    phone_numbers = tds[7][1].text
    email = tds[9][1].text
    director = tds[11][1].text

    # Make row
    row = [main_title, oblast, city, phone_numbers, email, director]

    # Append to CSV
    with open('orphanages.csv',newline='', mode='a') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerow(row)
    
    # Print for debugging purposes
    print(main_title)
    print(oblast)
    print(city)
    print(phone_numbers)
    print(email)
    print(director)

    print('-----------------------------------')

