#!/user/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import socket

def getIP(domain):
    """
    This method returns the first IP address string
    that responds as the given domain name
    """
    try:
        return socket.gethostbyname(domain)
    except Exception:
        return False

def getIPx(domain):
    """
    This method returns an array containing
    one or more IP address strings that respond
    as the given domain name
    """
    try:
        return list(set(socket.gethostbyname_ex(domain)[2]))
    except Exception:
        return False
#
def getHost(ip):
    """
    This method returns the 'True Host' name for a
    given IP address
    """
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return False
#
def getAlias(domain):
    """
    This method returns an array containing
    a list of aliases for the given domain
    """
    try:
        data = socket.gethostbyname_ex(domain)
        return list(data[1])
    except Exception:
        return False

def launch_dns_ip_resolver(ip_or_domain):
    functions = {
        'IP': {'function': getIP, 'result': ''},
        'IPx': {'function': getIPx, 'result': ''},
        'Host': {'function': getHost, 'result': ''},
        'Alias': {'function': getAlias, 'result': ''}
    }

    return {
        k:v['function'](ip_or_domain) for k,v in functions.items()
    }

def launch_reverse_ip_resolver(ip):
    return getHost(ip)
