import requests

IPINFO_URL = "http://ipinfo.io/{ip}/json"


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
    parse the json response returning the country code of the IP"""
    resp = requests.get(IPINFO_URL.format(ip=ip_address))
    resp.raise_for_status()
    data = resp.json()
    return data["country"]
