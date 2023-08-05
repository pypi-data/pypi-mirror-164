"""Python wrapper for Hashicorp's Terraform pre-built binary."""

import os
import platform
import stat
import urllib.request
import zipfile
from os.path import join

TERRAFORM_NULL_PROVIDER_VERSION = "2.0.2"


def download(version=TERRAFORM_NULL_PROVIDER_VERSION):
    platform_name = platform.system().lower()
    'https://releases.hashicorp.com/terraform-provider-vsphere/2.0.2/' \
    'terraform-provider-vsphere_2.0.2_linux_amd64.zip'
    base_url = f"https://releases.hashicorp.com/terraform-provider-vsphere/" \
               f"{version}"
    file_name = f"terraform-provider-vsphere_{version}_{platform_name}" \
                f"_amd64.zip"
    download_url = f"{base_url}/{file_name}"
    download_directory = "downloads"
    extract_directory = "lib"
    target_file = join(download_directory, file_name)

    os.makedirs(download_directory, exist_ok=True)
    os.makedirs(extract_directory, exist_ok=True)

    urllib.request.urlretrieve(download_url, target_file)

    with zipfile.ZipFile(target_file) as terraform_zip_archive:
        terraform_zip_archive.extractall(extract_directory)

    executable_path = join(extract_directory,
                           f"terraform-provider-vsphere_v{version}_x5")
    executable_stat = os.stat(executable_path)
    os.chmod(executable_path, executable_stat.st_mode | stat.S_IEXEC)

