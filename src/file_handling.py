import os, shutil


def create_directory(absolute_path):
    if os.path.exists(absolute_path):
        shutil.rmtree(absolute_path)
    os.mkdir(absolute_path)

def copy_files(src_path, dst_path):
    
    create_directory(dst_path)
    static_files = os.listdir(src_path)
    
    for item in static_files:
        new_src_path = os.path.join(src_path, item)
        
        if os.path.isfile(new_src_path):
            
            new_file_path = new_src_path
            shutil.copy(new_file_path, dst_path)

        else:
            
            new_dst_path = os.path.join(dst_path, item)
            copy_files(new_src_path, new_dst_path)

