import os
from src.file_handling import copy_files

ABSOLUT_PATH_PUBLIC = os.path.abspath("../public/")
ABSOLUT_PATH_STATIC = os.path.abspath("../static")


def main():
    copy_files(ABSOLUT_PATH_STATIC, ABSOLUT_PATH_PUBLIC)

if __name__ == "__main__":
    main()

