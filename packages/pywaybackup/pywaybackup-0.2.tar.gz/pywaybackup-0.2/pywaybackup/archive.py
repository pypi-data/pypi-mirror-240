import requests
import datetime
import os
import magic
from pprint import pprint
import time
import pathlib

def print_result(result_list):
    print("")
    if not result_list:
        print("No snapshots found")
    else:
        pprint(result_list)
        print(f"\n-----> {len(result_list)} snapshots listed")

# create filelist
def query_list(url: str, range: int):
    print("\nQuerying snapshots...")
    range = datetime.datetime.now().year - range
    range = "&from=" + str(range)
    cdxQuery = f"https://web.archive.org/cdx/search/xd?output=json&url=*.{url}/*{range}&fl=timestamp,original&filter=!statuscode:200"
    cdxResult_json = requests.get(cdxQuery).json()[1:] # first line is fieldlist, so remove it [timestamp, original]
    cdxResult_list = [{"timestamp": snapshot[0], "url": snapshot[1]} for snapshot in cdxResult_json]
    print(f"\n-----> {len(cdxResult_list)} snapshots found")
    return cdxResult_list





# create folders for output
def create_outputdir(output):
    pathlib.Path(output).mkdir(parents=True, exist_ok=True)





def split_url(url):
    """
    Split  url into domain, subdir and file.
    If no file is present, the filename will be index.html
    """
    domain = url.split("//")[-1].split("/")[0]
    subdir = "/".join(url.split("//")[-1].split("/")[1:-1])
    filename = url.split("/")[-1] or "index.html"
    return domain, subdir, filename





def remove_empty_folders(path, remove_root=True):
    print("")
    print("Removing empty output folders...")
    print("")
    count = 0
    if not os.path.isdir(path):
        return
    # remove empty subfolders
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                try:
                    os.rmdir(dir_path)
                    print(f"-----> {dir_path}")
                    count += 1
                except OSError as e:
                    print(f"Error removing {dir_path}: {e}")
    # remove empty root folder
    if remove_root and not os.listdir(path):
        try:
            os.rmdir(path)
            print(f"-----> {path}")
            count += 1
        except OSError as e:
            print(f"Error removing {path}: {e}")
    if count == 0:
        print("No empty folders found")





# example download: http://web.archive.org/web/20190815104545id_/https://www.google.com/
# example url: https://www.google.com/
# example timestamp: 20190815104545
def download_full(download_list, output):
    print("\nDownloading snapshots...")
    headers = {'User-Agent': 'Mozilla/5.0'}
    for snapshot in download_list:
        timestamp, url = snapshot["timestamp"], snapshot["url"]
        download_url = f"http://web.archive.org/web/{timestamp}id_/{url}"
        domain, subdir, filename = split_url(url)
        download_dir = os.path.join(output, domain, timestamp, subdir)
        create_outputdir(download_dir)
        filepath = os.path.join(download_dir, filename)
        max_retries = 2
        for i in range(max_retries):
            try:
                data = requests.get(download_url, headers=headers)
                with open(filepath, 'wb') as file:
                    file.write(data.content)
                print(f"Download: {url} -> {filepath}")
                break
            except:
                print(f"Download failed, retrying ({i+1}/{max_retries})...")
                time.sleep(1)
        else:
            print(f"Download failed, skipping {url}")





# scan output folder and guess mimetype for each file
# if add file extension if not present
def guess_mimetype(filepath):
    print("")
    print("Guessing mimetypes for unknown files...")
    if not os.path.isfile(filepath):
        return
    for dirs, files in os.walk(filepath):
        for file in files:
            filepath = os.path.join(dirs, file)
            file_extension = filepath.split(".")[-1]
            if file_extension == "":
                file_extension = magic.from_file(filepath, mime=True)
                file_extension = "." + file_extension.split("/")[-1]
                new_filepath = filepath + file_extension
                os.rename(filepath, new_filepath)
                print(f"Rename: {filepath} -> {new_filepath}")
    