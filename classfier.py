import sys
import os
import shutil

def classify(abs_path, script_name):
    try:
        files = os.listdir(abs_path)
    except FileNotFoundError:
        print("Error - %s does not exist!" % abs_path)
        quit()
    #print(files)
    print("Start classifying...\n")
    for f in files:
        if os.path.isfile(f) and f != script_name and not f.startswith("."):
            #print(f)
            src_file = os.path.join(abs_path, f)
            dest_dir = os.path.join(abs_path, f[0].upper())
            try:
                os.mkdir(dest_dir)
                print("Directory %s is made.\n" % dest_dir)
            except FileExistsError:
                if not os.path.isdir(dest_dir):
                    print("Error - Destination directory %s exists but not a directory!\n" % dest_dir)
                    quit()
            shutil.move(src_file, dest_dir)
            print("File, %s has moved to directory, %s." % (src_file, dest_dir))

if __name__ == "__main__":
    #if len(sys.argv) == 1:
        #classify(os.getcwd(), sys.argv[0])
    #elif len(sys.argv) > 2:
        #classify(os.path.abspath(sys.argv[1]), sys.argv[0])
