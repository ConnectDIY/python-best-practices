from __future__ import annotations
from abc import ABC, abstractmethod

from dip.data_structure import ReportModel
from dip.presenter import IPresenter


class IUseCaseInteractor(ABC):
    """
    High-level modules should not depend on low-level modules.
    Both should depend on abstractions.
    """

    def __init__(self, a: str, b: str, presenter: IPresenter):
        # a,b -- some required params for Business logic
        self.presenter = presenter
        self.b = b
        self.a = a

    @abstractmethod
    def get_report(self) -> ReportModel:
        pass


class UseCaseInteractorMock(IUseCaseInteractor):

    def get_report(self) -> ReportModel:
        rm = ReportModel(
            name='mock model',
            type='Main report',
            data={
                'a': self.a,
                'b': self.b
            }
        )

        # Imagine that we need to use IPresenter here.
        # Due to we shouldn't know about low-level dependency, we use DIP here.
        vm = self.presenter.get_view_model(rm)
        assert vm is not None

        # Mock data
        return rm
