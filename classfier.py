import sys
import os
import shutil

def classify(abs_path, script_name):
    # get file-list in specifed directory with absolute path string
    try:
        files = os.listdir(abs_path)
    except FileNotFoundError:
        print("Error - %s does not exist!" % abs_path)
        quit()

    print("Start classifying...\n")

    for f in files:
        if os.path.isfile(f) and f != script_name and not f.startswith("."):

            # make src, dest string
            src_file = os.path.join(abs_path, f)
            if f[0] >= '0' and f[0] <= '9':
                dest_dir = os.path.join(abs_path, "0")
            elif f[0].upper() >= "A" and f[0].upper() <= "Z":
                dest_dir = os.path.join(abs_path, f[0].upper())
            else:
                dest_dir = os.path.join(abs_path, "_")

            # make dest directory or use existing one
            try:
                os.mkdir(dest_dir)
                print("Directory %s is made.\n" % dest_dir)
            except FileExistsError:
                if not os.path.isdir(dest_dir):
                    print("Error - Destination directory %s exists but not a directory!\n" % dest_dir)
                    quit()
            
            # move file to dest directory
            shutil.move(src_file, dest_dir)
            print("File, %s has moved to directory, %s." % (f, dest_dir))
            
    print("Classifying is finished.")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        classify(os.getcwd(), sys.argv[0])
    elif len(sys.argv) > 2:
        classify(os.path.abspath(sys.argv[1]), sys.argv[0])
