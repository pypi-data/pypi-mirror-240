
import asyncio
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, AsyncIterator, Coroutine, Dict, List, Tuple

from xbridge import xfmt
from xbridge.cipher import Cipher
from xbridge.config import Config
from xbridge.interface import IInterface, PrInterface, SrInterface
from xbridge.rsa_key import RSAKey
from xbridge.xbridge import ProtocalInfo


@dataclass
class HelloMsg(xfmt.Any):
    preferLocales: List[str] = None
    #// 支持的locale列表
    pubkey: bytes = None
    #// 公钥
    random: bytes = None
    #// 随机数16B + 时间戳
    sign: bytes = None

    def toBytes(self) -> bytes:
        return xfmt.Dict(vars(self)).toBytes()
    
    def getLocalValue(self) -> Any:
        return self
    
    @staticmethod
    def fromXDict(xdict: xfmt.Dict):
        preferLocales = xdict.value['preferLocales'].localValue
        pubkey = xdict.value['pubkey'].localValue
        sign = xdict.value['sign'].localValue
        random = xdict.value['random'].localValue
        return HelloMsg(preferLocales, pubkey, random, sign)
    
    @staticmethod
    def fromBytes(data: bytes) -> Tuple['HelloMsg', int]:
        xdict, used = xfmt.Dict.fromBytes(data)   
        return HelloMsg.fromXDict(xdict), used


@dataclass
class HelloReplyMsg(xfmt.Any):
    locale: str = None
    #// 将会使用的locale
    pubkey: bytes = None
    #// 公钥
    random: bytes = None
    #// 随机数 16B + 时间戳
    sign: bytes = None
    #// 随机数的签名, 为了证明公钥是自己的
    aesKey: bytes = None
    #// 用对方公钥加密的AES key
    aesIV: bytes = None

    def toBytes(self) -> bytes:
        # dict = vars(self)
        # dict['__class__'] = self.__class__.__name__
        return xfmt.Dict(vars(self)).toBytes()
    
    @staticmethod
    def fromXDict(xdict: xfmt.Dict) -> 'HelloReplyMsg':
        locale = xdict.value['locale'].localValue
        pubkey = xdict.value['pubkey'].localValue
        random = xdict.value['random'].localValue
        sign = xdict.value['sign'].localValue
        aesKey = xdict.value['aesKey'].localValue
        aesIV = xdict.value['aesIV'].localValue
        return HelloReplyMsg(locale, pubkey, random, sign, aesKey, aesIV )

    @staticmethod
    def fromBytes(data: bytes) -> Tuple['HelloReplyMsg', int]:      
        xdict, used = xfmt.Dict.fromBytes(data)  
        return HelloReplyMsg.fromXDict(xdict), used

# class Stream:
#     id: int = None
#     size: int = None
#     offset: int = None

class IPeer:

    @abstractmethod
    async def checkVersion(self, versions: List[int]) -> int:
        pass

    @abstractmethod
    async def handShake(self, version: int, info: HelloMsg) -> HelloReplyMsg:
        pass

    @abstractmethod
    async def restoreStream(self, id: int, offset: int) -> bool:
        pass

    # notify connection will close
    @abstractmethod
    async def close(self) -> bool:
        pass

    @abstractmethod
    async def getService(self, name: str) -> IInterface:
        pass


class PrPeer(PrInterface, IPeer):

    async def checkVersion(self, versions: List[int]) -> int:
        call = xfmt.Call.of(self.obj_id, self.checkVersion.__name__, [versions])
        ret = await self.channel.callFuncNumber(call)
        return ret.localValue

    async def handShake(self, version: int, info: HelloMsg) -> HelloReplyMsg:
        call = xfmt.Call.of(self.obj_id, self.handShake.__name__, [version, info])
        ret = await self.channel.callFuncDict(call)
        return HelloReplyMsg.fromXDict(ret)
    
    async def restoreStream(self, id: xfmt.Number, offset: xfmt.Number) -> bool:
        call = xfmt.Call.of(self.obj_id, self.restoreStream.__name__, [id, offset])
        ret = await self.channel.callFuncU8(call)
        return ret.value != 0
    
    async def close(self) -> bool:
        call = xfmt.Call.of(self.obj_id, self.close.__name__, [])
        ret = await self.channel.callFuncU8(call)
        return ret.value != 0
    
    async def getService(self, name: str) -> IInterface:
        call = xfmt.Call.of(self.obj_id, self.getService.__name__, [name])
        ret = await self.channel.callFuncNumber(call)
        return PrInterface(self.channel, ret.localValue)


class _SrPeer(SrInterface, IPeer):

    def __init__(self, config: Config, ch=None) -> None:
        super().__init__(ch)
        self.config = config
   
    async def _checkVersion(self, versions: xfmt.List) -> xfmt.Number:
        ret = await self.checkVersion(versions.localValue)
        return xfmt.Number.of(ret)

    async def _handShake(self, version: xfmt.Number, info: xfmt.Dict) -> HelloReplyMsg:
        return await self.handShake(version.localValue, HelloMsg.fromXDict(info))

    async def _restoreStream(self, id: xfmt.Number, offset: xfmt.Number) -> xfmt.U8:
        ret = await self.restoreStream(id.localValue, offset.localValue)
        return xfmt.U8(1 if ret else 0)

    async def _close(self) -> bool:
        ret = await self.close()
        return xfmt.U8(1 if ret else 0)
    
    async def _getService(self, name: xfmt.Str) -> IInterface:
        return await self.getService(name.localValue)


class SrPeer(_SrPeer):

    async def checkVersion(self, versions: List[int]) -> int:
        chooseVersion = 0 # not support
        versions.sort()
        for v in versions:
            if v in ProtocalInfo.supportVersions:
                chooseVersion = v
        return chooseVersion
    
    async def handShake(self, version: int, info: HelloMsg) -> HelloReplyMsg:

        # check version support?
        if version not in ProtocalInfo.supportVersions:
            raise ValueError("protocal version %d is not supported. only supports %s", version, ProtocalInfo.supportVersions)

        # print('handShake info', info)
        # print('handShake info type', type(info))
        # print('handShake info pubkey', type(info.pubkey))
        peerRSA = RSAKey.fromBytes(None, info.pubkey)

        # 1. get peer id and check permission
        peerid = peerRSA.pubkey_hash
        # if not permission.allowConnect(peerid):
        #     raise ValueError("No permission to connect from %s" % peerid)

        # 2. verify signature in hello msg
        if not peerRSA.verify(info.random, info.sign):
            raise ValueError("Failed to verify peer rsa pubkey")

        # 3. create random and sign
        rsa = RSAKey.load(self.config.dir)
        random = Cipher.random()
        sign =rsa.sign(random)

        # 4. create aes key
        cipher = Cipher.new()
        ekey = peerRSA.encrypt(cipher.key)
        eiv = peerRSA.encrypt(cipher.iv)

        # 5. setup aes cipher to current channel???
        self.channel.next_cipher = cipher

        return HelloReplyMsg(info.preferLocales[0], rsa.pubkey_bytes, random, sign, ekey, eiv )
    
    async def restoreStream(self, id: int, offset: int) -> bool:
        return True
    
    async def close(self) -> bool:
        print("🌈 waiting for receive all pending data")
        while len(self.channel.pending_streams) > 0:
            await asyncio.sleep(0.2)
        # await asyncio.sleep(1)
        return True