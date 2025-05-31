from playwright.sync_api import sync_playwright, expect, Page
import pytest

from pages.courses_list_page import CoursesListPage, CheckVisibleCourseCardParams


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    # print("start test")
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courser_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courser_title).to_be_visible()
    expect(courser_title).to_have_text('Courses')

    empty_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_icon).to_be_visible()

    title_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(title_text).to_be_visible()
    expect(title_text).to_have_text('There is no results')

    description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_text).to_be_visible()
    expect(description_text).to_have_text('Results from the load test pipeline will be displayed here')
    # print("stop test")

# поставил урл но работать не будет так как не созданы карты
def test_course_page(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page.check_visible_course_card(
        CheckVisibleCourseCardParams(
            index=0,
            title="Playwright",
            max_score="10",
            min_score="1",
            estimated_time="2 weeks"
        )
    )