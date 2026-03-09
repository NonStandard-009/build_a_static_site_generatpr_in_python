class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props={}) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplemented

    def props_to_html(self):
        output = ""

        for prop in self.props:
            output += f' {prop}="{self.props[prop]}"'

        return output
    
    def __repr__(self) -> str:
        return f"HTMLNode(\n\t{self.tag},\n\t{self.value},\n\t{self.children},\n{self.props_to_html()})"

