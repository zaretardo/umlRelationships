# Realization: Activity implements the ActivityInterface

from abc import ABC, abstractmethod


class ActivityInterface(ABC):
    @abstractmethod
    def conduct(self):
        pass


class ScienceFair(ActivityInterface):
    def conduct(self):
        print("The science fair has started.")


activity = ScienceFair()
activity.conduct()