from enum import Enum


class AllureStories(str, Enum):
    COURSES = "Courses"
    DASHBOARD = "Dashboard"
    REGISTRATION = "Registration"
    AUTHORIZATION = "Authorization"