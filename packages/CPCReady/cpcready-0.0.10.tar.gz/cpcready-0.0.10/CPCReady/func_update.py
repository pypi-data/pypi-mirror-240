
import os
import requests
from packaging import version
from CPCReady import common as cm
from rich.console import Console
import re
import subprocess
import logging
from CPCReady import __version__
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)
from distutils.version import LooseVersion

console = Console()

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def lastVersion(module):
    pypi_url = 'https://pypi.org/pypi'
    url = f'{pypi_url}/{module}/json'
    try:
        respuesta = requests.get(url, verify=False)
        respuesta.raise_for_status()

        # Extrae y devuelve la última versión
        last_Version = respuesta.json()['info']['version']
        return last_Version
    except requests.exceptions.RequestException as e:
        return "0"


##
# upgrade version
#
# @param check: if true only check / if false upgrade version
##

def check_version():
    github_version = lastVersion("cpcready")
    install_version = __version__

    v1 = LooseVersion(install_version)
    v2 = LooseVersion(github_version)

    if v2 > v1:
        return github_version
    else:
        return "99.99.99"


##
# check is string version format X.X.X
#
# @param version: version
##

# def is_version_format(version):
#     patron = r"^\d+\.\d+\.\d+$"
#     if re.match(patron, version):
#         return True
#     else:
#         return False


##
# check upgrade version
#
# @param version_install: version instalada en el sistema
# @param version_repo: version del repositorio
# @param out: generate template directory
##

# def check_upgrade(version_repo):
#     if os.path.exists(os.getenv("CPCREADY") + "/RELEASE"):
#         with open(os.getenv("CPCREADY") + "/RELEASE", "r") as archivo:
#             version_install = archivo.read()
#             v1 = version.parse(version_install)
#             v2 = version.parse(version_repo)

#             if v2 > v1:
#                 print(f"[bold yellow] New version ({version_repo}) of CPCready. Please Upgrade.[/]")
#                 return True
#     else:
#         return


##
# Get latest release
##

# def get_latest_release():
#     url = f"https://api.github.com/repos/cpcready/installer/releases/latest"
#     headers = {}
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         data = response.json()
#         return data.get("name")
#     else:
#         return "0"


# ##
# # Get install release
# ##

# def get_install_release():
#     RELEASE = os.getenv("CPCREADY") + "/RELEASE"
#     if os.path.exists(RELEASE):
#         with open(os.getenv("CPCREADY") + "/RELEASE", "r") as archivo:
#             version_install = archivo.read()
#             return version_install
#     else:
#         return "NONE"


# def version(check=True):
#     # github_version = get_latest_release().replace("Release ","")
#     # install_version= get_install_release()

#     # if not is_version_format(github_version):
#     #     if check == False:
#     #         print()
#     #         cm.msgWarning("It is not possible to recover the last published version.")
#     #     return "99.99.99"
#     # if not is_version_format(install_version):
#     #     if check == False:
#     #         print()
#     #         cm.msgWarning("It is not possible to recover the last install version.")
#     #     return "99.99.99"

#     # v1 = LooseVersion(install_version)
#     # v2 = LooseVersion(github_version)

#     # if check == True:
#     #     if v2 > v1 :
#     #         return github_version
#     #     else:
#     #         return False
#     # else:
#     if check_version() != "99.99.99":
#         SETUP = os.getenv("CPCREADY") + "/setup.sh"
#         cmd = [SETUP, "upgrade"]

#         proceso = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
#         for linea in proceso.stdout:
#             print(linea, end="")

#         proceso.wait()
#         codigo_salida = proceso.returncode
#         if codigo_salida != 0:
#             print()
#             cm.msgError("Updating the version of CPCReady.")
#     else:
#         cm.msgCustom("UPDGRADE", " CPCReady is updated.", "green")
