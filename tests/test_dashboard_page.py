import time

from pages.dashboard_page import DashboardPage
from config.config import Links, DashboardPageDate


def test_short_feedback(browser):
    link = Links.dashboard_link
    dashboard_page = DashboardPage(browser, link)
    dashboard_page.open()
    dashboard_page.input_feedback(DashboardPageDate.short_feedback)
    dashboard_page.submit_feedback()
    time.sleep(2)
    dashboard_page.assert_feedback_too_short()

def test_long_feedback(browser):
    link = Links.dashboard_link
    dashboard_page = DashboardPage(browser, link)
    dashboard_page.open()
    dashboard_page.input_feedback(DashboardPageDate.long_feedback)
    dashboard_page.submit_feedback()
    time.sleep(2)
    dashboard_page.assert_feedback_submit()

def test_empty_feedback(browser):
    link = Links.dashboard_link
    dashboard_page = DashboardPage(browser, link)
    dashboard_page.open()
    dashboard_page.submit_feedback()
    time.sleep(2)
    dashboard_page.assert_feedback_too_short()
