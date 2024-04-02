import requests

def getLink(text):
    i = dataLast.find("<p><a href=\"https://college.uniyar.ac.ru/wp-content/uploads")
    if i != -1:
        link = ""
        for i in text[(i+13):-1]:
            if i == "\"":
                break
            else:
                link+=i
        return link

link = "https://college.uniyar.ac.ru/%D1%80%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B7%D0%B0%D0%BD%D1%8F%D1%82%D0%B8%D0%B9"

r = requests.get(link) #получение объекта страницы

"""
with open('site.html', 'r') as f:
    data = f.read()
    if data != r.content.decode("utf-8"):
        with open('site1.html', 'wb') as n:
            n.write(r.content)
            print("Update site.html")
"""

with open('site.html', 'r') as f:
    dataLast = f.read()

linkPDF = getLink(r.content.decode("utf-8"))
print(linkPDF)


"""
obj.content # получение объекта в байтах
"""
