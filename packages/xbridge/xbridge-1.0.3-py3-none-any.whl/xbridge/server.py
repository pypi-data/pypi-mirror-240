

import asyncio
import contextlib
import socket
from typing import AsyncIterator

import netifaces
import qrcode
import websockets

from xbridge import bonjour
from xbridge.channel import WebsocketChannel
from xbridge.peer import IPeer, SrPeer


def get_ip():

    ip = '172.0.0.1'
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        return ip
    finally:
        s.close()

    # for interface_name in netifaces.interfaces():
    #     if interface_name.startswith('lo'):
    #         continue
    #     interface = netifaces.ifaddresses(
    #         interface_name).get(netifaces.AF_INET)
    #     if interface != None:
    #         for info in interface:
    #             return info['addr']


def create_session_handler(peer: SrPeer):
    
    async def handle_session(ws):
        print("session start...")
        ch = WebsocketChannel(ws)
        ch.registerService("", peer)
        await ch.waitStop()
        print("session exit")

    return handle_session


# start a server
@contextlib.asynccontextmanager
async def start(name: str, peer: SrPeer):
    ip = get_ip()
    try:
        async with websockets.serve(
            create_session_handler(peer),
            "0.0.0.0",
            compression=None,
            ssl=None
        ) as ws:
            print("ws server started")
        
            port: int = ws.sockets[0].getsockname()[1]

            # print("ws:", ws.sockets)
            info = bonjour.register_service(name, ip, port)
            name = info.name.split(".")[0]
            print("Server %s run on port %d" % (name, port))
            
            yield ip, port

    finally:
        print("ws server end")
