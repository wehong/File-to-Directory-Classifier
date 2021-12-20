import sys
import os
import shutil

def declassify(abs_path):
    try:
        files = os.listdir(abs_path)
    except FileNotFoundError:
        print("Error - \'%s\' does not exist!" % abs_path)
        quit()

    print("Start de-classifying...\n")
    
    for f in files:
        tgt_dir = os.path.join(abs_path, f)
        if os.path.isdir(tgt_dir) and not f.startswith("."):
            files_in_tgtdir = os.listdir(tgt_dir)
            for fit in files_in_tgtdir:
                tgt = os.path.join(tgt_dir, fit)
                shutil.move(tgt, abs_path)
                print("\'%s\' moves to \'%s\'\n." % (tgt, abs_path))
            shutil.rmtree(tgt_dir, ignore_errors=True)
            print("Directory \'%s\' is removed.\n" % tgt_dir)
    
    print("De-classifying is finished.")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        declassify(os.getcwd())
    elif len(sys.argv) == 2:
        declassify(os.path.abspath(sys.argv[1]))
    else:
        print("Error. Improper number of parameters.")
        print("Usage: \'python %s\' or \'python %s <directory>\'" % (sys.argv[0], sys.argv[0]))
