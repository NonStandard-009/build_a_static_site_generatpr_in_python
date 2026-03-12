from enum import Enum
from htmlnode import ParentNode
from split_node import text_node_to_html_node, text_to_children
from textnode import TextNode, TextType


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

def markdown_to_blocks(markdown) -> list:
    md_blocks = []

    for block in markdown.split("\n\n"):
        if block != '': 
            md_blocks.append(block.strip('\n '))
    
    return md_blocks

def markdown_to_html_node(markdown_file):
    inner_parents = []
    md_blocks = markdown_to_blocks(markdown_file)
    
    for block in md_blocks:
        block_type = block_to_block_type(block)
        
        match block_type:
            case BlockType.HEADING:
                counter = 0
                for chr in block[:6]:
                    if chr != '#':
                        break
                    counter += 1
                children = text_to_children(block[counter:])
                parent_heading = ParentNode(f"h{counter}", children)
                inner_parents.append(parent_heading)
            
            case BlockType.PARAGRAPH:
                block_lines = block.split("\n")
                text = " ".join(block_lines)
                children = text_to_children(text)
                parent_paragraph = ParentNode("p", children)
                inner_parents.append(parent_paragraph)

            case BlockType.QUOTE:
                children = text_to_children(block)
                parent_quote = ParentNode("blockquote", children)
                inner_parents.append(parent_quote)
                
            case BlockType.UNORDERED_LIST:
                children = []
                list_items = block.split("\n")
                
                for item in list_items:
                    children.append(ParentNode("li", text_to_children(item[2:])))
                
                parent_unordered_list = ParentNode("ul", children)
                inner_parents.append(parent_unordered_list)
                
            case BlockType.ORDERED_LIST:
                children = []
                list_items = block.split("\n")
                
                for item in list_items:
                    children.append(ParentNode("li", text_to_children(item[2:])))
                
                parent_ordered_list = ParentNode("ol", children)
                inner_parents.append(parent_ordered_list)
                
            case BlockType.CODE:
                code_block = TextNode(block[4:-3], TextType.CODE)
                parent_code = ParentNode("pre", [text_node_to_html_node(code_block)])
                inner_parents.append(parent_code)

    return ParentNode("div", inner_parents)

