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

    def test_bold_text(self):
        test_case = [
                TextNode("This is text with a **bold text** word, here is another `code block` word.", TextType.TEXT), 
                [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("bold text", TextType.BOLD),
                    TextNode(" word, here is another `code block` word.", TextType.TEXT),
                    ]
                ]
        new_nodes = split_nodes_delimiter([test_case[0]], "**", TextType.BOLD)

        self.assertEqual(new_nodes, test_case[1])

    def test_bold_code_text(self):
        test_case = [
                TextNode("This is text with a **bold text** word, here is another `code block` word.", TextType.TEXT), 
                [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("bold text", TextType.BOLD),
                    TextNode(" word, here is another ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" word.", TextType.TEXT)
                    ]
                ]
        new_nodes = split_nodes_delimiter([test_case[0]], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)

        self.assertEqual(new_nodes, test_case[1])
        pass


if __name__ == "__main__":
    unittest.main()

