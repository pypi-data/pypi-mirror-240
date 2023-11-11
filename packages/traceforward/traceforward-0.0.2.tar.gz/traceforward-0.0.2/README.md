# Traceforward

Forward Networks utility that enhances traceroute experience, extending original traceroute output
with useful information from Forward.

The tool expects Forward Server data to be present in configuration file:
```shell
➜  cat ~/.traceforward/traceForwardConfig.ini
[FORWARD_SERVER]
url = <FORWARD_SERVER_URL>
username = <USERNAME>
password = <USERNAME>
network_id = <NETWORK_ID>
```
If this file is not present, for example during the first run, the tool will
prompt for the information and create config folder and file.

## For developers

- To test from local folder:
```shell
# Move to 'src' folder:
cd src
# Run traceforward as module:
 python3 -m traceforward --help
```
 - Build and test in virtualenv:
```shell
# build 
python3 -m build
# create a test venv
python3 -m venv .env/fresh-install-test
# activate
. .env/fresh-install-test/bin/activate
# install:
pip install dist/traceforward-0.0.1-py3-none-any.whl
# run from cli:
traceforward --help
```
