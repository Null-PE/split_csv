import os

def split(filehandler, encoding="CP932", output_path='output', keep_headers=True):
    file = open(filehandler, encoding=encoding)
    lines = file.readlines()
    subfile = None
    for line in lines:
        if "【select" in line:
            if subfile:
                subfile.close()
            name = line.split('】',1)[1]
            subfile = open(f"{output_path}/{name}.csv", "w", encoding="utf8")
        else:
            subfile.write(line)
    
    subfile.close()


if __name__ == "__main__":
    files = os.listdir("input")
    for file in files:
        if file is not os.path.isdir(file):
            split(os.path.join("input",file))