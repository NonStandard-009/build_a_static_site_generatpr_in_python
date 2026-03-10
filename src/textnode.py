from enum import Enum
from src.htmlnode import LeafNode


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
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)

        case TextType.BOLD:
            return LeafNode('b', text_node.text)

        case TextType.ITALIC:
            return LeafNode('i', text_node.text)

        case TextType.CODE:
            return LeafNode('code', text_node.text)

        case TextType.LINK:
            return LeafNode('a', text_node.text, {"href": text_node.url})

        case TextType.IMAGE:
            return LeafNode('a', text_node.text, {"href": text_node.url})

        case _:
            raise Exception("Incorrect TextType")

