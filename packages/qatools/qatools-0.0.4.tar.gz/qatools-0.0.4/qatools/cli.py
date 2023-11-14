#!/usr/bin/python
""  # line:6
import argparse  # line:7
import os  # line:8
import sys  # line:9

from qatools import __description__  # line:11
from qatools import __version__  # line:12
from qatools.adb import decryption  # line:13
from qatools.adb import get_adb_path  # line:14
from qatools.adb import get_host_ip  # line:15

adb = get_adb_path()  # line:17


def main():  # line:20
    OOOO0OOO00OO00000 = argparse.ArgumentParser(description=__description__)  # line:21
    OOOO0OOO00OO00000.add_argument(
        "-v", "--version", dest="version", action="store_true", help="show version"
    )  # line:25
    OO00OOO000OOO0000 = OOOO0OOO00OO00000.add_subparsers(
        help="sub-command help"
    )  # line:26
    OO00OOO000OOO0000.add_parser("clear", help="clear app cache data).")  # line:27
    OO00OOO000OOO0000.add_parser(
        "adb", help="complete adb debugging capability."
    )  # line:28
    OO00OOO000OOO0000.add_parser(
        "remote", help="open Android device remote debugging port(5555)."
    )  # line:31
    OO00OOO000OOO0000.add_parser(
        "proxy", help=f"enable device global proxy({get_host_ip()}:8888)."
    )  # line:34
    OO00OOO000OOO0000.add_parser(
        "unproxy", help=f"disable device global proxy."
    )  # line:35
    if len(sys.argv) == 1:  # line:37
        OOOO0OOO00OO00000.print_help()  # line:39
        sys.exit(0)  # line:40
    elif len(sys.argv) == 2:  # line:41
        if sys.argv[1] in ["-v", "--version"]:  # line:43
            print(f"{__version__}")  # line:45
        elif sys.argv[1] == "remote":  # line:47
            os.system(f"{adb} tcpip 5555")  # line:49
        elif sys.argv[1] == "proxy":  # line:51
            os.system(
                f'{adb} {decryption(b"c2hlbGwgc2V0dGluZ3MgcHV0IGdsb2JhbCBodHRwX3Byb3h5")} {get_host_ip()}:8888'
            )  # line:55
        elif sys.argv[1] == "unproxy":  # line:57
            os.system(
                f'{adb} {decryption(b"c2hlbGwgc2V0dGluZ3MgcHV0IGdsb2JhbCBodHRwX3Byb3h5IDow")}'
            )  # line:61
        elif sys.argv[1] == "adb":  # line:63
            os.system(f"{adb}")  # line:65
        elif sys.argv[1] in ["-h", "--help"]:  # line:67
            OOOO0OOO00OO00000.print_help()  # line:69
        else:  # line:70
            OOOO0OOO00OO00000.print_help()  # line:71
        sys.exit(0)  # line:72
    elif sys.argv[1] == "adb":  # line:74
        del sys.argv[0:2]  # line:75
        OOO0OOOOOOOOO0000 = " ".join(
            [str(OO000OO0000O0O0O0) for OO000OO0000O0O0O0 in sys.argv]
        )  # line:76
        os.system(f"{adb} {OOO0OOOOOOOOO0000}")  # line:77
        sys.exit(0)  # line:78
    elif len(sys.argv) == 3:  # line:80
        if sys.argv[1] == "clear":  # line:81
            os.system(f"{adb} shell pm clear {sys.argv[2]}")  # line:82
        sys.exit(0)  # line:83
    OOO0OOOOOOOOO0000 = OOOO0OOO00OO00000.parse_args()  # line:85
    if OOO0OOOOOOOOO0000.version:  # line:87
        print(f"{__version__}")  # line:88
        sys.exit(0)  # line:89
