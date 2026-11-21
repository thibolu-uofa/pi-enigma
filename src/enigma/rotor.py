def _to_index(letter: str) -> int:
    """Convert a letter A-Z (either case) to a number 0-25.

    Raises ValueError for anything that is not a single ASCII letter.
    """
    if not letter.isascii():
        raise ValueError("Input must be a single ASCII letter.")
    letter = letter.upper()
    if len(letter) != 1 or not "A" <= letter <= "Z":
        raise ValueError("Input must be a single letter A-Z.")
    return ord(letter) - ord("A")


def _to_letter(index: int) -> str:
    return chr(index + ord("A"))


class Rotor:
    """One Enigma rotor: scrambles letters and turns as keys are pressed."""

    def __init__(
        self, wiring: str, notch: str, ring: str = "A", position: str = "A"
    ) -> None:
        """Create a rotor from its wiring, notch, ring setting and start position."""
        self._wiring = [_to_index(c) for c in wiring]
        self._notch = notch.upper()
        self._ring = ring.upper()
        self._position = position.upper()

    @property
    def position(self) -> str:
        """The letter currently shown in the rotor window."""
        return self._position

    def forward(self, letter: str) -> str:
        """Encode a letter right-to-left (towards the reflector)."""
        return _to_letter(self._wiring[_to_index(letter)])

    def backward(self, letter: str) -> str:
        """Encode a letter left-to-right (back from the reflector)."""
        index = self._wiring.index(_to_index(letter))
        return _to_letter(index)

    def step(self) -> None:
        """Advance the rotor by one position, wrapping Z back to A."""
        raise NotImplementedError("Rotor class is not implemented yet.")

    def at_notch(self) -> bool:
        """Return True if the rotor is at its notch position."""
        raise NotImplementedError("Rotor class is not implemented yet.")
