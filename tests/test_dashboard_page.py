import time
from pages.dashboard_page import DashboardPage
from config.config import Links, DashboardPageDate


class TestFeedback:
    def test_short_feedback(self, browser):
        link = Links.dashboard_link
        dashboard_page = DashboardPage(browser, link)
        dashboard_page.open()
        dashboard_page.input_feedback(DashboardPageDate.short_feedback)
        dashboard_page.submit_feedback()
        dashboard_page.assert_feedback_too_short()


    def test_long_feedback(self, browser):
        link = Links.dashboard_link
        dashboard_page = DashboardPage(browser, link)
        dashboard_page.open()
        dashboard_page.input_feedback(DashboardPageDate.long_feedback)
        dashboard_page.submit_feedback()
        dashboard_page.assert_feedback_submit()


    def test_empty_feedback(self, browser):
        link = Links.dashboard_link
        dashboard_page = DashboardPage(browser, link)
        dashboard_page.open()
        dashboard_page.submit_feedback()
        dashboard_page.assert_feedback_too_short()

class TestChecklist:
    def test_checkboxes(self, browser):
        link = Links.dashboard_link
        dashboard_page = DashboardPage(browser, link)
        dashboard_page.open()
        dashboard_page.click_checkboxes()
