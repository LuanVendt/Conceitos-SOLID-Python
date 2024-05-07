from abc import ABC, abstractmethod


class Document(ABC):  # generic

    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

    @abstractmethod
    def format(self): pass

    @abstractmethod
    def calculate(self): pass


class DocumentPDF:  # ISP

    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass


class DocumentTXT:  # ISP

    @abstractmethod
    def load(self): pass

    @abstractmethod
    def format(self): pass


class DocumentExcel:  # ISP

    @abstractmethod
    def load(self): pass

    @abstractmethod
    def calculate(self): pass


# Uma classe não deve ser forçada a implementar interfaces que ela não utiliza
