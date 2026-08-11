from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/")
    sleep(3)

    driver.find_element(By.LINK_TEXT, "HTML Form").click()

    assert "/forms/post" in driver.current_url, (
        "URL не изменился на /forms/post"
    )

    driver.back()
    sleep(5)

    assert (
        driver.current_url == "https://httpbin.qa-territory.online/"
    ), "Не удалось вернуться на исходный URL"
    sleep(3)

    driver.quit()
