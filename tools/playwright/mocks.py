from playwright.sync_api import Page, Route


def mock_static_resource(page:Page):
    page.route("**/*.{ico,png,jpg,svg,mp4, woff2}", lambda route: route.abort())