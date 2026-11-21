"""Tests for the Rotor class"""

from enigma.rotor import Rotor

ROTOR_I_WIRING = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR_I_NOTCH = "Q"


def test_tr1_forward_a_to_e() -> None:
    """Test that Rotor I encodes A to E in the forward direction."""
    rotor = Rotor(ROTOR_I_WIRING, ROTOR_I_NOTCH)
    assert rotor.forward("A") == "E"
