from tensorflow.keras.callbacks import Callback
from typing import List
from ringbell import RingBell

__all__ = ["KerasDing"]


class KerasDing(Callback):

    def __init__(
        self,
        sample: str = "microwave",
        verbose: bool = True
    ):
        """Create a new RingBell.

        Parameters
        ------------------------------------------
        sample: str = "microwave"
            Name of one of the available samples.
            Currently available are 'bojack', 'pink_guy', 'rick', 'whale' and 'microwave'.
            Use 'random' for choosing a random sample.
            If the provided element is not in the set, we will check for
            a possible path.
        verbose: bool = True
            Whether to play the audio.

        Raises
        ----------------------
        ValueError
            If the given sample does not exist.
        ValueError
            If the given path does not correspond to a playable object.

        Returns
        ----------------------
        Return a new Ding object.
        """
        self._ringbell = RingBell(
            sample=sample,
            verbose=verbose
        )

    @staticmethod
    def available_samples() -> List[str]:
        """Returns list with the available samples."""
        return RingBell.available_samples()

    def on_train_end(self, *args: List):
        """Plays the sound at the end of training."""
        self._ringbell.play()
