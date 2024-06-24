import typer

from dip.controller import Controller1
from dip.data_structure import ReportType
from dip.presenter import Presenter, StdOutView, TxtView
from dip.use_case_layer import UseCaseInteractorMock


def cli(report_type: ReportType, lines_limit: int = 10):
    presenter = Presenter()
    interactor = UseCaseInteractorMock('line1', 'line2', presenter)
    controller = Controller1(interactor)
    report = controller.get_report(report_type, lines_limit)


    view_model = presenter.get_view_model(report)
    StdOutView().handle(view_model)
    TxtView('test.txt').handle(view_model)


typer.run(cli)
