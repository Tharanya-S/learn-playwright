from playwright.sync_api import sync_playwright

print("Starting Playwright...")

with sync_playwright() as p:
    print("Launching browser...")
    # Launch the browser
    browser = p.chromium.launch(headless=False)

    print("Creating new page...")
    # Create a new page
    page = browser.new_page()

    print("Navigating to Google...")
    # Navigate to Google
    page.goto("https://www.google.com")

    # Print the page title
    print(f"Page title: {page.title()}")
    
    # Print the current URL
    print(f"Current URL: {page.url}")
    
    print("Closing browser...")
    # Close the browser
    browser.close()

print("Script completed!")