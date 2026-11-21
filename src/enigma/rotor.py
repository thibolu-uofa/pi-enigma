class Rotor:
    """One Enigma rotor: scrambles letters and turns as keys are pressed."""

    def __init__(
        self, wiring: str, notch: str, ring: str = "A", position: str = "A"
    ) -> None:
        """Create a rotor from its wiring, notch, ring setting and start position."""
        raise NotImplementedError("Rotor class is not implemented yet.")

    @property
    def position(self) -> str:
        """The letter currently shown in the rotor window."""
        raise NotImplementedError("Rotor class is not implemented yet.")

    def forward(self, letter: str) -> str:
        """Encode a letter right-to-left (towards the reflector)."""
        raise NotImplementedError("Rotor class is not implemented yet.")

    def backward(self, letter: str) -> str:
        """Encode a letter left-to-right (back from the reflector)."""
        raise NotImplementedError("Rotor class is not implemented yet.")

    def step(self) -> None:
        """Advance the rotor by one position, wrapping Z back to A."""
        raise NotImplementedError("Rotor class is not implemented yet.")

    def at_notch(self) -> bool:
        """Return True if the rotor is at its notch position."""
        raise NotImplementedError("Rotor class is not implemented yet.")
