import os, sys
from file_handling import copy_files_recursive, generate_pages_recursive

ABSOLUT_PATH_DST = os.path.abspath("docs")
ABSOLUT_PATH_STATIC = os.path.abspath("static")
MARKDOWN_CONTENT = os.path.abspath("content")
HTML_TEMPLATE = os.path.abspath("template.html")


def main():
    basepath = sys.argv[1] if sys.argv[1] != None else "/"

    copy_files_recursive(ABSOLUT_PATH_STATIC, ABSOLUT_PATH_DST)
    generate_pages_recursive(MARKDOWN_CONTENT, HTML_TEMPLATE, ABSOLUT_PATH_DST, basepath)
    

if __name__ == "__main__":
    main()

