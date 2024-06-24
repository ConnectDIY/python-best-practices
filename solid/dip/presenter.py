from __future__ import annotations
from abc import ABC, abstractmethod

from dip.data_structure import ReportModel, ViewModel


class IPresenter(ABC):
    @abstractmethod
    def get_view_model(self, report_model: ReportModel) -> ViewModel:
        pass


class Presenter(IPresenter):
    # That is required to add IPresenter if we want to use
    # this class somewhere in the Higher lvl code.

    def get_view_model(self, report_model: ReportModel) -> ViewModel:
        return ViewModel(
            header=f"Report for {report_model.name} in {report_model.type} format.",
            lines=[f"[{k}] {v}" for k, v in report_model.data.items()]
        )


class IView(ABC):
    @abstractmethod
    def handle(self, view_model: ViewModel):
        pass


class StdOutView(IView):

    def handle(self, view_model: ViewModel):
        print(view_model.header)
        for line in view_model.lines:
            print(line)


class TxtView(IView):
    def __init__(self, filename: str):
        self.filename = filename

    def handle(self, view_model: ViewModel):
        with open(self.filename, 'w') as f:
            print(view_model.header, file=f)
            for line in view_model.lines:
                print(line, file=f)
