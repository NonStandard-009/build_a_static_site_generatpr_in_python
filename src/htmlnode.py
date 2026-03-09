class HTMLNode:
    def __init__(self, tag=None, value=None, children=[], props={}) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        output = ""

        for prop in self.props:
            output += f' {prop}="{self.props[prop]}"'

        return output
    
    def __repr__(self) -> str:
        return f"HTMLNode(\n\t{self.tag},\n\t{self.value},\n\t{self.children},\n\t{self.props_to_html()})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props={}) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Node cannot have empty tag")
        
        if self.children == None:
            raise ValueError("Node must have children")
        
        children_to_html = ""
        for child in self.children:
            children_to_html += f'{child.to_html()}'

        return f'<{self.tag}{self.props_to_html()}>{children_to_html}</{self.tag}>'


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props={}) -> None:
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"HTMLNode(\n\t{self.tag},\n\t{self.value},\n\t{self.props_to_html()})"

