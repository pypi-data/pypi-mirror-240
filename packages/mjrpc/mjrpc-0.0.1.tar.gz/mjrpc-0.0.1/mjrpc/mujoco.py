import grpc
from concurrent import futures
from . import mujoco_pb2
from . import mujoco_pb2_grpc

# Client part
class MjModelClass:
    def __init__(self, client):
        self.client = client

    def from_xml_path(self, file_path: str) -> int:
        path = mujoco_pb2.String(value=file_path)
        m = self.client.stub.MjModel_from_xml_path(path)
        return m.value

class MuJoCoRPCClient:
    def __init__(self, url: str = "localhost:50051"):
        self.url = url
        self.channel = grpc.insecure_channel(url)
        self.stub = mujoco_pb2_grpc.mujocoStub(self.channel)
        self.MjModel = MjModelClass(self)
    
    def MjData(self, m: int) -> int:
        m = mujoco_pb2.Id(value=m)
        d = self.stub.MjData(m)
        return d.value

    def mj_step(self, m: int, d: int) -> int:
        _m = mujoco_pb2.Id(value=m)
        _d = mujoco_pb2.Id(value=d)
        _mj_step_msg = mujoco_pb2.mj_step_msg(m=_m, d=_d)

        err = self.stub.mj_step(_mj_step_msg)
        return err.value

def connect(url: str):
    return MuJoCoRPCClient(url)


# Server part
class MuJoCoRPCServer(mujoco_pb2_grpc.mujocoServicer):
    def __init__(self, port: str):
        self.mujoco = __import__('mujoco')
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        self.port = port
        self._ms = dict() # Dictionary of models
        self._ds = dict() # Dictionary of datas
        mujoco_pb2_grpc.add_mujocoServicer_to_server(self, self.server)
        self.server.add_insecure_port("[::]:" + port)
        self.server.start()
        print("MuJoCo RPC server started, listening on " + port)
        self.server.wait_for_termination() # Improve how we will deal with this

    def load_model_from_xml_path(self, path):
        print(f'load_model_from_xml_path: {path}')
        _mid = len(self._ms)
        self._ms[_mid] = self.mujoco.MjModel.from_xml_path(path)
        return _mid

    def new_MjData(self, m):
        _did = len(self._ds)
        self._ds[_did] = self.mujoco.MjData(m)
        return _did

    def MjModel_from_xml_path(self, request, context):
        _mid = self.load_model_from_xml_path(request.value)
        mid = mujoco_pb2.Id(value=_mid)
        return mid
    
    def MjData(self, request, context):
        _mid = request.value
        m = self._ms[_mid]
        _did = self.new_MjData(m)
        did = mujoco_pb2.Id(value=_did)
        return did

    def mj_step(self, request, context):
        _mid = request.m.value
        _did = request.d.value
        m = self._ms[_mid]
        d = self._ds[_did]
        self.mujoco.mj_step(m,d)
        print(f'Running ({_mid}, {_did}): {d.time}')
        err = mujoco_pb2.ErrorCode(value=0)
        return err

def serve(port: str = "50051"):
    return MuJoCoRPCServer(port)