"""Test."""
from hlm_texts import __version__


def test_version():
    """Test version."""
    assert __version__[:-1] == "0.1."
