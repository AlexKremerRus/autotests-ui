from playwright.sync_api import sync_playwright, expect, Page
import pytest

from components.courses.create_course_form_component import CourseFormParams
from pages.courses_list_page import CoursesListPage, CheckVisibleCourseCardParams
from pages.create_course_page import CreateCoursePage

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
def test_empty_courses_list(courses_list_page: CoursesListPage):

    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page.navbar.check_visible('username')
    courses_list_page.sidebar.check_visible()
    courses_list_page.toolbar_view.check_visible()

    courses_list_page.check_visible_empty_view()




@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page:CreateCoursePage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.create_course_toolbar.check_visible()

    create_course_page.image_upload_widget.check_visible()
    create_course_page.create_course_form.check_visible(course_form_params_empty)

    create_course_page.create_course_exercises_toolbar.check_visible()

    create_course_page.check_visible_exercises_empty_view()
    create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
    create_course_page.image_upload_widget.check_visible(is_image_upload=True)

    create_course_page.create_course_form.fill(course_form_params_tests) ###
    create_course_page.create_course_toolbar.click_create_course_button()
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible( card_params_tests)




