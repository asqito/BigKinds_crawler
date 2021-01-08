from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# 설치된 크롬 브라우저 버전에 맞게 다운로드
driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.bigkinds.or.kr/v2/news/index.do")

time.sleep(1)

# 검색조건 : 기간
driver.find_element_by_xpath('//*[@id="date-filter-btn"]').click()

date_begin_box = driver.find_element_by_xpath('//*[@id="search-begin-date"]')
date_begin_box.send_keys(Keys.CONTROL + "a")
date_begin_box.send_keys(Keys.DELETE)
date_begin_box.send_keys("2015-01-01")

time.sleep(2)

date_end_box = driver.find_element_by_xpath('//*[@id="search-end-date"]')
date_end_box.send_keys(Keys.CONTROL + "a")
date_end_box.send_keys(Keys.DELETE)
date_end_box.send_keys("2015-12-31")

driver.find_element_by_xpath('//*[@id="date-confirm-btn"]').click()

# 검색조건 : 언론사 선택
driver.find_element_by_xpath('//*[@id="provider-filter-btn"]').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="중앙지"]').click()
driver.find_element_by_xpath('//*[@id="경제지"]').click()
driver.find_element_by_xpath('//*[@id="전문지"]').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="collapse-step-1"]/div/div/div/div/div[3]/div[2]/div/div[3]/button[2]').click()

# 검색조건 : 통합분류 (경제, IT_과학)
driver.find_element_by_xpath('//*[@id="category-filter-btn"]').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="category-tree-wrap"]/ul/li[2]/div/span[3]/label/span').click()
driver.find_element_by_xpath('//*[@id="category-tree-wrap"]/ul/li[8]/div/span[3]/label/span').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="collapse-step-1"]/div/div/div/div/div[3]/div[3]/div/div[3]/button[2]').click()

# 검색조건 : 상세검색 (검색어 범위 : 제목)
driver.find_element_by_xpath('//*[@id="detail-filter-btn"]').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="search-scope-type"]/option[text()="제목"]').click()

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_xpath('//*[@id="total-search-key"]')
search_box.send_keys("투자 유치")

time.sleep(1)

# 검색버튼 누르기
search_button = driver.find_element_by_xpath('//*[@id="collapse-step-1"]/div/div/div/div/div[1]/span/button')
search_button.click()


# 검색결과 누르기
time.sleep(5)  # 검색결과 리스트 로딩까지 시간 대기

for n in range(1, 11):  # 검색 결과 리스트 10개 차례대로 로딩
    x = '//*[@id="news-results"]/div[' + str(n) +']/div[2]/div[1]/h4'
    # print(x)
    driver.find_element_by_xpath(x).click()
    # 리스트 10개 미만일 때 예외 처리

    # 검색결과 리스트 누르면 팝업으로 결과 보여짐 -> 새로운 창으로 포커싱
    driver.switch_to.window(driver.window_handles[-1])
    driver.get_window_position(driver.window_handles[-1])

    # gettext = driver.find_element_by_class_name('news-detail__content')
    # print(gettext.text)

    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="news-detail-modal"]/div/div/div[3]/button').click()
    time.sleep(3)
    print(n)

time.sleep(3)
driver.close()


"""
# 결과 리스트 페이지 이동
# 다음 클릭, 1-처음, 2-이전, 3-1, 4-2, 5-3, 6-4, 7-5, 8-6, 9-7, 10-다음
driver.find_element_by_xpath('//*[@id="news-results-pagination"]/ul/li[10]/a').click()   
time.sleep(5)
driver.find_element_by_xpath('//*[@id="news-results-pagination"]/ul/li[4]/a').click()  # 9번째 페이지 클릭

n = 10
x = '//*[@id="news-results-pagination"]/ul/li[' + str(n) +']'
print(x)
print('//*[@id="news-results-pagination"]/ul/li[10]')

try:
    # 페이지 넘기기, 3 ~ 10
    # 예외 처리


except:
"""