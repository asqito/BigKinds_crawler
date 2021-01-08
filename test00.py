"""
page = 0

while True:
    page = page + 1

    if page % 10 == 1:
        print("Page no : ", page)

    elif page > 30:
        break

    else:
        print("Page else no : ", page)


n = 10
x = '//*[@id="news-results-pagination"]/ul/li[' + str(n) +']'
print(x)
print('//*[@id="news-results-pagination"]/ul/li[10]')

"""

for n in range(1, 11):
    print(n)

