"""Test uvicorn kw."""

import pytest

from spec import load_spec
from spec.service.runner import uvicorn_options


@pytest.fixture
def pyproject(mocker):
    """Mock pyproject."""
    fake_pyproject = {
        'tool': {
            'poetry': {
                'name': 'service-name',
                'version': '1.2.3',
                'description': 'Service description',
            },
        },
    }

    mocker.patch('spec.fn.load_pyproject', return_value=fake_pyproject)
    return fake_pyproject


def test_uvicorn_options():
    """Test uvicorn options."""

    spec = load_spec()
    options = uvicorn_options(spec)

    assert options['app'] == spec.service.entrypoint
    assert options['host'] == spec.service.uri.host
    assert options['port'] == spec.service.uri.port
    assert options['use_colors'] != spec.status.on_k8s
    assert options['log_level'] == spec.profile.log_level
    assert 'log_config' not in options
    assert options['access_log'] == spec.status.debug
    assert options['workers'] == spec.policies.service_workers
