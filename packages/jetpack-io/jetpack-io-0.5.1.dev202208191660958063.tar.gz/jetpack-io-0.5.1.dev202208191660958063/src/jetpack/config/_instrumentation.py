from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional
import uuid

import schedule

from jetpack.config import _k8s
from jetpack.proto.runtime.v1alpha1 import remote_pb2

if TYPE_CHECKING:
    from jetpack.core._jetroutine import Jetroutine
    from jetpack.core._task import Task


class Tracer:
    """
    Base class for Jetpack instrumentation.
    Inspired by https://github.com/python-trio/trio/blob/6754c74eacfad9cc5c92d5c24727a2f3b620624e/docs/source/tutorial/tasks-with-trace.py
    """

    def task_created(self, task: Task) -> None:
        """Called when runtime client creates new task"""

    def result_returned(self, task_id: uuid.UUID, result: remote_pb2.Result) -> None:
        """Called when runtime client has received new result"""

    def scheduled_task_created(self, task: Task) -> None:
        """Called when new scheduled task created"""

    def cronjob_loaded(
        self, name: str, repeat_pattern: Optional[schedule.Job], schedule: Optional[str]
    ) -> None:
        """Called when a cronjob has been loaded by SDK"""

    def jetroutine_called(self, func: Jetroutine[Any]) -> None:
        """Called when a jetroutine (@jetroutine or @cron) is executed."""


class LocalTracer(Tracer):
    def task_created(self, task: Task) -> None:
        print(f"Task {task.id} created. Symbol name = {task.symbol_name()}")

    def result_returned(self, task_id: uuid.UUID, result: remote_pb2.Result) -> None:
        print(f"Result for task {task_id} returned.")

    def scheduled_task_created(self, task: Task) -> None:
        print(
            f"Task {task.id} scheduled for time = {task.target_time}. Symbol name = {task.symbol_name()}"
        )

    def cronjob_loaded(
        self, name: str, repeat_pattern: Optional[schedule.Job], schedule: Optional[str]
    ) -> None:
        if repeat_pattern:
            print(f"Cronjob {name} loaded. Repeat pattern = {repeat_pattern}")
        if schedule:
            print(f"Cronjob {name} loaded. Repeat pattern = {schedule}")

    def jetroutine_called(self, jetroutine: Jetroutine[Any]) -> None:
        print(f'Jetroutine "{jetroutine._name()}" was called')


_tracer = Tracer()
_local_tracer = LocalTracer()


# TODO(Landau): Allow custom tracer
def get_tracer() -> Tracer:
    if _k8s.is_in_cluster():
        return _tracer
    return _local_tracer
