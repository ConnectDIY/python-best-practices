from dip.data_structure import ReportType, ReportModel
from dip.use_case_layer import IUseCaseInteractor


class Controller1:
    def __init__(self, interactor: IUseCaseInteractor):
        self.interactor = interactor


    def get_report(self, report_type: ReportType, lines_limit: int) -> ReportModel:
        report_model = self.interactor.get_report()
        return report_model

