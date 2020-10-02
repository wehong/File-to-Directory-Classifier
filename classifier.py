import sys
import os
import shutil

def hangul_dir(ko):
    if ko >= "가" and ko < "나":
        return "가"
    elif ko >= "나" and ko < "다":
        return "나"
    elif ko >= "다" and ko < "라":
        return "다"
    elif ko >= "라" and ko < "마":
        return "라"
    elif ko >= "마" and ko < "바":
        return "마"
    elif ko >= "바" and ko < "사":
        return "바"
    elif ko >= "사" and ko < "아":
        return "사"
    elif ko >= "아" and ko < "자":
        return "아"
    elif ko >= "자" and ko < "차":
        return "자"
    elif ko >= "차" and ko < "카":
        return "차"
    elif ko >= "카" and ko < "타":
        return "카"
    elif ko >= "타" and ko < "파":
        return "타"
    elif ko >= "파" and ko < "하":
        return "파"
    else:
        return "하"

def classify(abs_path, script_name):
    # get file-list in specifed directory with absolute path string
    try:
        files = os.listdir(abs_path)
        print(files)
    except FileNotFoundError:
        print("Error - \'%s\' does not exist!" % abs_path)
        quit()

    print("Start classifying...\n")

    for f in files:
        af = os.path.join(abs_path, f)
        if os.path.isfile(af) and f != script_name and not f.startswith("."):

            # make src, dest string
            src_file = os.path.join(abs_path, f)
            if f[0].upper() >= "A" and f[0].upper() <= "Z":
                dest_dir = os.path.join(abs_path, f[0].upper())
            elif f[0] >= '0' and f[0] <= '9':
                dest_dir = os.path.join(abs_path, "0")
            elif f[0] >= "가" and f[0] <= "힣":
                dest_dir = os.path.join(abs_path, hangul_dir(f[0]))
            else:
                dest_dir = os.path.join(abs_path, "_")

            # make dest directory or use existing one
            try:
                os.mkdir(dest_dir)
                print("Directory \'%s\' is made.\n" % dest_dir)
            except FileExistsError:
                if not os.path.isdir(dest_dir):
                    print("Error - Destination directory \'%s\' exists but it is not a directory!\n" % dest_dir)
                    quit()
            
            # move file to dest directory
            shutil.move(src_file, dest_dir)
            print("\'%s\' has moved to directory \'%s\'.\n" % (f, dest_dir))
            
    print("Classifying is finished.\n")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        classify(os.getcwd(), sys.argv[0])
    elif len(sys.argv) >= 2:
        classify(os.path.abspath(sys.argv[1]), sys.argv[0])
