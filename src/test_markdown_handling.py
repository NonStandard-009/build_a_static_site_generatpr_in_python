import unittest
from markdown_handling import BlockType, markdown_to_blocks, block_to_block_type, markdown_to_html_node


class TestMarkdownHandling(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        resulting_types = []
        testing_blocks = [
            "# This # is a heading",
            "```\n if {This test block is code}:\n\tThe output should be = BlockType.CODE```",
            "> This is quoting Boots, a quote...",
            "- This is an item on a list\n- This is another item",
            "1. This is number one\n2. This is number two",
            "This is just lazy"
            ]
        
        for block in testing_blocks:
            resulting_types.append(block_to_block_type(block))


        self.assertListEqual(
                resulting_types,
                [
                    BlockType.HEADING,
                    BlockType.CODE,
                    BlockType.QUOTE,
                    BlockType.UNORDERED_LIST,
                    BlockType.ORDERED_LIST,
                    BlockType.PARAGRAPH
                    ]
                )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
                )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
                )


if __name__ == "__main__":
    unittest.main()

