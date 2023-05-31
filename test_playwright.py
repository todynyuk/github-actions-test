import os
from playwright.sync_api import Playwright, sync_playwright, expect

URL = os.environ.get("URL")

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(URL)
    expect(page).to_have_title("MediaCMS")

register_page = page.get_by_role("link", name="Register")
register_page.click()

expect(page).to_have_url("https://demo.mediacms.io/accounts/signup/")
with sync_playwright() as playwright:
    run(playwright)
