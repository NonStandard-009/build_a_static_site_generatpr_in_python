import unittest
from textnode import TextNode, TextType
from split_node import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes


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

    def test_split_images(self):
        node = TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
                )
        new_nodes = split_nodes_image([node])
        
        self.assertListEqual(
                [
                    TextNode("This is text with an ", TextType.TEXT),
                    TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" and another ", TextType.TEXT),
                    TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                    ],
                new_nodes,
                )
    
    def test_split_links(self):
        node = TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.TEXT,
                )
        new_nodes = split_nodes_link([node])
        
        self.assertListEqual(
                [
                    TextNode("This is text with a link ", TextType.TEXT),
                    TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                    TextNode(" and ", TextType.TEXT),
                    TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                    ],
                new_nodes,
                )

    def test_text_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        
        self.assertListEqual(
                [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                    ],
                new_nodes
                )


if __name__ == "__main__":
    unittest.main()

