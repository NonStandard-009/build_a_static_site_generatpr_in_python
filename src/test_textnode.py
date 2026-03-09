import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        
        self.assertEqual(node, node2)
        
    def test_eq_url(self):
        node3 = TextNode("This text node type is a Link", TextType.LINK)
        node4 = TextNode("This text node type is just PLAN", TextType.PLAN)
        
        self.assertEqual(node3.url, node4.url)
            
    def test_noteq_type(self):
        node5 = TextNode("This node is another link", TextType.LINK, "http://localhost:6969")
        node6 = TextNode("Is this node another link?", TextType.BOLD)

        self.assertNotEqual(node5.text_type, node6.text_type)


if __name__ == "__main__":
    unittest.main()

