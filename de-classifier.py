import sys
import os
import shutil

def declassify(abs_path):
    try:
        files = os.listdir(abs_path)
        print(files)
    except FileNotFoundError:
        print("Error - %s does not exist!" % abs_path)
        quit()

    print("Start classifying...\n")
    
    for f in files:
        if os.path.isdir(f) and not f.startswith("."):
            tgt_dir = os.path.join(abs_path, f)
            files_in_tgtdir = os.listdir(tgt_dir)
            for fit in files_in_tgtdir:
                tgt = os.path.join(tgt_dir, fit)
                shutil.move(tgt, abs_path)
            shutil.rmtree(tgt_dir, ignore_errors=True)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        declassify(os.getcwd())
    elif len(sys.argv) >= 2:
        declassify(os.path.abspath(sys.argv[1]))