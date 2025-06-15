from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from dataclasses import dataclass

from elements.image import Image
from elements.text import Text
import allure

@dataclass
class CheckVisibleCourseCardParams:
    index: int
    title: str
    max_score: str
    min_score: str
    estimated_time: str

class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu =  CourseViewMenuComponent(page)

        self.title = Text(page, 'course-widget-title-text', "Title")
        self.image = Image(page, 'course-preview-image', "Image")

        self.max_score_text = Text(page, 'course-max-score-info-row-view-text', "max score")
        self.min_score_text = Text(page, 'course-min-score-info-row-view-text', 'min score')

        self.estimated_time_text = Text(page, 'course-estimated-time-info-row-view-text', 'estimated time')

    # @allure.step("Check visible course view at index '{params.index}' ")
    def check_visible(self, params:CheckVisibleCourseCardParams):
        # Дам объяснение зачем так а не декоратором - в декоратор падал объект класса и выдавал ссылку на объект а не его значения
        # Данное решение избавляет от этой проблеы - сейчас отображается корректно
        with allure.step(f"Check visible course view at index '{params.index}' "):

            self.image.check_visible(nth=params.index)

            self.title.check_visible(nth=params.index)
            self.title.check_have_text(nth=params.index, text=params.title)

            self.max_score_text.check_visible(nth=params.index)
            self.max_score_text.check_have_text(nth=params.index, text=f"Max score: {params.max_score}")

            self.min_score_text.check_visible(nth=params.index)
            self.min_score_text.check_have_text(nth=params.index, text=f"Min score: {params.min_score}")

            self.estimated_time_text.check_visible(nth=params.index)
            self.estimated_time_text.check_have_text(nth=params.index, text=f"Estimated time: {params.estimated_time}")
