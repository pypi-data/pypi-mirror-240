

from abc import abstractmethod
import os
from typing import Any, Coroutine, List

from xbridge.cmd.file_stream import FileWriterStream

from xbridge import xfmt
# from xbridge.file_stream import FileReaderStream, FileWriterStream
from xbridge.interface import PrInterface, SrInterface


class IFileReceiver():
    @abstractmethod
    async def askSend(self, files: List[str]) -> List[bool]:
        pass

    @abstractmethod
    async def send(self, files: List[xfmt.Stream]) -> None:
        pass


class PrFileReceiver(PrInterface, IFileReceiver):

    def __init__(self, interface: PrInterface) -> None:
        super().__init__(interface.channel, interface.obj_id)

    async def askSend(self, files: List[str]) -> List[bool]:
        call = xfmt.Call.of(self.obj_id, self.askSend.__name__, [files])
        ret = await self.channel.callFuncList(call)
        return [False if v == 0 else True for v in ret.localValue]
    
    async def send(self, files: List[xfmt.Stream]) -> None:
        call = xfmt.Call.of(self.obj_id, self.send.__name__, [files])
        await self.channel.callFunc(call)
    

class _SrFileReceiver(SrInterface, IFileReceiver):
    async def _askSend(self, files: xfmt.List) -> xfmt.List:
        ret = await self.askSend(files.localValue)
        return xfmt.List(ret)

    async def _send(self, files: xfmt.List) -> xfmt.End:
        await self.send(files.localValue)
        return xfmt.End()


class SrFileReceiver(_SrFileReceiver):
    async def askSend(self, files: List[str]) -> List[bool]:
        for f in files:
            print("ask send %s --- Accepct? " % f, True)
        return [True for s in files]
    
    async def send(self, files: List[xfmt.Stream]) -> None:
        # print("handle send...", files)
        for f in files:
            # print("will receive file", f)
            os.mkdir('__temp')
            s = FileWriterStream(f, '__temp/' + f.name)
            self.channel.registerStream(s)



