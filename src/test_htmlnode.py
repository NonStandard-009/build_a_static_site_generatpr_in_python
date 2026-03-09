import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_output(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            }
        node = HTMLNode(
                tag="<b>",
                value="This is the text inside this node.",
                props={
                    "href": "https://www.google.com",
                    "target": "_blank",
                    }
                )
        self.assertEqual(node.props, props)

    def test_eq_tag(self):
        node = HTMLNode(
                tag="<b>",
                value="This is the text inside this node.",
                )
        node2 = HTMLNode(
                tag="<b>",
                value="This is the text inside this node.",
                )
        node3 = HTMLNode(
                tag="<a>",
                value="This is the text inside this node.",
                )

        self.assertEqual(node.tag, node2.tag)
        self.assertNotEqual(node.tag, node3.tag)

    def test_noteq_value(self):
        node = HTMLNode(
                tag="<b>",
                value="This is the text inside this node.",
                )
        node2 = HTMLNode(
                tag="<b>",
                value="This is the text inside this node.",
                )
        node3 = HTMLNode(
                tag="<a>",
                value="This is the link for this node.",
                )

        self.assertNotEqual(node.value, node3.value)
        self.assertNotEqual(node2.value, node3.value)


if __name__ == "__main__":
    unittest.main()

