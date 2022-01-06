import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_itemsss(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    input1 = browser.find_elements_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert input1, 'Не нашли кнопку добавления заказа';
