import sys
import csv
import subprocess
from optparse import OptionParser


def main():
    parser = OptionParser()
    parser.add_option("-d", "--domain", help="The name of host you want to scan")
    (option, args) = parser.parse_args()
    domain = option.domain
    if not domain:
        print("domain is required")
        sys.exit(2)
    else:
        cmd = f"host -a {domain} | awk 'NR==10, NR==$NF' >> ~/{domain}.csv"
        data = subprocess.call([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        print(f"Please find the generated file at ~/{domain}.csv")


if __name__ == "__main__":
    main()
