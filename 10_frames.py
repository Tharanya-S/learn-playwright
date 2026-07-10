"""
==========================================================
Lesson 10 - Frames (iFrames)
==========================================================

Topics Covered:
---------------
1. frame_locator()
2. page.frame()
3. Nested Frames
4. Assertions inside Frames
==========================================================
"""

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    context = browser.new_context()

    page = context.new_page()

    # ---------------------------------------------------
    # Open Website
    # ---------------------------------------------------

    page.goto("https://letcode.in/frame")

    # ===================================================
    # Example 1 : frame_locator()
    # ===================================================

    first_frame = page.frame_locator("#firstFr")

    first_frame.locator("input[name='fname']").fill("John")

    first_frame.locator("input[name='lname']").fill("Doe")

    print("Filled First Frame")

    page.wait_for_timeout(2000)

    # ===================================================
    # Example 2 : Nested Frame
    # ===================================================

    nested_frame = (
        page.frame_locator("#firstFr")
            .frame_locator("iframe")
    )

    nested_frame.locator("input[name='email']").fill(
        "john@test.com"
    )

    print("Filled Nested Frame")

    page.wait_for_timeout(2000)

    # ===================================================
    # Example 3 : Assertions
    # ===================================================

    expect(
        first_frame.locator("input[name='fname']")
    ).to_have_value("John")

    expect(
        first_frame.locator("input[name='lname']")
    ).to_have_value("Doe")

    expect(
        nested_frame.locator("input[name='email']")
    ).to_have_value("john@test.com")

    print("Assertions Passed")

    page.wait_for_timeout(2000)

    # ===================================================
    # Example 4 : page.frame()
    # ===================================================

    frame = page.frame(name="firstFr")

    if frame:

        print("Frame Found Using page.frame()")

        print(frame.url)

        frame.locator("input[name='fname']").fill("Playwright")

        page.wait_for_timeout(2000)

    else:

        print("Frame Not Found")

    browser.close()