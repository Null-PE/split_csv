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
            if name is None or 'dummy' in name:
                name = f"{count}_{line.strip()}"
                count = count + 1
            print(f"write into subfile {subpath}/{name}.csv")
            subfile = open(f"{subpath}/{name}.csv", "w", encoding="utf8")
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
