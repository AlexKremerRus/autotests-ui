from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    expect(email_input).to_be_visible()
    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    expect(password_input).to_be_visible()
    button_login = page.get_by_test_id('login-page-login-button')
    expect(button_login).to_be_visible()

    email_input.fill('user.name@gmail.com')

    password_input.fill("password")
    button_login.click()
    wrong_email_password = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_password).to_be_visible()
    expect(wrong_email_password).to_have_text('Wrong email or password')
    page.wait_for_timeout(1000)
