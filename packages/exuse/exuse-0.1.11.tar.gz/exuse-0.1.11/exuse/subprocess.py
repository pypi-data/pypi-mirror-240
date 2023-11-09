import os
import subprocess


def os_system(cmd: str, working_dir: str = None, logging=True, exitable=True):
    if working_dir:
        cmd = f"cd {working_dir} && {cmd}"
    if not logging:
        cmd = f"{cmd} > /dev/null 2>&1"
    code = os.system(cmd)
    if code != 0 and exitable:
        exit(code=code)
    return code


def run_ordered_commands(*commands, **kwargs):
    """
    按顺序在子进程中执行命令。

    Args:
      - `skip_failed`: 某条命令执行错误时是否跳过它继续执行后续命令。默认 `False`。
    """
    skip_failed = kwargs.get("skip_failed", False)
    for command in commands:
        process = subprocess.run(command, shell=True)
        if skip_failed:
            continue
        if process.returncode != 0:
            return False
    return True
