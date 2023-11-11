from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def extract_naver_fashion_keyword():
    driver_path = '/Users/sonjisu/PycharmProjects/cloud-data-pipeline/etl/infra/chromedriver'
    service = Service(executable_path=driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument("--disable-gpu")
    options.add_argument("lang=ko_KR")
    options.add_argument("--incognito")
    options.add_argument("--safebrowsing-disable-download-protection")
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    naver_shopping_insight_url = 'https://datalab.naver.com/shoppingInsight/sCategory.naver'
    driver.get(naver_shopping_insight_url)

    driver.find_element(By.CSS_SELECTOR, "#content > div.section_instie_area.space_top > div > div.section.insite_inquiry > div > div > div:nth-child(1) > div > div:nth-child(2) > span").click()
    driver.find_element(By.CSS_SELECTOR, "a[data-cid='50000167']").click()

    driver.find_element(By.CSS_SELECTOR, '#content > div.section_instie_area.space_top > div > div.section.insite_inquiry > div > div > div:nth-child(2) > div.set_period_target > span:nth-child(1) > div:nth-child(2) > span').click()
    month_list = driver.find_elements(By.CSS_SELECTOR, '#content > div.section_instie_area.space_top > div > div.section.insite_inquiry > div > div > div:nth-child(2) > div.set_period_target > span:nth-child(1) > div:nth-child(2) > ul > li')
    month_list[-1].click()

    driver.find_element(By.CSS_SELECTOR, '#content > div.section_instie_area.space_top > div > div.section.insite_inquiry > div > div > div:nth-child(4) > div > div > span:nth-child(2)').click()
    driver.find_element(By.CSS_SELECTOR, '#content > div.section_instie_area.space_top > div > div.section.insite_inquiry > div > div > div:nth-child(5) > div > div > span:nth-child(3)').click()
    driver.find_element(By.CSS_SELECTOR, '#content > div.section_instie_area.space_top > div > div.section.insite_inquiry > div > div > div:nth-child(5) > div > div > span:nth-child(4)').click()

    driver.find_element(By.CSS_SELECTOR, '#content > div.section_instie_area.space_top > div > div.section.insite_inquiry > div > a').click()
    keyword_tags = driver.find_elements(By.CSS_SELECTOR,
                                        '#content > div.section_instie_area.space_top > div > div:nth-child(2) > div.section_insite_sub > div > div > div.rank_top1000_scroll > ul > li')
    keyword_list = []
    for keyword_tag in keyword_tags:
        keyword = keyword_tag.text.split('\n')[-1]
        keyword_list.append(keyword)

    return keyword_list

