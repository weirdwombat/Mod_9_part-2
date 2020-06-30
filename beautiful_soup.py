import requests

url = 'https://dmacc.edu/schedule/Pages/result.aspx?Term=202101&CourseNumber=CIS189'
response = requests.get(url)
html = response.content
f = open('requestResults.txt', 'w+')
f.writelines(str(html))
f.close()



