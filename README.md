# 🫀 PTB-XL ECG Data Ingestor

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Data Source](https://img.shields.io/badge/source-PhysioNet-red)

## 📖 Overview
The **PTB-XL ECG Data Ingestor** is a streamlined, automated Python pipeline designed to acquire and extract the PTB-XL clinical electrocardiography dataset. By handling streamed downloads and automated unzipping, this script ensures a reproducible and memory-efficient data setup for deep learning, AI research, and clinical data science environments.

## ✨ Key Features
* **Memory-Safe Streaming:** Downloads the massive dataset in 1MB chunks to prevent RAM overload and system crashes.
* **Live Progress Tracking:** Utilizes `tqdm` to display a highly responsive, visual progress bar detailing download speed, completion percentage, and ETA.
* **Automated Extraction:** Seamlessly decompresses the downloaded `.zip` archive into a dedicated, structured directory (`PTB_XL_Clinical_Data`).
* **Error Resilience:** Validates HTTP status responses before initiating the data transfer to ensure source availability.

## ⚙️ Prerequisites
Ensure you have Python installed on your system. You will need to install the required dependencies:

```bash
pip install requests tqdm
