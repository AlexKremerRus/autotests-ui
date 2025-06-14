import allure


@allure.step("Opening browser")
def open_browser():
    pass


@allure.step("Creating browser - {title}")
def create_course(title:str):
    pass

@allure.step("Closing browser")
def close_browser():
    ...


def test_feature ():
    open_browser()
    create_course()
    close_browser()

    with allure.step("Opening browser"):
        ...
    with allure.step("Creating course"):
        ...
    with allure.step("Closing browser"):
        pass