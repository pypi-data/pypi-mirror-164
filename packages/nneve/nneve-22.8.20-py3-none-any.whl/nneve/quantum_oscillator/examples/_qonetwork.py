from pathlib import Path

from .. import QOConstants, QONetwork, QOTracker

__all__ = ["default_qo_network"]

DIR = Path(__file__).parent
WEIGHTS_DIR = DIR / "_weights"


def default_qo_network(state: int = 1) -> QONetwork:
    assert 1 <= state <= 7, "Only states from 1 to 7 are available."
    constants = QOConstants(
        k=4.0,
        mass=1.0,
        x_left=-6.0,
        x_right=6.0,
        fb=0.0,
        sample_size=1200,
        tracker=QOTracker(),
    )
    network = QONetwork(constants=constants)
    network.load(WEIGHTS_DIR / f"s{state}.w")
    return network
