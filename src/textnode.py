from enum import Enum


class TextType(Enum):
    PLAN = "text"
    BOLD = "**bold text**"
    ITALIC = "_italic text_"
    CODE = "`code text`"
    LINK = "[anchor text] (url)"
    IMAGE = "![alt text] (url)" 

class TextNode:
    def __init__(self, text="", text_type=TextType.PLAN, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other ) -> bool:
        eq_text = self.text == other.text
        eq_text_type = self.text_type == other.text_type
        eq_url = self.url == other.url

        return eq_text and eq_text_type and eq_url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

