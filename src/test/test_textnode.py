import unittest
from src.textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        
        self.assertEqual(node, node2)
        
    def test_eq_url(self):
        node3 = TextNode("This text node type is a Link", TextType.LINK)
        node4 = TextNode("This text node type is just PLAN", TextType.TEXT)
        
        self.assertEqual(node3.url, node4.url)
            
    def test_noteq_type(self):
        node5 = TextNode("This node is another link", TextType.LINK, "http://localhost:6969")
        node6 = TextNode("Is this node another link?", TextType.BOLD)

        self.assertNotEqual(node5.text_type, node6.text_type)

    def test_plain_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
                
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_italic_text(self):
        node2 = TextNode("This is pretentious text", TextType.ITALIC)
        html_node2 = text_node_to_html_node(node2)

        self.assertEqual(html_node2.tag, 'i')
        self.assertEqual(html_node2.value, "This is pretentious text")

    def test_link_text(self):
        node3 = TextNode("Come out and learn", TextType.LINK, "https://boot.dev")
        html_node3 = text_node_to_html_node(node3)
        
        self.assertEqual(html_node3.tag, 'a')
        self.assertNotEqual(html_node3.props, None)


if __name__ == "__main__":
    unittest.main()

