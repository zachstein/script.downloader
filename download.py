import requests
import os
import time
from tqdm import tqdm

def download_file(url, output_folder):
    url = url.strip()
    file_name = os.path.basename(url)
    file_path = os.path.join(output_folder, file_name)

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors

        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 KB

        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=file_name)

        with open(file_path, 'wb') as f:
            for data in response.iter_content(block_size):
                f.write(data)
                progress_bar.update(len(data))

        progress_bar.close()

        return True

    except (requests.exceptions.RequestException, IOError):
        return False

def download_files(file_urls, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    warning_count = 0
    failed_urls = []

    print("\nDownlading Files...\n")

    for url in file_urls:
        success = download_file(url, output_folder)
        if not success:
            warning_count += 1
            failed_urls.append(url)

    print(f"\nDownload completed with [{warning_count}] warning(s).")

    if warning_count > 0:
        print("\nLinks that encountered errors:\n")
        for url in failed_urls:
            print(url, end='')

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    links_file_path = os.path.join(script_dir, "links.txt")
    output_folder = os.path.join(script_dir, "downloads")

    with open(links_file_path, "r") as links_file:
        file_urls = links_file.readlines()

    download_files(file_urls, output_folder)