import argparse
import json
from typing import Dict, Tuple, Optional, List
import requests
from traceforward.config import get_config_file_data
from traceforward.utils.helpers import \
    print_blue,\
    conditional_extend_or_append,\
    Action


try:
    requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]
except Exception:
    pass


SERVER_ENDPOINT = "{url}/api/networks/{network_id}/detailed-trace-route"
NETWORKS_ENDPOINT = "{url}/api/networks"
DETAILS_LINK = (
    "More details: {url}/?/search?networkId={network_id}"
    "&snapshotId={snapshot_id}&q=f({src_ip})(ipv4_dst.{dst_ip})"
)
LATEST_PROCESSED_SNAPSHOT = (
    "{url}/api/networks/{network_id}/snapshots/latestProcessed"
)
SPACES = ' '*4


class BadStatusFromForwardServerException(Exception):
    pass


class MalformedDataFromForwardServerException(Exception):
    pass


class TraceRouteHopData:
    """
    Not compliant with snake_case naming style, but to be consistent
     with the data struct returned by Forward Server API
    """
    def __init__(
        self,
        deviceName: Optional[str] = None,
        ingressInterface: Optional[str] = None,
        egressInterface: Optional[str] = None,
        ingressInterfaceUtilization: Optional[int] = None,
        egressInterfaceUtilization: Optional[int] = None,
        aclNames: Optional[List[str]] = None,
        nats: Optional[List[str]] = None,
        vlan: Optional[int] = None,
        mplsLabels: Optional[List[int]] = None
    ):
        self.deviceName = deviceName
        self.ingressInterface = ingressInterface
        self.egressInterface = egressInterface
        self.ingressInterfaceUtilization = ingressInterfaceUtilization
        self.egressInterfaceUtilization = egressInterfaceUtilization
        self.aclNames = aclNames
        self.nats = nats
        self.vlan = vlan
        self.mplsLabels = mplsLabels

    def pretty_display(self, display_index: Optional[str] = None):
        display = []
        display.append(
            f"device name: {self.deviceName}"
        ) if self.deviceName else None
        display.append(
            f"ingress interface: {self.ingressInterface}"
            f" (utilization: {self.ingressInterfaceUtilization}%)"
        ) if self.ingressInterface and self.ingressInterfaceUtilization\
            else None
        display.append(
            f"egress interface: {self.egressInterface}"
            f" (utilization: {self.egressInterfaceUtilization}%)"
        ) if self.egressInterface and self.egressInterfaceUtilization\
            else None
        display.append(
            f"acl names: {self.aclNames}") if self.aclNames else None
        display.append(
            f"nat translations: {self.nats}") if self.nats else None
        display.append(f"vlan: {self.vlan}") if self.vlan else None
        display.append(
            f"mpls labels: {self.mplsLabels}"
        ) if self.mplsLabels else None

        if display_index:
            return f"{display_index} " + f"\n{SPACES}".join(display)

        return SPACES + f"\n{SPACES}".join(display)


def _get_forward_server_response(
    server_url: str, auth: Tuple[str, str], request_body: Dict
) -> Optional[List[TraceRouteHopData]]:
    # print(f"About to send request with the following body:{request_body}")
    try:
        response = requests.post(
            server_url,
            verify=False,
            auth=auth,
            headers={
                "Content-Type": "application/json"
            },
            data=json.dumps(request_body))
    except requests.exceptions.ConnectionError:
        return None
    if response.status_code != 200:
        raise BadStatusFromForwardServerException(
            f"Server reply: {response.text}"
        )
    try:
        hops = response.json()['hops']
        return json.loads(
            json.dumps(hops), object_hook=lambda d: TraceRouteHopData(**d)
        )
    except (KeyError, TypeError) as ex:
        raise MalformedDataFromForwardServerException(
            f"Received malformed data {response.json()} from ForwardServer"
        ) from ex


def get_extended_traceroute_data(
    request_body: Dict
) -> Optional[List[TraceRouteHopData]]:
    config_data = get_config_file_data()
    if not config_data:
        return None
    try:
        extended_traceroute_data = _get_forward_server_response(
            server_url=SERVER_ENDPOINT.format(
                url=config_data['forward_server_url'],
                network_id=config_data['network_id']
            ),
            auth=(config_data['username'], config_data['password']),
            request_body=request_body
        )
    except (
        BadStatusFromForwardServerException,
        MalformedDataFromForwardServerException
    ) as ex:
        print_blue(f"Exception getting extended traceroute data: {str(ex)}")
        return None
    return extended_traceroute_data


def check_forward_sever_reachability() -> bool:
    config_data = get_config_file_data()
    # Use localhost addresses for checking reachablility request since we
    # do not care about the information from the server
    empty_req_body = {
        "srcIP": "127.0.0.1",
        "dstIP": "127.0.0.1",
        "traceRouteHops": [["127.0.0.1"]],
        "lastHopSuffix": False
    }
    try:
        response = requests.post(
            SERVER_ENDPOINT.format(
                url=config_data['forward_server_url'],
                network_id=config_data['network_id']
            ),
            verify=False,
            auth=(config_data['username'], config_data['password']),
            headers={
                "Content-Type": "application/json"
            },
            data=json.dumps(empty_req_body)
        )
        if response.status_code != 200:
            return False
        return True
    except requests.exceptions.ConnectionError:
        return False


def _get_latest_processed_snapshot(config_data: Dict) -> Optional[str]:
    try:
        response = requests.get(
            LATEST_PROCESSED_SNAPSHOT.format(
                url=config_data['forward_server_url'],
                network_id=config_data['network_id']
            ),
            verify=False,
            auth=(config_data['username'], config_data['password'])
        )
        if response.status_code != 200:
            return None
        return response.json()['id']
    except (requests.exceptions.ConnectionError, KeyError):
        return None


def print_powered_by(src_ip: Optional[str], dst_ip: Optional[str]):
    config_data = get_config_file_data()
    if config_data and check_forward_sever_reachability():
        latest_processed_snapshot = _get_latest_processed_snapshot(
            config_data
        )
        if latest_processed_snapshot:
            print_blue(
                DETAILS_LINK.format(
                    url=config_data['forward_server_url'],
                    network_id=config_data['network_id'],
                    snapshot_id=latest_processed_snapshot,
                    src_ip=src_ip,
                    dst_ip=dst_ip
                )
            )
        print_blue("Powerd by Forward Platform.")
