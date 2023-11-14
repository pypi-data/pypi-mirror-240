import multiprocessing
import pytest
import time

from servers.client_tester_server import ClientTesterServer


def client_tester_server_starter():
    server = ClientTesterServer('50051')
    server.serve()

@pytest.fixture(scope="session", autouse=True)
def client_tester_server():
    client_tester_server_process = multiprocessing.Process(target=client_tester_server_starter)
    client_tester_server_process.start()
    time.sleep(1)
    yield
    client_tester_server_process.terminate()
