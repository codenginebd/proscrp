import re

class Formatter:
    def __init__(self):
        pass
    @staticmethod
    def refine_page(page):
        formatted_page = re.sub(r'<(.+?)>',' ',page)
        formatted_page = re.sub(r'(\s+)',' ',formatted_page)
        return formatted_page.strip()