import unittest
from src.htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_output(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            }
        node = HTMLNode(
                tag="b",
                value="This is the text inside this node.",
                props={
                    "href": "https://www.google.com",
                    "target": "_blank",
                    }
                )
        self.assertEqual(node.props, props)

    def test_eq_tag(self):
        node = HTMLNode(
                tag="b",
                value="This is the text inside this node.",
                )
        node2 = HTMLNode(
                tag="b",
                value="This is the text inside this node.",
                )
        node3 = HTMLNode(
                tag="a",
                value="This is the text inside this node.",
                )

        self.assertEqual(node.tag, node2.tag)
        self.assertNotEqual(node.tag, node3.tag)

    def test_noteq_value(self):
        node = HTMLNode(
                tag="b",
                value="This is the text inside this node.",
                )
        node2 = HTMLNode(
                tag="b",
                value="This is the text inside this node.",
                )
        node3 = HTMLNode(
                tag="a",
                value="This is the link for this node.",
                )

        self.assertNotEqual(node.value, node3.value)
        self.assertNotEqual(node2.value, node3.value)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Come here to learn and stop being a soydev!",{"href":"https://boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://boot.dev">Come here to learn and stop being a soydev!</a>')



if __name__ == "__main__":
    unittest.main()

