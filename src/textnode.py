from enum import Enum


class TextType(Enum):
    TEXT = ""
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"

class TextNode:
    def __init__(self, text="", text_type=TextType.TEXT, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other ) -> bool:
        eq_text = self.text == other.text
        eq_text_type = self.text_type == other.text_type
        eq_url = self.url == other.url

        return eq_text and eq_text_type and eq_url

    def __repr__(self) -> str:
        if self.url == None:
            return f"TextNode({self.text}, {self.text_type})"
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

