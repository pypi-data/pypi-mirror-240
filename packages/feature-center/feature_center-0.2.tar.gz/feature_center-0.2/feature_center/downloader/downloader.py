#!/usr/bin/env python3
import os
import shlex
import logging
import subprocess
import requests
from urllib.parse import urlparse


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


class DownloaderError(Exception):
    """
    Downloader errors
    """
    def __init__(self, message, *args):
        super().__init__(message)
        self.args = args
        logger.error(message)

def extract_afs_server_path(afs_address):
    """
    提取afs地址中的server和path
    """
    parsed_url = urlparse(afs_address)
    afs_server = f"afs://{parsed_url.netloc}"
    afs_path = f"/{parsed_url.path.lstrip('/')}"
    if afs_path.startswith("//"):
        afs_path = afs_path.replace("//", "/", 1)
    return afs_server, afs_path

class Downloader:
    """
    数据下载器
    """
    def __init__(self, data_name, local_path="./", data_ugi="gunir_sata,gunir"):
        """
        init
        """
        self.data_name = data_name
        self.local_path = local_path
        self.data_ugi = data_ugi
        self._init_afs_ugi()
        self.get_afs_address()

    def _init_afs_ugi(self):
        """
        初始化并解析ugi
        """
        self.afs_address = ""
        self.afs_user = ""
        self.afs_pwd = ""
        self.afs_server = ""
        self.afs_path = ""
        if self.data_ugi and "," in self.data_ugi:
            self.afs_user = self.data_ugi.split(",")[0]
            self.afs_pwd = self.data_ugi.split(",")[1]

    def get_afs_address(self):
        """
        获取特征中心数据名称对应的afs地址
        """
        url = f"http://mlops.baidu-int.com:8528/superflow/api/GetSampleVersionAddress?version_name={self.data_name}%3FX-Mlops-Token%3D8aed0522-0187-429d-8a23-c213d1bc33d8&X-Mlops-Token=8aed0522-0187-429d-8a23-c213d1bc33d8"
        headers = {
            'user_name': 'chenxiaoyan07',
            'token': '1f76b81d-41f8-4dc1-8f7f-ea4478fee876',
            'rdw_auth_type': 'token',
            'Content-Type': 'application/json',
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise DownloaderError(f"Error: get data afs address failed, status_code: {response.status_code}")

        try:
            json_data = response.json()
        except ValueError as e:
            raise DownloaderError(f"Error: get data afs address failed, error: {str(e)}")

        afs_address = json_data.get("data")
        if not afs_address:
            raise DownloaderError(f"Error: get data afs address failed, data_name: {self.data_name}")
        self.afs_server, self.afs_path = extract_afs_server_path(afs_address)
        
        return afs_address
    
    def download(self):
        """
        下载数据到本地
        """
        father_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        afsshell_path = os.path.join(father_path, "afsshell", "bin", "afsshell")

        cmd = f"{afsshell_path} --username={self.afs_user} --password={self.afs_pwd} " \
              f"get {self.afs_server}/{self.afs_path}/{self.data_name} {self.local_path}"

        cmd = shlex.split(cmd)
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            raise DownloaderError(f"Error: data download failed, data_name: {self.data_name}")

    
    def get_data_obj(self):
        """
        读取数据到内存
        """
        # 判断指定路径下是否已经包含数据
        file_path = os.path.join(self.local_path, self.data_name)
        if not os.path.exists(file_path):
            self.download()
        
        try:
            return open(file_path, 'r')
        except FileNotFoundError:
            raise DownloaderError(f"Error: The file {file_path} was not found.")
        except OSError as e:
            raise DownloaderError(f"Error: An OS error occurred while opening the file {file_path}: {e}")
        

if __name__ == "__main__":
    # downloader = Downloader("aurora_ctr_NNCTR_TEST_chenxiaoyan07_20231109_135", ".", "gunir_sata,gunir")
    downloader = Downloader("aurora_sat_RAS_TRAIN_TOP30_chenxiaoyan07_20231108_102", ".", "gunir_sata,gunir")
    # downloader = Downloader("3", ".", "gunir_sata,gunir")
    afs_address = downloader.get_afs_address()
    downloader.download()
