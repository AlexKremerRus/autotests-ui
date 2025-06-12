from components.base_component import BaseComponent
from playwright.sync_api import Page,expect
from dataclasses import dataclass

@dataclass
class CourseFormParams:

    title: str
    estimated_time: str
    description: str
    max_score: str
    min_score: str


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.estimated_time_input = page.get_by_test_id(
            'create-course-form-estimated-time-input').locator('input')
        self.description_textarea = page.get_by_test_id('create-course-form-description-input').locator(
            'textarea').first
        self.msx_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')


    def fill(self, params: CourseFormParams):
        expect(self.title_input).to_be_visible()
        self.title_input.fill(params.title)

        expect(self.estimated_time_input).to_be_visible()
        self.estimated_time_input.fill(params.estimated_time)

        expect(self.description_textarea).to_be_visible()
        self.description_textarea.fill(params.description)

        expect(self.msx_score_input).to_be_visible()
        self.msx_score_input.fill(params.max_score)

        expect(self.min_score_input).to_be_visible()
        self.min_score_input.fill(params.min_score)

    def check_visible(self, params: CourseFormParams):
        expect(self.title_input).to_be_visible()
        expect(self.title_input).to_have_value(params.title)

        expect(self.estimated_time_input).to_be_visible()
        expect(self.estimated_time_input).to_have_value(params.estimated_time)

        expect(self.description_textarea).to_be_visible()
        expect(self.description_textarea).to_have_value(params.description)

        expect(self.msx_score_input).to_be_visible()
        expect(self.msx_score_input).to_have_value(params.max_score)

        expect(self.min_score_input).to_be_visible()
        expect(self.min_score_input).to_have_value(params.min_score)








