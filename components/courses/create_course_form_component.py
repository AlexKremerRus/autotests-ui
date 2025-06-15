from components.base_component import BaseComponent
from playwright.sync_api import Page,expect
from dataclasses import dataclass

from elements.input import Input
from elements.textarea import Textarea
import allure

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

        self.title_input = Input(page, 'create-course-form-title-input', "title")
        self.estimated_time_input = Input(page,
            'create-course-form-estimated-time-input', "estimated time")
        self.description_textarea = Textarea(page, 'create-course-form-description-input', 'description')
        self.msx_score_input = Input(page, 'create-course-form-max-score-input', "max score")
        self.min_score_input = Input(page, 'create-course-form-min-score-input', "min score")

    @allure.step("Fill course form")
    def fill(self, params: CourseFormParams):
        self.title_input.check_visible()
        self.title_input.fill(params.title)

        self.estimated_time_input.check_visible()
        self.estimated_time_input.fill(params.estimated_time)

        self.description_textarea.check_visible()
        self.description_textarea.fill(params.description)

        self.msx_score_input.check_visible()
        self.msx_score_input.fill(params.max_score)

        self.min_score_input.check_visible()
        self.min_score_input.fill(params.min_score)


    @allure.step("Check visible course form")
    def check_visible(self, params: CourseFormParams):
        self.title_input.check_visible()
        self.title_input.check_have_value(params.title)

        self.estimated_time_input.check_visible()
        self.estimated_time_input.check_have_value(params.estimated_time)

        self.description_textarea.check_visible()
        self.description_textarea.check_have_value(params.description)

        self.msx_score_input.check_visible()
        self.msx_score_input.check_have_value(params.max_score)

        self.min_score_input.check_visible()
        self.min_score_input.check_have_value(params.min_score)








