from . import mujoco_pb2

class MuJoCoRPCClient:
    def __init__(self, url: str) -> None:
        self.url = url

    class MjModel:
        def from_xml_path(file_path: str) -> int:
            m = mujoco_pb2.Id(value=3)
            return m.value
    
    def MjData(self, m: int) -> int:
        d = mujoco_pb2.Id(value=m+2)
        return d.value

    def mj_step(self, m: int, d: int) -> int:
        _m = mujoco_pb2.Id(value=m)
        _d = mujoco_pb2.Id(value=d)
        return 0

def connect(url: str):
    return MuJoCoRPCClient(url)

