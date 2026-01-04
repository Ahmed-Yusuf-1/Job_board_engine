from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://weworkremotely.com/categories/remote-python-jobs")

        numofpages = page.locator(".new-listing-container").all()

        for card in numofpages:
            linkcount = card.locator(".listing-link--unlocked").count()
            
            if linkcount > 0:
                title = card.locator(".new-listing__header__title").inner_text()
                company = card.locator(".new-listing__company-name").inner_text()
                location = card.locator(".new-listing__company-headquarters").inner_text()
                link = card.locator(".listing-link--unlocked").get_attribute("href")
                print(f"{title} at {company} ({location}) - Link: {link}")

        browser.close()


if __name__ == "__main__":
    run()