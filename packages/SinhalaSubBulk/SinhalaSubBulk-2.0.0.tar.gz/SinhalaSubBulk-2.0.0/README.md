# SinhalaSubBulk
A Simple Python library for Download Bulk of Sinhala Subtitles

## Installation
To install, run the following command:
```bash
python3 pip install SinhalaSubBulk
```

## To Download Subtitle Bulk
```python
import SinhalaSubBulk

bulk_url = ''# example
download_path = 'Downloads' # Folder Name

SinhalaSubBulk.download(bulk_url, download_path)
```
### Or
```python
from SinhalaSubBulk import download

bulk_url = ''# example
download_path = 'Downloads' # Folder Name

download(bulk_url, download_path)
```

## For More Details
How to use this program
```python
import SinhalaSubBulk
print(SinhalaSubBulk.HELP)
```
## About Me
About me and this program
```python
import SinhalaSubBulk
print(SinhalaSubBulk.ABOUTME)
```