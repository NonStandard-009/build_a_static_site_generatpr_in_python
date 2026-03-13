import os
from file_handling import copy_files_recursive, generate_page

ABSOLUT_PATH_PUBLIC = os.path.abspath("public")
ABSOLUT_PATH_STATIC = os.path.abspath("static")
MARKDOWN_CONTENT = os.path.abspath("content/index.md")
HTML_TEMPLATE = os.path.abspath("template.html")


def main():
    copy_files_recursive(ABSOLUT_PATH_STATIC, ABSOLUT_PATH_PUBLIC)
    generate_page(MARKDOWN_CONTENT, HTML_TEMPLATE, ABSOLUT_PATH_PUBLIC)
    

if __name__ == "__main__":
    main()

