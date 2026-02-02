# Job Board Engine 🚀

A robust, automated tool for scraping and aggregating job listings from multiple online platforms. Built with **Python** and **Playwright**, this engine handles dynamic web content to extract key job details and export them into a structured format.

---

## ✨ Features

* **Dynamic Content Handling:** Uses Playwright to scrape modern websites with heavy JavaScript loading.
* **Structured Data Output:** Automatically generates a `jobs.json` file containing title, company, location, and direct links.
* **Headless Operation:** Designed to run efficiently in the background without a GUI.
* **Extensible Scraper Logic:** Easily adaptable to different job board structures.

## 🛠 Tech Stack

* **Language:** Python 3.11+
* **Automation:** Playwright (Chromium/WebKit/Firefox)
* **Testing:** Pytest
* **Data Format:** JSON

---

## 🚀 Getting Started

### Prerequisites

* Python 3.11 or higher installed.
* `pip` for package management.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Ahmed-Yusuf-1/job_board_engine.git](https://github.com/Ahmed-Yusuf-1/job_board_engine.git)
    cd job_board_engine
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # Linux/MacOS
    source venv/bin/activate
    # Windows
    .\venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install playwright pytest
    playwright install
    ```

---

## 📂 Usage

To run the scraper and update the job database:

```bash
python test_scraper.py
