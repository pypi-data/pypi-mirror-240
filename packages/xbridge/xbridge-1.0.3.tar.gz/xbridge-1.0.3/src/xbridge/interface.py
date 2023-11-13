

        

from abc import ABC
from xbridge import xfmt
from xbridge.channel import Channel


class IInterface(ABC):
    obj_id: int = -1
    channel: Channel = None

    def bindChannel(self, ch: Channel):
        self.channel = ch
    
    # # send bytes of data
    # async def writeItem(self, item: xfmt.Any):
    #     # 将数据放入发送队列, 队列的长度是有限的, 所以这里可能要等待
    #     # write进度由yield返回
    #     await self.channel.write_queue.put(item)

    # async def readItem(self) -> xfmt.Any:
    #     # 委托transfer_task接收数据, 使用yield返回
    #     # 接收到的数据是一个完整的xfmt类型数据
    #     return await self.channel.read_queue.get()
    

class PrInterface(IInterface):
    def __init__(self, ch, obj_id: int) -> None:
        self.channel = ch
        self.obj_id = obj_id

class SrInterface(IInterface):

    def __init__(self, ch = None) -> None:
        self.obj_id = id(self)
        self.channel = ch

    async def call(self, func_name: str, params: xfmt.List):
        func = getattr(self, '_' + func_name)
        # print("parmas:", params)
        # print("local parmas:", params.localValue)
        return await func(*(params.value))
