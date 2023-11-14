import pytest

from rgrpc.client import Client

@pytest.fixture(scope="session", autouse=True)
def rgrpc_client():
    try:
        yield Client('localhost:50051')
    except Exception as e:
        pytest.fail(f"Failed to initialize rgrpc client: {e}")


def test_get_services(rgrpc_client):
    services = rgrpc_client.get_services()
    assert len(services) == 2
    assert 'client_tester.ClientTester' in services
    assert 'grpc.reflection.v1alpha.ServerReflection' in services

def test_get_method_names(rgrpc_client):
    methods = rgrpc_client.get_method_names('client_tester.ClientTester')
    assert len(methods) == 4
    assert 'TestUnaryUnary' in methods
    assert 'TestUnaryStream' in methods
    assert 'TestStreamUnary' in methods
    assert 'TestStreamStream' in methods

def test_get_method_full_names(rgrpc_client):
    methods = rgrpc_client.get_method_full_names('client_tester.ClientTester')
    assert len(methods) == 4
    assert 'client_tester.ClientTester.TestUnaryUnary' in methods
    assert 'client_tester.ClientTester.TestUnaryStream' in methods
    assert 'client_tester.ClientTester.TestStreamUnary' in methods
    assert 'client_tester.ClientTester.TestStreamStream' in methods

def test_make_unary_unary_request(rgrpc_client):
    response = rgrpc_client.request(
        "client_tester.ClientTester",
        "TestUnaryUnary",
        {"factor": 1.0, "readings": [1.0, 2.0, 3.0]}
    )
    assert response == {'feedback': 'Acceptable'}

def test_make_unary_stream_request(rgrpc_client):
    responses = rgrpc_client.request(
        "client_tester.ClientTester",
        "TestUnaryStream",
        {"factor": 1.0, "readings": [1.0, 2.0, 3.0]}
    )
    for response in responses:
        assert response == {'feedback': 'Acceptable'}

def test_make_stream_unary_request(rgrpc_client):
    factors = [1.0, 2.0, 3.0]
    readings = [1.0, 2.0, 3.0]
    response = rgrpc_client.request(
        "client_tester.ClientTester","TestStreamUnary",
        iter([{"factor": factor, "readings": readings} for factor in factors])
    )
    assert response == {'feedback': 'Acceptable'}

def test_make_stream_stream_request(rgrpc_client):
    factors = [1.0, 2.0, 3.0]
    readings = [1.0, 2.0, 3.0]
    responses = rgrpc_client.request(
        "client_tester.ClientTester","TestStreamStream",
        iter([{"factor": factor, "readings": readings} for factor in factors])
    )
    for response in responses:
        assert response == {'feedback': 'Acceptable'}
