

import contextlib
from typing import AsyncIterator, Optional, Tuple
from xbridge import bonjour
from xbridge.channel import WebsocketChannel
from xbridge.cipher import Cipher
from xbridge.config import Config
from xbridge.peer import HelloMsg, IPeer, PrPeer
import websockets
from xbridge.rsa_key import RSAKey
from xbridge.xbridge import ProtocalInfo


def get_service_ip_port(service_name: str) -> Optional[Tuple[str, str]]:
    print("search service %s" % service_name)
    info = bonjour.get_service_info(service_name)
    if info is None:
        print("can't find service %s" % service_name)
        return None
    return bonjour.get_ip_port(info)
    # print("service address: %s%d" % ('ws://' + ip + ':', port))

    # return (ip, port)


def get_service_url(service_name: str):
    url = 'ws://'
    name_arr = service_name.split(':')
    if len(name_arr) >= 2:
        url += service_name
    else:
        (ip, port) = get_service_ip_port(service_name)
        url += ('%s:%d' % (ip, port))

    print('url: ', url)

    return url

@contextlib.asynccontextmanager
async def connect(name: str, config: Config) -> AsyncIterator[PrPeer]:
    url = get_service_url(name)

    async with websockets.connect(url, compression=None, ssl=None) as websocket:

        try:
            print("session start...")

            ch = WebsocketChannel(websocket)
            peer = PrPeer(ch, 0)

            version = await peer.checkVersion(ProtocalInfo.supportVersions)
            print("remote xbridge version: ", version)

            rsa = RSAKey.load(config.dir)
            random = Cipher.random()
            sign = rsa.sign(random)
            
            hello = HelloMsg(config.preferLocales, rsa.pubkey_bytes, random, sign)
            # print("hello", hello)
            ret = await peer.handShake(version, hello)
            # print('ret', ret)

            iv = rsa.decrypt(ret.aesIV)
            key = rsa.decrypt(ret.aesKey)

            cipher = Cipher(key, iv)
            ch.cipher = cipher

            print('handshake ok')
            
            yield peer
            await peer.close()


        finally:
            print("will close socket")
            await websocket.close()
            print("session end!")

