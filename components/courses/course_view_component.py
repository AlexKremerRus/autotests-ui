from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from dataclasses import dataclass

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

        self.title = page.get_by_test_id('course-widget-title-text')
        self.image = page.get_by_test_id('course-preview-image')

        self.max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')

        self.estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')

    def check_visible(self, params:CheckVisibleCourseCardParams):
        expect(self.image).to_be_visible()

        expect(self.title.nth(params.index)).to_be_visible()
        expect(self.title.nth(params.index)).to_have_text(params.title)

        expect(self.max_score_text.nth(params.index)).to_be_visible()
        expect(self.max_score_text.nth(params.index)).to_have_text(f"Max score: {params.max_score}")

        expect(self.min_score_text.nth(params.index)).to_be_visible()
        expect(self.min_score_text.nth(params.index)).to_have_text(f"Min score: {params.min_score}")

        expect(self.estimated_time_text.nth(params.index)).to_be_visible()
        expect(self.estimated_time_text .nth(params.index)).to_have_text(
            f"Estimated time: {params.estimated_time}")