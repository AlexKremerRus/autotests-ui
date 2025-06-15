from components.base_component import BaseComponent
from playwright.sync_api import Page,expect

from elements.button import Button
from elements.text import Text
import allure

class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'title')
        self.create_exercise_button = Button(page, 'create-course-exercises-box-toolbar-create-exercise-button', 'exercise button')

    @allure.step("Check visible course exercises toolbar view")
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Exercises')
        self.create_exercise_button.check_visible()

    @allure.step("Click create exercise button")
    def click_create_exercises_button(self):
        self.create_exercise_button.click()