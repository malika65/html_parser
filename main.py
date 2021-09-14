import requests

from  bs4 import BeautifulSoup

import csv

# get url and return html 
def get_html(url):
    response = requests.get(url)
    return response.text  # return html of web page 

# get html and parse tag 'a' and get all links from href
def get_all_links(html):
    soap = BeautifulSoup(html,'lxml')
    tds = soap.find('tbody')
    links = []
    for td in tds:
        a = td.find('a').get('href')
        link = "https://coinmarketcap.com"+a
        links.append(link)

    return links

# get html of each link and return name and price of bicoins
def get_page_data(html):
    soap = BeautifulSoup(html,'lxml')

    try:
        name  = soap.find('h1',class_='priceHeading').text.strip()
    except:
        name = ''

    try:
        price = soap.find('div',class_='priceValue').text.strip()
    except:
        price = ''

    data = {'name': name, "price": price}
    return data 

# get all data and write it on csv
def write_csv(data):
    with open('coinmarketcap.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            (data['name'],
            data['price']))

        print(data['name'],'parsed')

# main function that loop all link and write them into csv 
def main():
    url = "https://coinmarketcap.com/all/views/all/"
    all_links = get_all_links(get_html(url))
    for i in all_links:
        html = get_html(i)
        data = get_page_data(html)
        write_csv(data)





if __name__ == '__main__':
    main()


