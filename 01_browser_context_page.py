"""
==========================================================
Lesson 01 - Browser, BrowserContext & Page
==========================================================

Topics Covered:
---------------
1. sync_playwright()
2. Browser
3. BrowserContext
4. Page
5. page.goto()
6. page.title()
7. page.url

Website:
--------
https://www.saucedemo.com/

==========================================================
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    print("Starting Playwright...\n")

    # Launch Chromium Browser
    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    print("Browser Launched")

    # Create Browser Context
    context = browser.new_context()

    print("Browser Context Created")

    # Create a New Page (Browser Tab)
    page = context.new_page()

    print("New Page Created")

    # Open Website
    page.goto("https://www.saucedemo.com/")

    print("Website Opened")

    # Print Page Title
    print("\nPage Title:")
    print(page.title())

    # Print Current URL
    print("\nCurrent URL:")
    print(page.url)

    # Browser Information
    print("\nBrowser Information")
    print("----------------------")
    print(browser)

    print("\nContext Information")
    print("----------------------")
    print(context)

    print("\nPage Information")
    print("----------------------")
    print(page)

    # Wait so we can observe
    page.wait_for_timeout(5000)

    # Close Browser
    browser.close()

    print("\nBrowser Closed")