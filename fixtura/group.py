class GroupHelper:
    def __init__(self,app):
        self.app=app

    def return_to_groups_page(self):
        wb = self.app.wb
        wb.find_element_by_link_text("group page").click()

    def create(self, group):
        wb = self.app.wb
        self.open_groups_page()
        wb.find_element_by_link_text("groups").click()
        # init group creations
        wb.find_element_by_name("new").click()
        # fill group form
        wb.find_element_by_name("group_name").click()
        wb.find_element_by_name("group_name").clear()
        wb.find_element_by_name("group_name").send_keys(group.name)
        wb.find_element_by_name("group_header").click()
        wb.find_element_by_name("group_header").clear()
        wb.find_element_by_name("group_header").send_keys(group.header)
        wb.find_element_by_name("group_footer").click()
        wb.find_element_by_name("group_footer").clear()
        wb.find_element_by_name("group_footer").send_keys(group.footer)
        #submit group creation
        wb.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wb = self.app.wb
        wb.find_element_by_link_text("groups").click()