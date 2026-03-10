from textnode import TextType, TextNode


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


def main():
    node = TextNode("This is **text** with a `code block`! word. here is another `code block` word", TextType.TEXT)

    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)

    
    print("[")
    for node in new_nodes:
        print(f"\t {node},")
    print("]")

if __name__ == "__main__":
    main()

