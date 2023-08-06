"""Zoom File"""
import requests
from requests.exceptions import HTTPError

URL = "https://assets.zoom.us/docs/ipranges/Zoom.txt"

def get_zoom_ips(url:str = URL, cert = True) -> list:
    """_summary_

    Args:
        url (str, optional): Used if URL ever changes. Defaults to most recent txt published file
        cert (bool, str, optional): Used to specfy verification in RestAPI Call. Defaults to True.

    Raises:
        HTTPError: _description_

    Returns:
        list: List of Zoom IP Networks
    """
    params = ""
    req = requests.get(url=url, params=params,verify=cert)
    if req.status_code != 200:
        raise HTTPError()
    return req.text.split()
