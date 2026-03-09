from htmlnode import *


def main():
    props = {
            "href": "https://www.google.com",
            "target": "_blank",
            }
    node = HTMLNode(props=props) 
    print(node.__repr__())

if __name__ == "__main__":
    main()

