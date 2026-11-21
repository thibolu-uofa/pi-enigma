def _is_valid(letter: str) -> bool:
    """Return True if the letter is a single uppercase letter A-Z."""
    return (
        len(letter) == 1
        and letter.isalpha()
        and ord(letter) >= ord("A")
        and ord(letter) <= ord("Z")
    )


def _to_index(letter: str) -> int:
    return ord(letter) - ord("A")


def _to_letter(index: int) -> str:
    return chr(index + ord("A"))


class Rotor:
    """One Enigma rotor: scrambles letters and turns as keys are pressed."""

    def __init__(
        self, wiring: str, notch: str, ring: str = "A", position: str = "A"
    ) -> None:
        """Create a rotor from its wiring, notch, ring setting and start position."""
        self._wiring = wiring.upper()
        self._notch = notch.upper()
        self._ring = ring.upper()
        self._position = position.upper()

    @property
    def position(self) -> str:
        """The letter currently shown in the rotor window."""
        return self._position

    def forward(self, letter: str) -> str:
        """Encode a letter right-to-left (towards the reflector)."""
        if not _is_valid(letter):
            raise ValueError("Input must be a single letter A-Z.")
        print(letter)
        letter = letter.upper()
        letter_forward = self._wiring[(_to_index(letter)) % 26]
        return letter_forward

    def backward(self, letter: str) -> str:
        """Encode a letter left-to-right (back from the reflector)."""
        raise NotImplementedError("Rotor class is not implemented yet.")

    def step(self) -> None:
        """Advance the rotor by one position, wrapping Z back to A."""
        raise NotImplementedError("Rotor class is not implemented yet.")

    def at_notch(self) -> bool:
        """Return True if the rotor is at its notch position."""
        raise NotImplementedError("Rotor class is not implemented yet.")
