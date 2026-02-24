# from playwright.sync_api import sync_playwright
# def search_laptopp(page,search_term):
#         page.goto("https://www.daraz.com.np")
#         page.type("input[name='q']", "laptop")
#         page.click(".search-box__button--1oH7")
#         print(input("Press any key to close browser"))
# def select_lap(page):
#         page.click(".picture-wrapper.jBwCF").first.click()
#         page.mouse.wheel(0,1000)     
#         page.click(".next-input.next-input-single.next-input-medium.next-number-picker-input")
# def add_to_cart(page):
#         page.click("text=Add to Cart")
#         page.once("dialog", lambda dialog: dialog.accept())
# def click_phone_number(page):
#         page.locator("text=Phone Number").click()
#         def main():
#          with sync_playwright() as p:
#           browser = p.chromium.launch(headless=False)
#           page = browser.new_page()
#           search_laptopp(page,search_term)
#           select_lap(page)
#           add_to_cart(page)
#          click_phone_number(page)
#         print(input("Press any key to close browser"))
#         main()

from playwright.sync_api import sync_playwright

def search_laptopp(page, search_term):
    page.goto("https://www.daraz.com.np")
    page.type("input[name='q']", search_term)
    page.click(".search-box__button--1oH7")

def select_lap(page):
    page.locator(".picture-wrapper.jBwCF").first.click()
    page.mouse.wheel(0,1000)     
    page.click(".next-input.next-input-single.next-input-medium.next-number-picker-input")

def add_to_cart(page):
    page.click("text=Add to Cart")
    page.once("dialog", lambda dialog: dialog.accept())

def click_phone_number(page):
    page.locator("text=Phone Number").click()

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        search_laptopp(page, "laptop")       
        select_lap(page)
        add_to_cart(page)
        click_phone_number(page)
        input("Press any key to close browser")
        browser.close()

main()