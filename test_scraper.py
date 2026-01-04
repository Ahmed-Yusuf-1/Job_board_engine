from playwright.sync_api import sync_playwright
import json

def run():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://weworkremotely.com/categories/remote-python-jobs")

        all_jobs = []

        cards = page.locator(".new-listing-container").all()

        for card in cards:
            if card.locator(".listing-link--unlocked").count() > 0:
                title = card.locator(".new-listing__header__title").inner_text()
                company = card.locator(".new-listing__company-name").inner_text()
                location = card.locator(".new-listing__company-headquarters").inner_text()
                link = card.locator(".listing-link--unlocked").get_attribute("href")

                job_data = {
                    "title": title,
                    "company": company,
                    "location": location,
                    "link": link
                }

                all_jobs.append(job_data)
        
        with open("jobs.json", "w") as file:
            json.dump(all_jobs, file, indent=4)

        
        print("Finished! Saved jobs")
        browser.close()


if __name__ == "__main__":
    run()


def clean_text(text):
    new_text = text.lower().replace("/", " ")

