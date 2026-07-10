from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=False)

    # Create a new page
    page = browser.new_page()

    # Navigate to Google
    page.goto("https://www.google.com")

    # Print the page title
    print(f"Page title: {page.title()}")
    print(f"Current URL: {page.url}")
    
    # Wait for 5 seconds so you can see the output
    print("Waiting 5 seconds before closing...")
    time.sleep(5)

    # Close the browser
    browser.close()
    print("Browser closed!")