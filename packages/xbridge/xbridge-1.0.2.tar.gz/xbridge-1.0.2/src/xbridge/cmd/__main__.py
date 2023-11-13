
import asyncio
import logging
import os
import sys
import uuid
from typing import Any, Coroutine, List

import pkg_resources
import qrcode
from FileReceiver import IFileReceiver, PrFileReceiver, SrFileReceiver
from file_stream import FileReaderStream

import xbridge
from xbridge import bonjour
from xbridge.config import Config
from xbridge.interface import IInterface
from xbridge.peer import IPeer, SrPeer
from xbridge.progress_bar import TranferBar
from xbridge.xfmt import StreamData

from xbridge.log import logger

# logging.basicConfig(level=logging.DEBUG)
# FILES_FLAG = '--with-files'
# logger.setLevel(logging.DEBUG)


class MyServicePeer(SrPeer):

    async def getService(self, name: str) -> IInterface:
        print("try get service of: ", name)
        if name == IFileReceiver.__name__:
            return SrFileReceiver(self.channel)
        raise ValueError("service not found!")


async def start_service(name: str):
    config = Config()
    peer = MyServicePeer(config)
    async with xbridge.start(name, peer) as (ip, port):

        # show qrcode
        qr = qrcode.QRCode()
        qr.border = 1
        qr.add_data("%s:%d" % (ip, port))
        qr.print_ascii(invert=True)
        await asyncio.Future()  # run forever


async def ask_send_files(service_name, files: List[str]):
    config = Config()
    async with xbridge.connect(service_name, config) as peer:
        # got handshaked peer
        print("got handshaked peer")
        obj = await peer.getService(IFileReceiver.__name__)
        fileReceiver = PrFileReceiver(obj)
        accepts = await fileReceiver.askSend(files)
        # print('accepts', accepts)
        for f, ok in zip(files, accepts):
            # print(f, ok)
            if ok:
                stream = FileReaderStream(f)
                await fileReceiver.send([stream])
                await peer.channel.sendStream(stream)
    

def cmd(args: List[str]):
    argslen = len(args)
    # print("arg len = %d, args:" % argslen, args)
    # no params
    if argslen == 0 or args[0] == '-h' or args[0] == '--help':
        version = pkg_resources.require("xbridge")[0].version
        print("xbridge v%s" % version)

        print('\nStart service:')
        print('\txbridge [-c <config>] <server>')
        print('\nClient:')
        print('  Discover services nearby:')
        print('\txbridge -d')
        print('  Get Service info:')
        print('\txbridge <server> info')
        print('  Normoal Request:')
        print('\txbridge [-c <config>] <server> request <action> [<params...> [ --with-files <files...> ]]')
        print('  Send/Get/List file:')
        print('\txbridge [-c <config>] <server> send/get/ls [<files...>]')
        print('  Continue Session:')
        print('\txbridge [-c <config>] <server> session <id> <msgtype> [ <params...> [ --with-files <files...> ]')
        return
    
    # just discover

    if args[0] == '-d' or args[0] == 'discover':
        bonjour.discover_service()
        return

    # got config

    if args[0] == '-c':
        config_dir = args[1]
        args = args[2:]
    else:
        config_dir = os.path.join(os.environ['HOME'], '.xbridge')

    if not os.path.exists(config_dir):
        os.makedirs(config_dir, 0o755)
    elif not os.path.isdir(config_dir):
        raise Exception("Config dir %s is not a dir!" % config_dir)
    Config.config_dir = config_dir
    

    # got service name

    service_name = args[0]
    args = args[1:]

    # start service

    subcmd = args[0]

    print("subcmd: ", subcmd)

    if subcmd == 'start':
        # start
        # server.start_service(service_name, config_dir, config_dir)
        
        try:
            asyncio.run(start_service(service_name))
            # except KeyboardInterrupt:
            #     print("keyboard interrupt!")
            # except Exception as e:
            #     print("Server exception: ", e)
        finally:
            print("server end")
        return


    # got session id
    if args[0] == 'resume':
        session_id = args[1]
        args = args[2:]
    else:
        session_id = str(uuid.uuid1())

    subcmd = args[0]

    # handle request

    # service_url = xbridge.client.get_service_url(service_name)
    
    if subcmd == 'info':
        # info
        args = ['request', 'info']

    if subcmd == 'actions':
        args = ['request', 'get_actions']
        
    if subcmd == 'trust':
        # trust
        newArgs = ['request', 'trust']
        newArgs.extend(args[1:])
        args = newArgs
        # print("args:", args)

    elif subcmd == 'send':
        files = args[1:]
        try:
            asyncio.run(ask_send_files(service_name, files))
        finally:
            print("send finished")
        return
    
    elif subcmd == 'get':
        # get <files...>
        newArgs = ['request', AvailableActions.GetFiles]
        newArgs.extend(args[1:])
        args = newArgs
    elif subcmd == 'ls':
        # ls <files...>
        newArgs = ['request', AvailableActions.ListFiles]
        newArgs.extend(args[1:])
        args = newArgs

    # basic invoke request
    # <msg_type> [<action>] [<params...>] [--with-files <files...>]  
    # print(args)
    msg_type = args[0]
    action = ''
    if msg_type == 'request':
        params_index = 2
        try:
            action = args[1]
        except:
            pass
    else:
        params_index = 1

    try:
        dash_index = args.index(FILES_FLAG)
        params = args[params_index:dash_index]
        files = args[dash_index+1:]
    except:
        params = args[params_index:]
        files = []
        
    # print("action:", action)
    msg = NormalMsg(MsgType(msg_type), session_id, '', action, params, files)
    print('req:', msg.toPrettyString())
    # client.request(service_name, msg, handle_reply)

      
        


if __name__ == '__main__':
    args = sys.argv[1:]
    cmd(args)
