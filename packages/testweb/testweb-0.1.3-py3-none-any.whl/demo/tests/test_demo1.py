"""
@Author: kang.yang
@Date: 2023/11/14 14:46
"""
import testweb

from pages.demo_page import DemoPage


class TestSearch(testweb.TestCase):

    def start(self):
        self.page = DemoPage(self.driver)

    def test_search(self):
        self.page.open()
        self.page.ent_search.click()
        self.page.search_input.click()
        self.page.search_input.input("中兴")
        self.page.search_input.enter()
        self.page.first_item.click()


if __name__ == '__main__':
    testweb.main()

