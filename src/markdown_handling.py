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


if __name__ == "__main__":
    main()

