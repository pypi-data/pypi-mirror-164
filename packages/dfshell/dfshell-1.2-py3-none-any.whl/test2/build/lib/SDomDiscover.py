#!/usr/bin/env python3

# Libraries
try:
    import requests
    import sys
    import re
    import whois
    import json
    import argparse
    import dns.zone
    import dns.resolver
    import pydig
    from time import sleep
    import os
    import urllib3
    import pdb
except:
    print(c.YELLOW + "\n[" + c.RED + "-" + c.YELLOW + "] ERROR requirements missing try to install the requirements: pip3 install -r requirements.txt" + c.END)
    sys.exit(0)

# Output Colours
class c:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'

# Banner Function
def banner():
    print(c.YELLOW + '                _____                   ')
    print('             .-"     "-.                ')
    print('            / o       o \               ')
    print('           /   \     /   \              ')
    print('          /     )-"-(     \             ')
    print('         /     ( 6 6 )     \            ')
    print('        /       \ " /       \           ')
    print('       /         )=(         \    - By D3Ext')
    print('      /   o   .--"-"--.   o   \         ')
    print('     /    I  /  -   -  \  I    \        ')
    print(' .--(    (_}y/\       /\y{_)    )--.    ')
    print('(    ".___l\/__\_____/__\/l___,"    )   ')
    print(' \                                 /    ')
    print('  "-._      o O o O o O o      _,-"     ')
    print('      `--Y--.___________.--Y--\'        ')
    print('         |==.___________.==|            ')
    print('         `==.___________.==\'           ' + c.END)

# Argument parser Function
def parseArgs():

    p = argparse.ArgumentParser(description="SDomDiscover - Stealthy subdomain finder and much more")
    p.add_argument("-d", "--domain", help="domain to search its subdomains", required=True)
    p.add_argument("-a", "--axfr", help="try a domain zone transfer attack", action='store_true', required=False)
    p.add_argument("-m", "--mail", help="try to enumerate mail servers", action='store_true', required=False)
    p.add_argument('-e', '--extra', help="look for extra dns information", action='store_true', required=False)
    p.add_argument("-n", "--nameservers", help="try to enumerate the name servers", action='store_true', required=False)
    p.add_argument("-i", "--ip", help="it reports the ip or ips of the domain", action='store_true', required=False)
    p.add_argument("-w", "--waf", help="discover the WAF of the domain main page", action='store_true', required=False)
    p.add_argument("-s", "--subtakeover", help="check if any of the subdomains are vulnerable to Subdomain Takeover", action='store_true', required=False)
    p.add_argument("-r", "--repos", help="try to discover valid repositories and s3 servers of the domain", action='store_true', required=False)
    p.add_argument('-6', '--ipv6', help="enumerate the ipv6 of the domain", action='store_true', required=False)
    p.add_argument('-t', '--token', help="api token of https://proxycrawl.com to crawl email accounts", required=False)
    p.add_argument("-o", "--output", help="file to store the scan output", required=False)
    p.add_argument("--osint", help="perform OSINT to find some valid accounts in different applications", action='store_true', required=False)
    p.add_argument("--all", help="perform all the enumeration at once", action='store_true', required=False)
    p.add_argument("--version", help="display the script version", action='store_true', required=False)

    return p.parse_args()

# Nameservers Function 
def ns_enum(domain):
    print(c.BLUE + "\n[" + c.END + c.GREEN + "+" + c.END + c.BLUE + "] Trying to discover valid name servers...\n" + c.END)
    sleep(0.2)

    """
    Query to get NS of the domain
    """

    data = pydig.query(domain, 'NS')

    if data:
        for ns in data:
            l = len(ns)
            ns = ns[:l-1]
            print(c.YELLOW + ns + c.END)
    else:
        print(c.YELLOW + "Unable to enumerate" + c.END)

# IPs discover Function
def ip_enum(domain):
    print(c.BLUE + "\n[" + c.END + c.GREEN + "+" + c.END + c.BLUE + "] Discovering IPs of the domain...\n" + c.END)
    sleep(0.2)

    """
    Query to get ips
    """

    data = pydig.query(domain, 'A')

    if data:
        for ip in data:
            print(c.YELLOW + ip + c.END)
    else:
        print(c.YELLOW + "Unable to enumerate" + c.END)

# Extra DNS info Function
def txt_enum(domain):
    print(c.BLUE + "\n[" + c.END + c.GREEN + "+" + c.END + c.BLUE + "] Enumerating extra DNS information...\n" + c.END)
    sleep(0.2)

    """
    Query to get extra info about the dns
    """

    data = pydig.query(domain, 'TXT')

    if data:
        for info in data:
            print(c.YELLOW + info + c.END)
    else:
        print(c.YELLOW + "Unable to enumerate" + c.END)

# Function to discover the IPv6 of the target
def ipv6_enum(domain):
    print(c.BLUE + "\n[" + c.END + c.GREEN + "+" + c.END + c.BLUE + "] Getting ipv6 of the domain...\n" + c.END)
    sleep(0.2)

    """
    Query to get ipv6
    """

    data = pydig.query(domain, 'AAAA')
    
    if data:
        for info in data:
            print(c.YELLOW + info + c.END)
    else:
        print(c.YELLOW + "Unable to enumerate" + c.END)

# Mail servers Function
def mail_enum(domain):
    print(c.BLUE + "\n[" + c.END + c.GREEN + "+" + c.END + c.BLUE + "] Finding valid mail servers...\n" + c.END)
    sleep(0.2)

    """
    Query to get mail servers
    """

    data = pydig.query(domain, 'MX')

    if data:
        for mail_output in data:
            mail_output = mail_output.split(' ')[1]
            l = len(mail_output)
            mail_servers = mail_output[:l-1]
            print(c.YELLOW + mail_servers + c.END)
    else:
        print(c.YELLOW + "Unable to enumerate" + c.END)

# Domain Zone Transfer Attack Function
def axfr(domain):
    print(c.BLUE + "\n[" + c.END + c.GREEN + "+" + c.END + c.BLUE + "] Starting Domain Zone Transfer attack...\n" + c.END)
    sleep(0.2)

    """
    Iterate through the name servers and try an AXFR attack on everyone
    """

    ns_answer = dns.resolver.resolve(domain, 'NS')
    for server in ns_answer:
        ip_answer = dns.resolver.resolve(server.target, 'A')
        for ip in ip_answer:
            try:
                zone = dns.zone.from_xfr(dns.query.xfr(str(ip), domain))
                for host in zone:
                    print(c.YELLOW + "Found Host: {}".format(host) + c.END)
            except Exception as e:
                print(c.YELLOW + "NS {} refused zone transfer!".format(server) + c.END)
                continue

# Modified function from https://github.com/Nefcore/CRLFsuite WAF detector script <3
def wafDetector(domain):
    
    """
    Get WAFs list in a file
    """

    r = requests.get("https://raw.githubusercontent.com/D3Ext/SDomDiscover/main/utils/wafsign.json")
    f = open('wafsign.json', 'w')
    f.write(r.text)
    f.close()

    with open('wafsign.json', 'r') as file:
        wafsigns = json.load(file)

    print(c.BLUE + "\n[" + c.END + c.GREEN + "+" + c.END + c.BLUE + "] Discovering active WAF on the main web page...\n" + c.END)
    sleep(1)
    
    """
    Payload to trigger the possible WAF
    """

    payload = "../../../../etc/passwd"

    try:

        """
        Check the domain and modify if neccessary 
        """

        if domain.endswith("/") and domain.startswith("https://"):
            response = requests.get(domain + payload, verify=False)

        elif domain.endswith("/") and not domain.startswith("https://"):
            response = requests.get('https://' + domain + payload, verify=False)

        elif not domain.endswith("/") and domain.startswith("https://"):
            response = requests.get(domain + '/' + payload, verify=False)
        
        elif not domain.endswith("/") and not domain.startswith("https://"):
            response = requests.get('https://' + domain + '/' + payload, verify=False)

    except:
        print(c.YELLOW + "An error has ocurred" + c.END)

        try:
            os.remove('wafsign.json')
        except:
            pass
    
        return None

    code = str(response.status_code)
    page = response.text
    headers = str(response.headers)
    cookie = str(response.cookies.get_dict())

    """
    Check if WAF has blocked the request
    """

    if int(code) >= 400:
        bmatch = [0, None]
        for wafname, wafsign in wafsigns.items():
            total_score = 0
            pSign = wafsign["page"]
            cSign = wafsign["code"]
            hSign = wafsign["headers"]
            ckSign = wafsign["cookie"]
            if pSign:
                if re.search(pSign, page, re.I):
                    total_score += 1
            if cSign:
                if re.search(cSign, code, re.I):
                    total_score += 0.5
            if hSign:
                if re.search(hSign, headers, re.I):
                    total_score += 1
            if ckSign:
                if re.search(ckSign, cookie, re.I):
                    total_score += 1
            if total_score > bmatch[0]:
                del bmatch[:]
                bmatch.extend([total_score, wafname])

        if bmatch[0] != 0:
            print(c.YELLOW + bmatch[1] + c.END)
        else:
            print(c.YELLOW + "WAF not detected or doesn't exists" + c.END)
    else:
        print(c.YELLOW + "An error has ocurred or unable to enumerate" + c.END)

    try:
        os.remove('wafsign.json')
    except:
        pass

# Use the token
def crawlMails(domain, api_token):

    print(c.BLUE + "\n[" + c.GREEN + "+" + c.BLUE + "] Crawling valid email accounts" + c.END)

    """
    Use the api of proxycrawl to with your token to get valid emails
    """

    api_url = f"""https://api.proxycrawl.com/leads?token={api_token}&domain={domain}"""

    r = requests.get(api_url)
    
    print()
    print(c.YELLOW + r.text + c.END)

# Function to check subdomain takeover
def subTakeover(all_subdomains):

    """
    Iterate through all the subdomains to check if anyone is vulnerable to subdomain takeover
    """
    
    vuln_counter = 0
    print(c.BLUE + "\n[" + c.GREEN + "+" + c.BLUE + "] Checking if any subdomain is vulnerable to takeover\n" + c.END)
    sleep(1)
    
    for subdom in all_subdomains:
        try:
            sleep(0.05)
            resquery = dns.resolver.resolve(subdom, 'CNAME')
            
            for resdata in resquery:
                resdata = (resdata.to_text())
                
                if subdom[-8:] in resdata:
                    r = requests.get("https://" + subdom, allow_redirects=False)
    
                    if r.status_code == 200:
                        vuln_counter += 1
                        print(c.YELLOW + subdom + " appears to be vulnerable" + c.END)

                else:
                    pass

        except:
            pass
    
    if vuln_counter <= 0:
        print(c.YELLOW + "Any subdomain is vulnerable" + c.END)

# Function to enumerate github and cloud
def cloudgitEnum(domain):

    print(c.BLUE + "\n[" + c.END + c.GREEN + "+" + c.END + c.BLUE + "] Finding valid git repositories or accounts\n" + c.END)

    """
    Check if an github account or a repositorythe same name exists 
    """

    r = requests.get("https://" + domain + "/.git")
    if r.status_code == 200 or r.status_code == 403 or r.status_code == 500:
        print(c.YELLOW + "Git repository found: https://" + domain + "/.git" + c.END)

    r = requests.get("https://github.com/" + domain.split(".")[0])
    if r.status_code == 200:
        print(c.YELLOW + "Github account found: https://github.com/" + domain.split(".")[0] + c.END)

    r = requests.get("https://gitlab.com/" + domain.split(".")[0])
    if r.status_code == 200:
        print(c.YELLOW + "Gitlab account found: https://gitlab.com/" + domain.split(".")[0] + c.END)

# Function to check valid accounts on different platforms
def osint(domain):
    
    print(c.BLUE + "\n[" + c.END + c.GREEN + "+" + c.END + c.BLUE + "] Searching valid accounts associated to the domain (social networks and more)\n" + c.END)
    
    """
    URLs array
    """

    osint_urls = ["https://twitter.com/{}","https://www.instagram.com/{}/","https://www.facebook.com/{}","https://pypi.org/user/{}","https://about.me/{}","https://www.airliners.net/user/{}/profile/photos","https://bitbucket.org/{}/","https://buymeacoff.ee/{}","https://www.chess.com/member/{}","https://www.clubhouse.com/@{}","https://dev.to/{}","https://www.dailymotion.com/{}","https://hub.docker.com/u/{}/","https://www.duolingo.com/profile/{}","https://www.fandom.com/u/{}","https://www.fiverr.com/{}","https://flipboard.com/@{}","https://www.freelancer.com/u/{}","http://en.gravatar.com/{}","https://hackerearth.com/@{}","https://hackerone.com/{}","https://imgur.com/user/{}","https://launchpad.net/~{}","https://leetcode.com/{}","https://medium.com/@{}","https://api.mojang.com/users/profiles/minecraft/{}","https://myspace.com/{}","https://notabug.org/{}","https://onlyfans.com/{}","https://pastebin.com/u/{}","https://www.patreon.com/{}","https://www.reddit.com/user/{}","https://www.snapchat.com/add/{}","https://sourceforge.net/u/{}","https://t.me/{}","https://tiktok.com/@{}","https://www.twitch.tv/{}","https://vsco.co/{}","https://vimeo.com/{}","https://www.virustotal.com/ui/users/{}/trusted_users"]

    valid_counter = 0

    for url in osint_urls:

        r = requests.get((url).format(domain.split(".")[0]), allow_redirects=True)

        if r.status_code == 200 and "not found" not in r.text and "Sorry, nobody" not in r.text and "Sorry, this" not in r.text and "Error 404" not in r.text and "doesn’t exist" not in r.text and "Page Not Found" not in r.text and "this page is not available" not in r.text:

            valid_counter += 1

            if valid_counter == 1:
                print(c.YELLOW + "Valid accounts" + c.END)
                print(c.YELLOW + "-------------" + c.END)

            print(c.YELLOW + (url).format(domain.split(".")[0]) + c.END)

    if valid_counter <= 0:
        print(c.YELLOW + "Any account found" + c.END)

# Main Domain Discoverer Function
def SDom(domain,filename):
    banner()
    print(c.BLUE + "\n[" + c.END + c.GREEN + "+" + c.END + c.BLUE + "] Discovering valid subdomains...\n" + c.END)
    sleep(0.1)

    """
    Get valid subdomains with a request to crt.sh
    """

    r = requests.get("https://crt.sh/?q=" + domain + "&output=json", timeout=30)
    formatted_json = json.dumps(json.loads(r.text), indent=4)
    domains = re.findall(r'"common_name": "(.*?)"', formatted_json)

    global doms
    doms = []

    raw_doms = sorted(set(domains))
    for dom in raw_doms:
        if dom.endswith(domain):
            doms.append(dom)

    if filename != None:
        f = open(filename, "a")
    
    if domains:

        """
        Iterate through the subdomains and check the lenght to print them in a table format
        """

        print(c.YELLOW + "+" + "-"*39 + "+")
        for value in doms:
            if value.endswith("." + domain):
    
                if len(value) >= 10 and len(value) <= 14:
                    l = len(value)
                    print("| " + value + "    \t\t\t|")
                    if filename != None:
                        f.write(value + "\n")

                if len(value) >= 15 and len(value) <= 19:
                    l = len(value)
                    print("| " + value + "\t\t\t|")
                    if filename != None:
                        f.write(value + "\n")

                if len(value) >= 20 and len(value) <= 24:
                    l = len(value)
                    print("| " + value + "   \t\t|")
                    if filename != None:
                        f.write(value + "\n")
    
                if len(value) >= 25 and len(value) <= 29:
                    l = len(value)
                    print("| " + value + "\t\t|")
                    if filename != None:
                        f.write(value + "\n")

        print("+" + "-"*39 + "+" + c.END)
        print(c.YELLOW + "\nTotal discovered sudomains: " + str(len(doms) - 1) + c.END)

        if filename != None:
            f.close()
            print(c.BLUE + "\n[" + c.GREEN + "+" + c.BLUE + "] Output stored in " + filename)
    else:
        print(c.YELLOW + "Any subdomains discovered through SSL transparency" + c.END)

# Program workflow starts here
if __name__ == '__main__':

    urllib3.disable_warnings()
    
    # If --version is passed
    if "--version" in sys.argv:
        print("\nSDomDiscover v1.0 - By D3Ext")
        print("Contact me: <d3ext@proton.me>\n")
        sys.exit(0)

    parse = parseArgs()

    # Check domain format
    if "." not in parse.domain:
        print(c.YELLOW + "\nInvalid domain format, example: domain.com\n" + c.END)
        sys.exit(0)

    # If --output is passed
    if parse.output:
        store_info=1
        filename = parse.output
    else:
        filename = None

    """
    If --all is passed do all enumeration processes
    """
    if parse.domain and parse.all:
        domain = parse.domain
        if domain.startswith('https://'):
            domain = domain.split('https://')[1]

        if domain.startswith('http://'):
            domain = domain.split('http://')[1]

        try:
            SDom(domain,filename)
            axfr(domain)
            mail_enum(domain)
            ns_enum(domain)
            ip_enum(domain)
            ipv6_enum(domain)
            txt_enum(domain)
            cloudgitEnum(domain)
            wafDetector(domain)
            subTakeover(doms)
            osint(domain)

            if parse.token:
                crawlMails(domain, parse.token)
            else:
                print(c.BLUE + "\n[" + c.GREEN + "-" + c.BLUE + "] No API token provided, skipping crawling" + c.END)

        except KeyboardInterrupt:
            sys.exit(c.RED + "\n[!] Interrupt handler received, exiting...\n" + c.END)

        sys.exit(0)

    """
    Enter in this part if the --all isn't passed
    """
    if parse.domain:

        domain = parse.domain

        if domain.startswith('https://'):
            domain = domain.split('https://')[1]

        if domain.startswith('http://'):
            domain = domain.split('http://')[1]
        
        try:
            SDom(domain,filename)
    
            """
            Check the passed arguments via command line
            """

            if parse.axfr:
                axfr(domain)
    
            if parse.mail:
                mail_enum(domain)

            if parse.nameservers:
                ns_enum(domain)

            if parse.ip:
                ip_enum(domain)

            if parse.ipv6:
                ipv6_enum(domain)

            if parse.extra:
                txt_enum(domain)

            if parse.repos:
                cloudgitEnum(domain)

            if parse.waf:
                wafDetector(domain)
    
            if parse.subtakeover:
                subTakeover(doms)

            if parse.osint:
                osint(domain)

            if parse.token:
                crawlMails(domain, parse.token)
    
        except KeyboardInterrupt:
            sys.exit(c.RED + "\n[!] Interrupt handler received, exiting...\n" + c.END)


