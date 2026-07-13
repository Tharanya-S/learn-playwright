"""
==========================================================
Lesson 15 - Screenshots, Videos & Tracing
==========================================================

Topics Covered:
---------------
1. Page Screenshot
2. Element Screenshot
3. Full Page Screenshot
4. Record Videos
5. Start Trace
6. Stop Trace
==========================================================
"""

from pathlib import Path

from playwright.sync_api import sync_playwright, expect

BASE_DIR = Path(__file__).parent

SCREENSHOT_DIR = BASE_DIR / "screenshots"
VIDEO_DIR = BASE_DIR / "videos"
TRACE_DIR = BASE_DIR / "traces"

SCREENSHOT_DIR.mkdir(exist_ok=True)
VIDEO_DIR.mkdir(exist_ok=True)
TRACE_DIR.mkdir(exist_ok=True)

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    context = browser.new_context(
        record_video_dir=str(VIDEO_DIR)
    )

    # -------------------------------
    # Start Trace
    # -------------------------------

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()

    page.goto("https://www.saucedemo.com/")

    # Login

    page.get_by_placeholder("Username").fill("standard_user")

    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    # -------------------------------
    # Page Screenshot
    # -------------------------------

    page.screenshot(
        path=SCREENSHOT_DIR / "inventory_page.png"
    )

    # -------------------------------
    # Full Page Screenshot
    # -------------------------------

    page.screenshot(
        path=SCREENSHOT_DIR / "full_page.png",
        full_page=True
    )

    # -------------------------------
    # Element Screenshot
    # -------------------------------

    first_product = page.locator(
        ".inventory_item"
    ).first

    first_product.screenshot(
        path=SCREENSHOT_DIR / "first_product.png"
    )

    print("Screenshots Captured")

    page.wait_for_timeout(2000)

    # -------------------------------
    # Stop Trace
    # -------------------------------

    context.tracing.stop(
        path=TRACE_DIR / "trace.zip"
    )

    print("Trace Saved")

    page.close()

    context.close()

    browser.close()

    print("Video Saved Automatically")