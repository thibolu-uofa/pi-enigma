"""Tests for the Rotor class"""

import pytest

from enigma.rotor import Rotor

ROTOR_I_WIRING = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR_I_NOTCH = "Q"


def test_tr1_forward_a_to_e() -> None:
    """Test that Rotor I encodes A to E in the forward direction."""
    rotor = Rotor(ROTOR_I_WIRING, ROTOR_I_NOTCH)
    assert rotor.forward("A") == "E"


@pytest.mark.parametrize("bad_letter", ["7", "!", "Ä", "", "AB"])
def test_tr7_forward_rejects_invalid_letter(bad_letter: str) -> None:
    """forward() must reject anything that is not a single letter A-Z."""
    rotor = Rotor(ROTOR_I_WIRING, ROTOR_I_NOTCH)
    with pytest.raises(ValueError):
        rotor.forward(bad_letter)
