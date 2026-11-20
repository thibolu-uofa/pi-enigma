"""Smoke tests: check that the project is installed and importable."""

import enigma

def test_package_imports() -> None:
    """Check that the package can be imported."""
    assert enigma is not None
    assert enigma.__doc__ is not None
    assert "Enigma machine simulator." == enigma.__doc__
