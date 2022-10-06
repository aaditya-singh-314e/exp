import os
import time
import signal
import subprocess
from pathlib import Path
from functools import partial
from datetime import datetime

import toml
from rich import print as rprint
from watchdog.tricks import Trick
from watchdog.observers import Observer
from watchdog.utils.process_watcher import ProcessWatcher


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class AutoRestartTrick(Trick):

    """Starts a long-running subprocess and restarts it on matched events.
    The command parameter is a list of command arguments, such as
    `['bin/myserver', '-c', 'etc/myconfig.ini']`.
    Call `start()` after creating the Trick. Call `stop()` when stopping
    the process.
    """

    def __init__(
        self,
        command,
        patterns=None,
        ignore_patterns=None,
        ignore_directories=False,
        stop_signal=signal.SIGINT,
        kill_after=10,
    ):
        super().__init__(
            patterns=patterns,
            ignore_patterns=ignore_patterns,
            ignore_directories=ignore_directories,
        )
        self.command = command
        self.stop_signal = stop_signal
        self.kill_after = kill_after

        self.process = None
        self.process_watcher = None

    def start(self, src_path):
        # windows doesn't have setsid
        command = self.command[:]
        command.append(src_path)
        self.process = subprocess.Popen(command, preexec_fn=getattr(os, "setsid", None))

        _prompt = partial(self._prompt, src_path=src_path)
        self.process_watcher = ProcessWatcher(self.process, _prompt)
        self.process_watcher.start()

    def _prompt(self, src_path):
        datefmt = "%Y-%m-%d %H:%M:%S"
        now = datetime.now()
        now_str = datetime.strftime(now, datefmt)

        rprint(f"{now_str} [green] ✅ Build successful {src_path}!")

    def stop(self):
        if self.process is None:
            return

        if self.process_watcher is not None:
            self.process_watcher.stop()
            self.process_watcher = None

        def kill_process(stop_signal):
            if hasattr(os, "getpgid") and hasattr(os, "killpg"):
                os.killpg(os.getpgid(self.process.pid), stop_signal)
            else:
                os.kill(self.process.pid, self.stop_signal)

        try:
            kill_process(self.stop_signal)
        except OSError:
            # Process is already gone
            pass
        else:
            kill_time = time.time() + self.kill_after
            while time.time() < kill_time:
                if self.process.poll() is not None:
                    break
                time.sleep(0.25)
            else:
                try:
                    kill_process(9)
                except OSError:
                    # Process is already gone
                    pass
        self.process = None

    def on_closed(self, event):
        clear_screen()
        src_path = event.src_path
        self._restart(src_path)

    def _restart(self, src_path):
        self.stop()
        self.start(src_path)


if __name__ == "__main__":

    config_path = Path('config.toml')
    with open(config_path, 'r') as f:
        data = toml.load(config_path)
    
    assert(data.get('jupyter', None))
    assert(data['jupyter'].get('path', None))
    assert(data.get('jupytext', None))
    assert(data['jupytext'].get('path', None))

    print(data)

    path = "."

    event_handler1 = AutoRestartTrick(
        command=[
            data['jupytext']['path'],
            "--to",
            "py:percent",
        ],
        patterns=["notebooks/*/*.ipynb"],
        ignore_patterns=[
            "notebooks/*/*.py",
            "notebooks/*/*.md",
            "notebooks/*/*.png",
            "notebooks/*/*.jpeg",
        ],
    )

    event_handler2 = AutoRestartTrick(
        command=[
            data['jupyter']['path'],
            'nbconvert',
            "--to",
            "markdown",
        ],
        patterns=["notebooks/*/*.ipynb"],
        ignore_patterns=[
            "notebooks/*/*.py",
            "notebooks/*/*.md",
            "notebooks/*/*.png",
            "notebooks/*/*.jpeg",
        ],
    )

    # Initialize Observer
    observer = Observer()
    observer.schedule(event_handler1, path, recursive=True)
    observer.schedule(event_handler2, path, recursive=True)

    # Start the observer
    observer.start()
    try:
        while True:
            # Set the thread sleep time
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
