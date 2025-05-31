from playwright.sync_api import sync_playwright, expect, Page
import pytest

from pages.courses_list_page import CoursesListPage, CheckVisibleCourseCardParams
from pages.create_course_page import CreateCoursePage, CourseFormParams

course_form_params_empty = CourseFormParams(
    title='',
    description='',
    estimated_time='',
    max_score='0',
    min_score='0'
)

course_form_params_tests = CourseFormParams(
    title='Playwright',
    description='Playwright',
    estimated_time='2 weeks',
    max_score='100',
    min_score='10'
)

card_params_tests = CheckVisibleCourseCardParams(
    index=0,
    title=course_form_params_tests.title,
    max_score=course_form_params_tests.max_score,
    min_score=course_form_params_tests.min_score,
    estimated_time=course_form_params_tests.estimated_time
)

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):

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


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page:CreateCoursePage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(course_form_params_empty)
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercises_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image('./testdata/files/image.png')
    create_course_page.check_visible_image_upload_view(is_image_upload=True)
    create_course_page.fill_create_course_form(course_form_params_tests)
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(card_params_tests)


