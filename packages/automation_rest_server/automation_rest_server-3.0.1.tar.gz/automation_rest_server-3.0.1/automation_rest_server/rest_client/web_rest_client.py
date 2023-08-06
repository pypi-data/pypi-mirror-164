
import os
import yaml
import requests
from rest_client.resource.node_resource import NodeResource
from rest_client.resource.test_resource import TestResource
from test_framework.state import NodeState
from utils import log


class WebRestClient(object):

    def __init__(self, time_out=20):
        host, port = self.get_web_server()
        __session = requests.Session()
        self.node = NodeResource(host, port, __session, time_out=time_out)
        self.test = TestResource(host, port, __session, time_out=time_out)

    @staticmethod
    def get_web_server():
        config_file = os.path.join(os.path.dirname(__file__), '..', 'configuration', 'web_server.yaml')
        server = yaml.load(open(config_file).read(), Loader=yaml.FullLoader)
        return server["host"], server['port']


def decorate_api_update_test_result(func):
    def func_wrapper(*args, **kwargs):
        print("decorate_api_update_test_result")
        ret = func(*args, **kwargs)
        client = WebRestClient()
        client.test.update_test_result(args[1], args[2], args[3], args[4])
        log.INFO("decorate_api_update_test_result end")
        return ret
    return func_wrapper


def decorate_api_update_node_status(func):
    def func_wrapper(*args, **kwargs):
        is_updated, status = func(*args, **kwargs)
        if is_updated is True:
            client = WebRestClient()
            client.node.update_node_status(status)
            log.INFO("Rest API set node status to {}".format(NodeState.verdicts_map[status]))
        return is_updated, status
    return func_wrapper


def decorate_api_node_startup(func):
    def func_wrapper(*args, **kwargs):
        log.INFO("Rest API Node startup")
        client = WebRestClient()
        client.node.startup()
        ret = func(*args, **kwargs)
        return ret
    return func_wrapper

