import bs4 as bs

soup = bs.BeautifulSoup(open("requestResults.txt"), 'html.parser')
f = open('requestResultsPretty.txt','w+')
f.writelines(soup.prettify())
f.close()
