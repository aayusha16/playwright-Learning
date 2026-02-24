# # # from playwright.sync_api import sync_playwright

# # # with sync_playwright() as p:
# # #     browser = p.chromium.launch(headless=False)
# # #     page = browser.new_page()
# # #     page.goto("https://www.daraz.com.np")
    
# # #     page.type("input[name='q']", "laptop")
# # #     page.click(".search-box__button--1oH7")   
# # #     # input("enter any keyt to closee browser")
# # #     print(input("enter any key"))
    
    
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.daraz.com.np")
    
    # Search laptop
    page.type("input[name='q']", "laptop")
    page.click(".search-box__button--1oH7")
    page.locator(".picture-wrapper.jBwCF ").first.click()
    page.mouse.wheel(0,1000)
    page.click(".next-input.next-input-single.next-input-medium.next-number-picker-input")
    page.click("text=Add to Cart")
    page.once("dialog", lambda dialog: dialog.accept())
    page.locator("text=Phone Number").click
    
    print(input("Press any key to close browser"))
# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.daraz.com.np")
    
#     # Search laptop
#     page.fill("input[name='q']", "laptop")
#     page.click(".search-box__button--1oH7")
#     page.click(".picture-wrapper.jBwCF")
#     # page.click(".next-input.next-input-single.next-input-medium.next-number-picker-input")
#     # page.fill("#module_quantity-input", "2")
#     # page.click(".cart-icon-daraz")
    
   
#     print(input("Press any key to close browser"))

