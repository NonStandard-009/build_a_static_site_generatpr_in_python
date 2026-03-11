from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block) -> BlockType:
    if block.startswith('#'):
        counter = 0
        for chr in block[:6]:
            if chr != '#':
                break
            counter += 1
        if 1 <= counter <= 6 and block[counter] == ' ':
            return BlockType.HEADING
    
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    elif block.startswith('>') or block.startswith('> '):
        return BlockType.QUOTE
    
    elif block.startswith("- "):
        return BlockType.UNORDERED_LIST
    
    elif block.startswith("1. "):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    md_blocks = []

    for block in markdown.split("\n\n"):
         md_blocks.append(block.strip('\n '))
    
    return md_blocks

def main():
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    
    md_blocks = markdown_to_blocks(md)

    print(md_blocks)

    for block in md_blocks:
        print(block)

    testing_blocks = [
            "# This # is a heading",
            "```\n if {This test block is code}:\n\tThe output should be = BlockType.CODE```",
            "> This is quoting Boots, a quote...",
            "- This is an item on a list\n- This is another item",
            "1. This is number one\n2. This is number two",
            "This is just lazy"
            ]
    
    for block in testing_blocks:
        print(block_to_block_type(block))


if __name__ == "__main__":
    main()

