from dapla_suv_tools._internals.util import constants


class OperationResult:
    result_json: dict
    result: str
    operation_log: dict

    def __init__(self, value: dict, success: bool = True,  log: dict = None):
        self.result = constants.OPERATION_OK if success else constants.OPERATION_ERROR
        self.result_json = value
        self.operation_log = {} if log is None else log
