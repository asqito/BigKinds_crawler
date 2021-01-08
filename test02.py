from selenium import webdriver

# 설치된 크롬 브라우저 버전에 맞게 다운로드
driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.bigkinds.or.kr/v2/news/search.do")

# 검색조건 : 기간
search_button = driver.find_element_by_css_selector("date-filter-btn")
search_button.click()

search_box = driver.find_element_by_css_selector("input#search-begin-date")
search_box.send_keys("2015-01-01")

search_box = driver.find_element_by_css_selector("input#search-end-date")
search_box.send_keys("2015-12-31")

search_button = driver.find_element_by_css_selector("date-confirm-btn")
search_button.click()

driver.implicitly_wait(1)

# 검색 조건 : 언론사
driver.find_element_by_css_selector("btn.btn-sm.btn-default.main-search-filters__btn.dropdown-toggle").click()


find_element_by_id("중앙지").click()
find_element_by_id("경제지").click()
find_element_by_id("전문지").click()

driver.find_element_by_css_selector("btn.btn-sm.btn-primary.half.close-filter-btn").click()

driver.implicitly_wait(1)

# 시간 지연


# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("total-search-key.form-control main-search__keyword search-key")
search_box.send_keys("투자 유치")

# 검색버튼 누르기
search_button = driver.find_element_by_css_selector("btn.main-search__search-btn.news-search-btn")
search_button.click()


