#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
from sys import exit
from rich.console import Console
from json import dumps



__all__ = ["fetch_proxies", "fetch_proxies_list", "fetch_proxies_json"]



console = Console()
proxy_list = []
final_list=[]
ua = generate_user_agent(os=('mac', 'linux', 'win'))



def listTodict(final_list):
    global res_dct
    res_dct = []
    for proxy_port in final_list:
        _lst = proxy_port.split(':')
        dct = {
            "IP Address": _lst[0],
            "Port": _lst[1]
        }
        res_dct.append(dct)
    return res_dct


def iO_func(final_list, proxy_type, output_filename, output_format):
    try:
        _filename = f"{output_filename}_{proxy_type}.{output_format}"
        if output_format == "json":
            listTodict(final_list)
            with open(_filename, "w+") as handle:
                handle.write(dumps(res_dct))
        else:
            with open(_filename, "w+") as handle:
                for proxy in final_list:
                    handle.write(str(proxy) + "\n")
    except Exception as err:
        console.print("[" + "[red bold]Error[/red bold]" + "]" + f"[bold blink] {err}...![/bold blink]")
        exit(1)



def get_url(ua, URL):
    temp_list = []
    s = requests.Session()
    if len(URL) != 0:
        for url in URL:
            try:
                s.headers.update({
                            "user-agent": f"{ua}",
                            "Accept-Encoding": "*",
                            "Connection": "keep-alive"
                        })
                r = s.get(url)
                soup = BeautifulSoup(r.content, 'html5lib')
                for row in soup.table.find_all('tr')[1:]:
                    cols = row.find_all('td')
                    cols = [ele.text.strip() for ele in cols]
                    temp_list.append([ele for ele in cols if ele])
                for i in range(len(temp_list)):
                    proxy = f"{temp_list[i][0]}:{temp_list[i][1]}"
                    if proxy not in proxy_list:
                        proxy_list.append(proxy)
                return proxy_list
            except Exception as err:
                console.print("[" + "[red bold]Error[/red bold]" + "]" + f"[bold blink] {err}...![/bold blink]")
                exit(1)



def get_api(ua, api):
    temp_list = []
    try:
        s = requests.Session()
        s.headers.update({
                    "user-agent": f"{ua}",
                    "Accept-Encoding": "*",
                    "Connection": "keep-alive"
                        })
        r = s.get(api)
        temp_list = r.content.decode('utf-8').splitlines()
        for proxy in temp_list:
            if proxy not in proxy_list:
                proxy_list.append(proxy)
        return proxy_list
    except Exception as err:
        console.print("[" + "[red bold]Error[/red bold]" + "]" + f"[bold blink] {err}...![/bold blink]")
        exit(1)



def get_uniQ(proxy_list):
    if len(proxy_list) > 0:
        for proxy in proxy_list:
            if proxy not in final_list:
                final_list.append(proxy)
    return final_list


def get_http_https(ua):
    URL = [
    "https://sslproxies.org", 
    "https://hidemy.name/en/proxy-list/?type=hs&anon=234#list", 
    "https://hidemy.name/en/proxy-list/?type=hs&anon=234&start=64#list",
    "https://hidemy.name/en/proxy-list/?type=hs&anon=234&start=128#list"]
    api = "https://www.proxy-list.download/api/v1/get?type=https"
    
    get_url(ua, URL)
    get_api(ua, api)



def get_socks4(ua):
    URL = [
    "https://www.socks-proxy.net", 
    "https://hidemy.name/en/proxy-list/?type=4&anon=1234#list"]
    api = "https://www.proxy-list.download/api/v1/get?type=socks4"
    
    get_url(ua, URL)
    get_api(ua, api)



def get_socks5(ua):
    URL = ["https://hidemy.name/en/proxy-list/?type=5&anon=1234#list"]
    api = "https://www.proxy-list.download/api/v1/get?type=socks5"
    
    get_url(ua, URL)
    get_api(ua, api)


# ------------------------------------------------------------------------------------->
#############################################
# Functions for ProxyNinja-ng PyPi package  #
#############################################
# ------------------------------------------------------------------------------------->


# Function to get proxies and save them to a file.
def fetch_proxies(proxy_type, output_filename, output_format):
    _type = str(proxy_type)
    _filename = str(output_filename)
    _format = str(output_format)
    if proxy_type == "https":
        get_http_https(ua)
        get_uniQ(proxy_list)
        iO_func(final_list, _type, _filename, _format)
    elif proxy_type == "socks4":
        get_socks4(ua)
        get_uniQ(proxy_list)
        iO_func(final_list, _type, _filename, _format)
    elif proxy_type == "socks5":
        get_socks5(ua)
        get_uniQ(proxy_list)
        iO_func(final_list, _type, _filename, _format)
    else:
        exit(f" {proxy_type} is not a valid proxy type...!")


# Function to get proxies and returns a List (IP:Port).
def fetch_proxies_list(proxy_type):
    global proxies_list
    proxies_list = []
    _type = str(proxy_type)
    if _type == "https":
        get_http_https(ua)
        get_uniQ(proxy_list)
        proxies_list = final_list
        return proxies_list
    elif _type == "socks4":
        get_socks4(ua)
        get_uniQ(proxy_list)
        proxies_list = final_list
        return proxies_list
    elif _type == "socks5":
        get_socks5(ua)
        get_uniQ(proxy_list)
        proxies_list = final_list
        return proxies_list
    else:
        exit(f" {proxy_type} is not a valid proxy type...!")


# Function to get proxies and returns Json Object.
def fetch_proxies_json(proxy_type):
    global proxies_json
    proxies_json = []
    _type = str(proxy_type)
    if _type == "https":
        get_http_https(ua)
        get_uniQ(proxy_list)
        listTodict(final_list)
        proxies_json = dumps(res_dct, indent=4)
        return proxies_json
    elif _type == "socks4":
        get_socks4(ua)
        get_uniQ(proxy_list)
        listTodict(final_list)
        proxies_json = dumps(res_dct, indent=4)
        return proxies_json
    elif _type == "socks5":
        get_socks5(ua)
        get_uniQ(proxy_list)
        listTodict(final_list)
        proxies_json = dumps(res_dct, indent=4)
        return proxies_json
    else:
        exit(f" {proxy_type} is not a valid proxy type...!")