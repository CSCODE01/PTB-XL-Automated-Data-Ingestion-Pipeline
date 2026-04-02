import os
import requests
import zipfile
from tqdm import tqdm


def ingest_medical_data():
    zip_url = "https://physionet.org/static/published-projects/ptb-xl/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3.zip"
    file_name = "ptb_xl_dataset.zip"
    extract_folder = "PTB_XL_Clinical_Data"

    response = requests.get(zip_url, stream=True)

    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024 * 1024

        with open(file_name, 'wb') as file, tqdm(
                desc=file_name,
                total=total_size,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(block_size):
                file.write(data)
                bar.update(len(data))
    else:
        return

    os.makedirs(extract_folder, exist_ok=True)

    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)


if __name__ == "__main__":
    ingest_medical_data()