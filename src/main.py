import subprocess
import sys
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
        subdomains = [
            'www',
            'mail',
            'autodiscover',
            'lyncdiscover',
            'sip',
            'enterpriseregistration',
            'enterpriseenrollment',
            '_sipfederationtls._tcp',
            '_sip._tls',
        ]
        print(f"Running queries for {domain}")
        cmd = f"host -a {domain} | grep -v 'Received'| awk 'NR==10, NR==$NF' > ~/{domain}.csv"
        subprocess.call([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        for subdomain in subdomains:
            print(f"Running queries for {subdomain}.{domain}")
            cmd = f"host -a {subdomain}.{domain} |  grep -v 'Received'| grep -v 'Trying' | grep -v 'ANSWER SECTION'| grep -v 'QUESTION SECTION' | grep -v 'HEADER' | grep -v 'ANY' | grep -v 'flags: qr rd' >> ~/{domain}.csv"
            subprocess.call([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        print(f"Opening the the generated file at ~/{domain}.csv")
        cmd = f"open ~/{domain}.csv"
        subprocess.call([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)


if __name__ == "__main__":
    main()
