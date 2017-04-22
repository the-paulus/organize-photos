#!/usr/bin/python

# Requirements exifread
# pip install exifread

from datetime import date, datetime, time
import exifread
import filecmp
import getopt
import magic
import os
import shutil
import sys

def destination_file_directory(file, directory):
    try:
        image = open(file, 'rb')
        exif = exifread.process_file(image, stop_tag='EXIF DateTimeOriginal')
        datetimeoriginal = exif['EXIF DateTimeOriginal'].values
        dateparts = datetimeoriginal.split(" ")[0].split(":")
        return os.path.join(directory, dateparts[0], dateparts[1], dateparts[2], os.path.basename(file))
    except (IOError, os.error) as why:
        raise

def main(src_path, dst_path, verbose):
    sep = os.path.sep
    vmsg = ""

    for root, subdirs, files in os.walk(src_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if "image" in magic.from_file(file_path, mime=True):
                    destination_file_path = destination_file_directory(file_path, dst_path)
                    destination_dir_path = os.path.dirname(destination_file_path)
                    if os.path.exists(destination_dir_path) is not True:
                        os.makedirs(destination_dir_path)

                    try:
                        if os.path.islink(file_path):
                            file_path = os.readlink(file_path)

                        vmsg = "Copying: " + file_path

                        if os.path.exists(destination_file_path) == True:
                            if filecmp.cmp(file_path, destination_file_path) == False:
                                tmp = destination_file_path.split(".")
                                tmp[-2] = tmp[-2] + "-" + datetime.now().strftime("%Y%m%d%H%M%S")
                                destination_file_path = ".".join(tmp)
                            else:
                                print(file_path + " and " + destination_file_path + " are the same file. Skipping...")
                                continue

                        vmsg += " -> " + destination_file_path

                        shutil.copy2(file_path, destination_file_path)

                        if verbose == True:
                            print(vmsg)
                    except (IOError, os.error) as why:
                        print(why)
            except Exception:
                pass

if __name__ == "__main__":
    src = ""
    dst = ""
    verbose = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:d:vh", ["src=", "dst="])
    except getopt.GetoptError:
        print(sys.argv[0] + "-s <source_dir> -d <destination_dir>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-s", "--source_dir"):
            src = arg
        elif opt in ("-d", "--destination_dir"):
            dst = arg
        elif opt in ("-v", "--verbose"):
            verbose = True
        elif opt in ("-h", "--help"):
            print("usage: " + sys.argv[0] + "-s|--src=<source_directory> -d|--dst=<destination_directory>")

    main(src, dst, verbose)
