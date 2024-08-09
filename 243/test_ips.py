import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

import pytest

from ips import ServiceIPRange, parse_ipv4_service_ranges, get_aws_service_range

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
# IP = IPv4Network("192.0.2.8")
IP = "54.244.46.0"


@pytest.fixture(scope="module")
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


def test_ServiceIPRange():
    an_ip_range = ServiceIPRange("AMAZON", "us-east-1", "52.96.245.0/24")
    assert (
        str(an_ip_range)
        == "52.96.245.0/24 is allocated to the AMAZON service in the us-east-1 region"
    )


def test_parser(json_file):
    # breakpoint()
    ip_ranges = parse_ipv4_service_ranges(source=json_file)
    aws_ranges = get_aws_service_range(IP, ip_ranges)
    an_ip_range = ServiceIPRange("AMAZON", "us-west-2", IPv4Network("54.244.0.0/16"))
    assert an_ip_range in aws_ranges

    with pytest.raises(ValueError, match="Address must be a valid IPv4 address"):
        aws_ranges = get_aws_service_range("IP", ip_ranges)
