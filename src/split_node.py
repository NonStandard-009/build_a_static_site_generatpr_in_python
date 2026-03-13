from textnode import TextType, TextNode
from htmlnode import LeafNode
from extract_from_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type) -> list:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text_blocks = node.text.split(delimiter)
        
        for i in range(len(text_blocks)):
            if len(text_blocks[i]) == 0:
                continue

            if i % 2 == 0:
                new_nodes.extend([TextNode(text_blocks[i], TextType.TEXT)])
            else:
                new_nodes.extend([TextNode(text_blocks[i], text_type)])

    return new_nodes 


def split_nodes_image(old_nodes) -> list:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images_data = extract_markdown_images(node.text)
        if len(images_data) == 0:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for image in images_data:
            before, after = remaining_text.split(f"![{image[0]}]({image[1]})", 1)
            if before != "":
                new_nodes.extend([TextNode(before, TextType.TEXT)])
            new_nodes.extend([TextNode(image[0], TextType.IMAGE, image[1])])
            remaining_text = after
        
        if len(remaining_text) != 0:
            new_nodes.extend([TextNode(remaining_text, TextType.TEXT)])

    return new_nodes 


def split_nodes_link(old_nodes) -> list:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links_data = extract_markdown_links(node.text)
        if len(links_data) == 0:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for link in links_data:
            before, after = remaining_text.split(f"[{link[0]}]({link[1]})", 1)
            if before != "":
                new_nodes.extend([TextNode(before, TextType.TEXT)])
            new_nodes.extend([TextNode(link[0], TextType.LINK, link[1])])
            remaining_text = after
        
        if len(remaining_text) != 0:
            new_nodes.extend([TextNode(remaining_text, TextType.TEXT)])

    return new_nodes


def text_to_textnodes(text) -> list:
    node = TextNode(text, TextType.TEXT)
    old_nodes = [node]

    old_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
    old_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
    old_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
    old_nodes = split_nodes_image(old_nodes)
    old_nodes = split_nodes_link(old_nodes)

    return old_nodes


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)

        case TextType.BOLD:
            return LeafNode('b', text_node.text)

        case TextType.ITALIC:
            return LeafNode('i', text_node.text)

        case TextType.CODE:
            return LeafNode('code', text_node.text)

        case TextType.LINK:
            return LeafNode('a', text_node.text, {"href": text_node.url})

        case TextType.IMAGE:
            return LeafNode('a', text_node.text, {"href": text_node.url})

        case _:
            raise Exception("Incorrect TextType")

def text_to_children(text):
    children = []

    text_nodes = text_to_textnodes(text.strip(" "))

    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    
    return children

