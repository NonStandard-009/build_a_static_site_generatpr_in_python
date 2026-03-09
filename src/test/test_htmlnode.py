import unittest
from src.htmlnode import HTMLNode, ParentNode,LeafNode


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

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "This is very pretentious text")
        self.assertEqual(node.to_html(), "<i>This is very pretentious text</i>")


    def test_to_html_with_multiple_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("i", "pretentious child")
        child_node3 = LeafNode("b", "bold child")
        
        parent_node = ParentNode("div", [child_node, child_node2, child_node3])
        
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><i>pretentious child</i><b>bold child</b></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        
        self.assertEqual(
                parent_node.to_html(),
                "<div><span><b>grandchild</b></span></div>",
                )

    def test_to_html_with_children(self):
        pass


if __name__ == "__main__":
    unittest.main()

