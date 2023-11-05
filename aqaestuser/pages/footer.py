from selenium.webdriver.common.by import By
from pages.base import Base


class Footer(Base):


    def get_link(self):
        return self.is_clickable()
        pass

