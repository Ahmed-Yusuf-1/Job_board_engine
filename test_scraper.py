from playwright.sync_api import sync_playwright
import json

def search(query):
    query_words = clean_text(query)

    first_word = query_words[0]
    results = set(inverted_index.get(first_word, []))

    for word in query_words[1:]:
            id = set(inverted_index.get(word, []))
            results = results & id
    return list(results)



    

def clean_text(text):
    text = text.replace("/", " ")

    special = "!.,()?"

    for char in special:
        text = text.replace(char, "")
    return text.lower().split(" ")


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

        global inverted_index
        inverted_index = {}

        for index, job in enumerate(all_jobs):
            words = clean_text(job['title'])

            for word in words:
                if word not in inverted_index:
                    inverted_index[word] = [index]
                else:
                    inverted_index[word].append(index)


    while True:
        query = input("Search for a job (or exit): ").lower()
        if query == "exit":
            break

        matches = search(query)
        print(f"Found {len(matches)} jobs")

        for index in matches:
            job = all_jobs[index]
            print(f"{job['title']} @ {job['company']}, {job['location']} Link: {job['link']}")
            print("-" * 20)


if __name__ == "__main__":
    run()