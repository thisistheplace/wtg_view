from abc import ABC, abstractmethod

class TabBase(ABC):

    @property
    @abstractmethod
    def layout(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    def apply_layout(self, app):
        app.layout = self.layout

    @abstractmethod
    def apply_callbacks(self, app):
        pass
