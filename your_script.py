from DrissionPage import Chromium, ChromiumOptions
co = ChromiumOptions()
co.set_argument("--no-sandbox")
browser = Chromium(co)
page = browser.latest_tab
page.get("https://batdongsan.com.vn/nha-dat-cho-thue")
print(page.html)
page.close()
