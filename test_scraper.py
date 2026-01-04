from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://weworkremotely.com/categories/remote-python-jobs")

        numofpages = page.locator(".new-listing-container").count()

        print(numofpages)

        browser.close()


if __name__ == "__main__":
    run()