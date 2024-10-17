import os,json 


path_scripts = "C:\depository\materials"


def show_files(exts =[".txt"],all =False):
    files_temp = []
    
    if all == True:
        items = os.listdir(path_scripts)
        for i in items:
            if os.path.isdir(os.path.join(f"{path_scripts}/{i}")):
                i_ = f"{i} || DIR"
                items[items.index(i)] = i_
        return items
    else:
        for i in exts:
            for j in os.listdir(path_scripts):
                if j.endswith(i):
                    files_temp.append(j)
        
        return files_temp


       
def read_file(file_path):
    with open(file_path,"r",encoding="utf-8") as f:
        data = f.read()
    
    return data

def write_file(file_path,data):
    with open(file_path,"w",encoding="utf-8") as f:
        f.write(data)
    f.close()
    