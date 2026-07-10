"""
==========================================================
Lesson 14 - File Upload & Download
==========================================================

Topics Covered:
---------------
1. set_input_files()
2. Single File Upload
3. Multiple File Upload
4. Remove Uploaded Files
5. expect_download()
6. save_as()
==========================================================
"""

from pathlib import Path

from playwright.sync_api import sync_playwright, expect

BASE_DIR = Path(__file__).parent

FILE = BASE_DIR / "files" / "sample.txt"

DOWNLOAD_DIR = BASE_DIR / "downloads"

DOWNLOAD_DIR.mkdir(exist_ok=True)

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    context = browser.new_context()

    page = context.new_page()

    # ====================================================
    # FILE UPLOAD
    # ====================================================

    page.goto(
        "https://the-internet.herokuapp.com/upload"
    )

    page.locator("#file-upload").set_input_files(FILE)

    page.get_by_role(
        "button",
        name="Upload"
    ).click()

    expect(
        page.locator("h3")
    ).to_have_text("File Uploaded!")

    expect(
        page.locator("#uploaded-files")
    ).to_have_text("sample.txt")

    print("Single File Upload Successful")

    browser.close()