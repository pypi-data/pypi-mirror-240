
from rich.console import Console
from rich.logging import RichHandler
from rich.text import Text
from rich.console import Console
from rich import inspect
from rich.table import Table
from rich import print
from rich.columns import Columns
from CPCReady import common as cm
from CPCReady import func_update as update

import sys
import os
import random
from CPCReady import __version__ as version

console = Console()


##
# Show banner dependencie model cpc
# @
# param cpc: Model CPC
##
def show(description=True):
    print()

    #     cpc = random.choice(cm.CPC_MODELS)
    #     if cpc == "6128":
    #         lineSize = 93
    #     elif cpc == "464":
    #         lineSize = 75
    #     elif cpc == "664":
    #         lineSize = 75

    #     Linea3 = description.ljust(lineSize - 1, " ")
    #     Linea1 = f"CPCReady v{version}".ljust(lineSize, " ")
    #     Linea2 = f"👉 https://cpcready.github.io/doc/".ljust(lineSize - 1, " ")

    #     CPC464 = f"""[bold white]{Linea1}[/]╔═╗╔═╗╔═╗ ┏┓┏┓┏┓ ┌─────────────┐  ON 🟢
    # [bold white]{Linea2}[/]║  ╠═╝║   ┃┃┣┓┃┃ │[red] ███ [green]███ [blue]███ [white]│
    # [bold white]{Linea3}[/]╚═╝╩  ╚═╝ ┗╋┗┛┗╋ └─────────────┘ COLOR"""

    #     CPC664 = f"""[bold white]{Linea1}[/]╔═╗╔═╗╔═╗ ┏┓┏┓┏┓ ┌─────────────┐  ON 🟢
    # [bold white]{Linea2}[/]║  ╠═╝║   ┣┓┣┓┃┃ │[red] ███ [green]███ [blue]███ [white]│
    # [bold white]{Linea3}[/]╚═╝╩  ╚═╝ ┗┛┗┛┗╋ └─────────────┘ COLOR"""

    #     CPC6128 = f"""[bold white]{Linea1}[/]┌─────────────┐  ENC.
    # [bold white]{Linea2}[/]│[red] ███ [green]███ [blue]███ [white]│  [green]▄▄▄[/green]
    # [bold white]{Linea3}[/]└─────────────┘"""
    check_version_local = update.check_version()
    if not check_version_local == "99.99.99":
        new_version = f"👋 New version {check_version_local} found. Please Upgrade.!!![/]"
    else:
        new_version = ""

    LOGOCPCREADY = f"""[bold white]╔═╗╔═╗╔═╗ ┌─────────────┐                                                            
[bold white]║  ╠═╝║   │[red] ███ [green]███ [blue]███ [white]│[bold white]                 {new_version}[/]
[bold white]╚═╝╩  ╚═╝ └─────────────┘
[bold yellow]Ready[/]
[bold yellow]█[/]                                                                                                   [bold green]v{version}"""

    BANNER = Table(show_header=False)

    # if cpc == "6128":
    #     BANNER.add_row(CPC6128)
    # elif cpc == "464":
    #     BANNER.add_row(CPC464)
    # elif cpc == "664":
    #     BANNER.add_row(CPC664)
    # else:
    #     cm.msgError("Model CPC not supported")
    #     sys.exit(1)

    BANNER.add_row(LOGOCPCREADY)
    console.print(BANNER)

    if description:
        print()
        print("[bold white]Github: [/]https://github.com/CPCReady/installer")
        print("[bold white]Docs  : [/]https://cpcready.github.io/doc/")
