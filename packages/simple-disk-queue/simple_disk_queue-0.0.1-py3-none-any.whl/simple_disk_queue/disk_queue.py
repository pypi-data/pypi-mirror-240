import os
import random
from typing import Any, Callable, List, Optional, Tuple, Union
from collections import deque

from . import _utils
from .config import Config, get_default_config
from .rw_lock import FileLock, Timeout


class DiskQueue:
    def __init__(self, id:str, config:Config=None, overwrite=False,
                 timeout=20) -> None:
        if config is None:
            config = get_default_config()
        self.config = config

        self.queue_file = os.path.join(self.config.get_queue_location(), f"{id}.pkl")
        if overwrite:
            self.clear(id)

        self.timeout = timeout

    def __len__(self):
        with FileLock(self.queue_file, timeout=self.timeout):
            if not os.path.isfile(self.queue_file):
                _utils.to_pickle(deque(), self.queue_file)
            curr_queue = _utils.read_pickle(self.queue_file)
            return len(curr_queue)

    def __getitem__(self, idx):
        with FileLock(self.queue_file, timeout=self.timeout):
            if not os.path.isfile(self.queue_file):
                _utils.to_pickle(deque(), self.queue_file)
            curr_queue = _utils.read_pickle(self.queue_file)
            return curr_queue[idx]

    def add_task(self, func, *args, **kwargs):
        with FileLock(self.queue_file, timeout=self.timeout):
            if not os.path.isfile(self.queue_file):
                _utils.to_pickle(deque(), self.queue_file)
            curr_queue = _utils.read_pickle(self.queue_file)
            curr_queue.append((func, args, kwargs))
            _utils.to_pickle(curr_queue, self.queue_file)

    def get_task(self):
        job = None
        with FileLock(self.queue_file, timeout=self.timeout):
            curr_queue = _utils.read_pickle(self.queue_file)
            if len(curr_queue):
                job = curr_queue.popleft()
                _utils.to_pickle(curr_queue, self.queue_file)
        return job

    def shuffle(self):
        with FileLock(self.queue_file, timeout=self.timeout):
            curr_queue = _utils.read_pickle(self.queue_file)
            curr_queue = list(curr_queue)
            random.shuffle(curr_queue)
            curr_queue = deque(curr_queue)
            _utils.to_pickle(curr_queue, self.queue_file)

    @classmethod
    def run(cls, id:str, max_attempts:int=30, timeout:int=20):
        queue = cls(id, timeout=timeout)
        failed_cnt = 0
        while failed_cnt < max_attempts:
            job = queue.get_task()
            if job is None:
                break
            func, args, kwargs = job
            try:
                func(*args, **kwargs)
            except KeyboardInterrupt as err:
                raise err
            except Exception as err:
                failed_cnt += 1
                print(f"Job {func} {args} {kwargs} failed with error {err}")
                queue.add_task(func, *args, **kwargs)

    @classmethod
    def clear(cls, id:str):
        queue = cls(id)
        if not os.path.isfile(cls(id).queue_file):
            return
        with FileLock(queue.queue_file):
            os.remove(queue.queue_file)