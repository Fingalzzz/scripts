# -*- coding: utf-8 -*-
"""
    proxy.lambda_function
    ~~~~~~~~~~~~~~~~~~~~~

    Transfer simple clash subscription link into various versions.

    :copyright: (c) 2020 by Fingalzzz.
    :license: MIT, see LICENSE for more details.
"""
import urllib3
import certifi
import yaml
import json


def lambda_handler(event, context):
    link = 'https://example.link'
    config = get_config(link)

    if event.get('targetApp') == 'CFW':
        new_config = to_cfw(config)
    else:
        new_config = to_shadowsoks(config)
    return {'statusCode': 200, 'body': new_config}


def get_config(link):
    """get config from subscription link

    @param link: subscription link of clash
    @type  link: String

    @return: clash config
    @rtype : Dict
    """
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
                               ca_certs=certifi.where())
    response = http.request('GET', link)
    config = yaml.safe_load(response.data.decode('utf-8'))
    return config


def to_cfw(config):
    """Transfer clash config into Clash for Windows version.
    Add several advanced features such as ad-block, proxy groups.

    @param config: clash config 
    @type  detial: Dict

    @return: advanced CFW config file
    @rtype : Yaml
    """
    # TODO: add rules and proxy groups <22-09-20, Fingalzzz> #
    # https://github.com/lhie1/Rules/blob/master/Clash/Rule.yaml
    return config


def to_shadowsoks(config: dict) -> str:
    """Transfer clash config into Shadowsocks version

    @param config: clash config 
    @type  detial: Dict

    @return: Shadowsocks config file
    @rtype : String in json format
    """
    shadowsocks_proxies: [dict] = list()
    # Based on https://github.com/shadowsocks/shadowsocks-android/blob/master/.github/doc-json.md
    # SS json file format: [{"remarks", "server", "server_port", "password", "method"}, {...}]
    proxies: [dict] = config['proxies']
    proxy: dict
    for proxy in proxies:
        new_proxy = {
            'remarks': proxy['name'],
            'server': proxy['server'],
            'server_port': proxy['port'],
            'password': proxy['password'],
            'method': proxy['cipher'],
            'route': 'bypass-lan-china',
            'proxy_apps': {
                'enabled': True,
                'bypass': True
            }
        }
        shadowsocks_proxies.append(new_proxy)

    shadowsocks_config: str = json.dumps(shadowsocks_proxies)
    return shadowsocks_config
