from bs4 import BeautifulSoup as BS
import requests
import csv

page = 1
count = 0
parser = []

while True:

    r = requests.get("https:...page/" + str(page) + '/')
    html = BS(r.content, 'html.parser')
    items = html.select('div.listco' or 'div.listco.prem_short')

    if (len(items)):
        for el in items:

            url = el.find_all('a')
            if not url:
                url = 'ERROR!!!'
                print(url)

            name = el.select('h4')
            if not name:
                name = 'ERROR!!!'
                print(name)

            description = el.select('p.listext1 > a')
            if not description:
                description = 'ERROR!!!'
                print(description)

            company = el.select('div.listcot > p:nth-of-type(3) > a')
            if not company:
                company = 'ERROR!!!'
                print(company)

            price = el.select('div.listcot > p.ltp1')
            if not price:
                price = 'ERROR!!!'
                print(price)

            address =el.select('div.listcotdown:nth-of-type(2)')

            if not address:
                address = 'ERROR!!!'
                print(address)

            time = el.select('div.listcotdown')

            if not time:
                time = 'ERROR!!!'
                print(time)


            count += 1
            p = (url[0].get('href'), name[0].text, description[0].text, company[0].text, price[0].text, address[0].text.strip(), time[0].text.replace('набору', 'набору '))
            # p.replace(u'\u200b', '*')
            parser.append(p)
        page += 1
    else:
        break

print('Найдено ', count, ' курсов')
print(parser)

with open("..\parser-courses2.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    file_writer.writerow([
        'url',
        'name',
        'description',
        'company',
        'price',
        'address',
        'time',
 ])
    for i in parser:
        file_writer.writerow(list(i))
