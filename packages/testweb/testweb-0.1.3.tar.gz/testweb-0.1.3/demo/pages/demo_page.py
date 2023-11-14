"""
@Author: kang.yang
@Date: 2023/11/14 14:40
"""
from testweb import Page, Elem


class DemoPage(Page):
    url = "https://www-test.qizhidao.com/"
    ent_search = Elem(role="link", name="查企业 查询分析全免费", desc="查企业入库")
    search_input = Elem(role="textbox", desc="输入框")
    first_item = Elem(role="link", name="中兴通讯股份有限公司")
