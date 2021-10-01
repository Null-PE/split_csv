import os
from pathlib import Path


def split(filehandler, encoding="CP932", output_path='output', keep_headers=True):
    subpath = f"{output_path}/{filehandler.split('.')[0]}"
    Path(subpath).mkdir(parents=True, exist_ok=True)
    file = open(filehandler, encoding=encoding)
    lines = file.readlines()
    subfile = None
    count = 0
    if lines:
        print(f"read {file.name} succeed.")
    for line in lines:
        if "【select" in line.lower():
            if subfile:
                subfile.close()
            name = line.strip().split('】', 1)[1]
            if name == '' or 'dummy' in name:
                name = line.strip()
            full_name = f"{subpath}/{count}_{name}.csv"
            print(f"write into subfile {full_name}")
            subfile = open(full_name, "w", encoding="utf8")
            count = count + 1
        elif subfile:
            subfile.write(line)
    if subfile:
        subfile.close()


if __name__ == "__main__":
    files = os.listdir("input")
    for file in files:
        if file == '.gitkeep':
            continue
        if file is not os.path.isdir(file):
            print(f"Split file: {file}")
            split(os.path.join("input", file))
