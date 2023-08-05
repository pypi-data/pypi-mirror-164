from __future__ import annotations

import base64
import time
from typing import TYPE_CHECKING, Dict
import uuid

from jetpack.config import _symbols
from jetpack.core._jetroutine import Jetroutine
from jetpack.proto.runtime.v1alpha1 import remote_pb2, remote_pb2_grpc

if TYPE_CHECKING:
    from jetpack.runtime._client import RuntimeClient


class LocalStub(remote_pb2_grpc.RemoteExecutorStub):
    task_results: Dict[str, remote_pb2.Result] = {}
    scheduled_tasks: Dict[str, remote_pb2.Task] = {}

    def __init__(self, client: RuntimeClient) -> None:
        self.client = client

    async def CreateTask(
        self,
        request: remote_pb2.CreateTaskRequest,
    ) -> remote_pb2.CreateTaskResponse:
        task_id = str(uuid.uuid4())
        if request.task.target_time.seconds <= time.time():
            func = _symbols.get_symbol_table().get_registered_symbols()[
                request.task.qualified_symbol
            ]
            await Jetroutine(self.client, func)._exec(
                task_id,
                request.task.encoded_args,
            )
        else:
            self.scheduled_tasks[task_id] = request.task
        return remote_pb2.CreateTaskResponse(
            task_id=task_id,
        )

    async def CancelTask(
        self,
        request: remote_pb2.CancelTaskRequest,
    ) -> remote_pb2.CancelTaskResponse:
        del self.scheduled_tasks[str(request.task_id)]
        return remote_pb2.CancelTaskResponse(success=True)

    async def PostResult(
        self,
        request: remote_pb2.PostResultRequest,
    ) -> remote_pb2.PostResultResponse:
        self.task_results[request.exec_id] = request.result
        return remote_pb2.PostResultResponse()

    async def WaitForResult(
        self,
        request: remote_pb2.WaitForResultRequest,
    ) -> remote_pb2.WaitForResultResponse:
        return remote_pb2.WaitForResultResponse(
            result=self.task_results[request.task_id],
        )

    async def RegisterApp(
        self,
        request: remote_pb2.RegisterAppRequest,
    ) -> remote_pb2.RegisterAppResponse:
        """
        This is a no op. To fetch cronjobs you can use cron.get_jobs()
        In the future we may want to simulate the registration process
        """
        return remote_pb2.RegisterAppResponse()

    async def GetTask(
        self,
        request: remote_pb2.GetTaskRequest,
    ) -> remote_pb2.GetTaskResponse:
        return remote_pb2.GetTaskResponse(
            encoded_args=self.scheduled_tasks[request.task_id].encoded_args
        )
