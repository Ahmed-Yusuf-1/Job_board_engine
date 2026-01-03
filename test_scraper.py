from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # 1. Launch the browser (headless=False means we can see it pop up!)
        browser = p.chromium.launch(headless=False)
        
        # 2. Open a new tab
        page = browser.new_page()
        
        # 3. Go to the website
        page.goto("https://weworkremotely.com/categories/remote-python-jobs")
        
        # 4. Print the page title to prove we are there
        print(page.title())
        
        # 5. Close the browser
        browser.close()

if __name__ == "__main__":
    run()