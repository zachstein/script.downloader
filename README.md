# URL File List Downloader

This Python script allows you to download files from a list of URLs and save them locally with progress tracking and error handling.

## Features

- Downloads files from a list of URLs specified in a text file.
- Supports various file formats (e.g., images, videos, documents).
- Displays progress bars for each file being downloaded.
- Handles errors gracefully and reports the count of warnings at the end.
- Provides a summary of the download process, including the number of warnings and the list of URLs that encountered errors.

## Prerequisites

- Python 3.x
- `requests` library
- `tqdm` library

## Installation

1. Clone the repository or download the script file.

2. Install the required libraries by running the following command:

```bash
pip install requests tqdm
```
## Usage

1. Create a text file named `links.txt` in the same directory as the script.

2. Add the URLs of the files you want to download to `links.txt`, with each URL on a separate line.

3. Open a terminal or command prompt and navigate to the directory where the script is located.

4. Run the script using the following command:

```python
python file_downloader.py
```
5. The script will start downloading the files from the specified URLs and display progress bars for each file.

6. Once the download process is complete, the script will report the count of warnings (if any) and list the URLs that encountered errors.

7. The downloaded files will be saved in a directory named `downloads` in the same location as the script.

## Configuration

- If you want to change the name of the input file containing the URLs, modify the `links_file_path` variable in the script.

- If you want to change the name of the output directory where the downloaded files are saved, modify the `output_folder` variable in the script.

## Error Handling

- If a file fails to download due to an error (e.g., invalid URL, network issues), the script will skip that file and continue with the next one.

- The script keeps track of the count of warnings (i.e., files that encountered errors) and reports it at the end of the download process.

- The script also provides a list of the URLs that encountered errors, making it easier to identify and troubleshoot any issues.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.
