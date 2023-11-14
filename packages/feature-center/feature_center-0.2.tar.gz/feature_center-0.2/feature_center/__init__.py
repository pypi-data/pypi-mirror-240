from feature_center.downloader.downloader import Downloader, DownloaderError, logger

def load_data(data_name, local_path="."):
    data_loader = Downloader(data_name, local_path, "gunir_sata,gunir")
    return data_loader.get_data_obj()

def download(data_name, local_path="."):
    data_loader = Downloader(data_name, local_path)
    data_loader.download()
    return 
