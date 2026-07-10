from playwright.sync_api import sync_playwright

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
    
    # Wait for user input before closing
    input("Press Enter to close the browser...")

    # Close the browser
    browser.close()
    print("Browser closed!")