class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def add(self, new_project_name):
        wd = self.app.wd
        # go to manage project page
        self.return_to_project_page()
        # init project creation
        wd.find_element_by_xpath("//form[@class='action-button'][@action='manage_proj_create_page.php']").click()
        # fill group form
        self.fill_form(new_project_name)
        # submit project creation
        wd.find_element_by_xpath("//input[@class='button'][@value='Добавить проект']").click()
        # go to manage project page
        self.return_to_project_page()
        self.project_cache = None

    def delete_by_name(self, name):
        wd = self.app.wd
        # go to manage project page
        self.return_to_project_page()
        # select project by id
        self.select_project_by_name(name)
        # submit deletion
        wd.find_element_by_xpath("//input[@class='button'][@value='Удалить проект']").click()
        wd.find_element_by_xpath("//input[@class='button'][@value='Удалить проект']").click()
        # go to manage project page
        self.return_to_project_page()
        self.project_cache = None


    def select_project_by_name(self, name):
        wd = self.app.wd
        # select group by id
        wd.find_element_by_link_text(name).click()

    def fill_form(self, project_name):
        wd = self.app.wd
        self.change_field_value("name", project_name)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_project_page(self):
        wd = self.app.wd
        wd.find_element_by_class_name("manage-menu-link").click()
        wd.get("http://localhost/mantisbt-1.3.0/manage_proj_page.php")

    def count(self):
        wd = self.app.wd
        self.return_to_project_page()
        return len(self.get_project_list())

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.return_to_project_page()
            self.project_cache = []
            for element in wd.find_elements_by_xpath("//div[@class='form-container' and not(@id)]//table/tbody/tr"):
                text = element.find_element_by_xpath("td").text
                self.project_cache.append(text)
        return list(self.project_cache)
