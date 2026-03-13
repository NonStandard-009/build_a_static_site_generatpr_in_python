import os, shutil
from markdown_handling import extract_title, markdown_to_html_node


def create_directory(absolute_path):
    if os.path.exists(absolute_path):
        shutil.rmtree(absolute_path)
    os.mkdir(absolute_path)

def copy_files_recursive(src_path, dst_path):
    
    create_directory(dst_path)
    static_files = os.listdir(src_path)
    
    for item in static_files:
        new_src_path = os.path.join(src_path, item)
        
        if os.path.isfile(new_src_path):
            
            new_file_path = new_src_path
            shutil.copy(new_file_path, dst_path)

        else:
            
            new_dst_path = os.path.join(dst_path, item)
            copy_files_recursive(new_src_path, new_dst_path)

def generate_page(from_path, template_path="LMAO", dst_path="LMAO"):
    print(f"Generating page from {from_path} to {dst_path} using {template_path}")
    
    with open(from_path, 'r') as src_file:
        md_file = src_file.read()
    
    with open(template_path, 'r') as template_file:
        html_template = template_file.read()
    
    html_string = markdown_to_html_node(md_file).to_html()
    title = extract_title(md_file)
    
    new_template = html_template.replace("{{ Title }}", title)
    new_template = new_template.replace("{{ Content }}", html_string)

    final_dst = os.path.join(dst_path, "index.html")
    with open(final_dst, 'w') as html_file:
        html_file.write(new_template)

