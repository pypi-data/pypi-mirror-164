from .. import cli
import os
import pytest
import sys


def test_cli():
    sys.argv = ["ym2021_prj"]
    response = cli.main()
    assert isinstance(response, str)
    assert "ym2021_prj" in response


@pytest.mark.parametrize(
    "var_name, exists, value",
    [
        ["TESTABLE", True, "testable"],
        ["NO_SUCH_ENV_VAR", False, None],
    ],
)
def test_env_var(var_name, exists, value):
    assert (var_name in os.environ) is exists
    env_var = os.environ.get(var_name)
    assert env_var == value
