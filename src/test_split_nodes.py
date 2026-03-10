import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter


class TestSplitNodes(unittest.TestCase):
    def test_code_text(self):
        test_case = [
                TextNode("This is text with a `code block` word, here is another `code block` word.", TextType.TEXT), 
                [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" word, here is another ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" word.", TextType.TEXT)
                    ]
                ]
        new_nodes = split_nodes_delimiter([test_case[0]], "`", TextType.CODE)

        self.assertEqual(new_nodes, test_case[1])

