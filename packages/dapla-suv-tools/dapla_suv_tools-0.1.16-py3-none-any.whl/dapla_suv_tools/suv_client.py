from datetime import date
from typing import Optional
import dapla_suv_tools._internals.client_apis.skjema_api as skjema_api
from dapla_suv_tools._internals.util.operation_result import OperationResult
from dapla_suv_tools._internals.util import constants


class SuvClient:
    suppress_exceptions: bool

    def __init__(self, suppress_exceptions: bool):
        self.suppress_exceptions = suppress_exceptions

    def get_skjema_by_id(self, *, skjema_id: int) -> dict:
        result = skjema_api.get_skjema_by_id(skjema_id=skjema_id)
        return self._process_result(result=result)

    def get_skjema_by_ra_nummer(
            self,
            *,
            ra_nummer: str,
            latest_only: bool = False,
            use_pagination: bool = False) -> dict:
        return skjema_api.get_skjema_by_ra_nummer(ra_nummer=ra_nummer, latest_only=latest_only)

    def create_skjema(
            self,
            *,
            ra_nummer: str,
            versjon: int,
            undersokelse_nr: str,
            gyldig_fra: date,
            endret_av: str,
            datamodell: Optional[str] = None,
            beskrivelse: Optional[str] = None,
            navn_nb: Optional[str] = None,
            navn_nn: Optional[str] = None,
            navn_en: Optional[str] = None,
            infoside: Optional[str] = None,
            eier: Optional[str] = None,
            kun_sky: bool = False,
            gyldig_til: Optional[date] = None,
    ) -> int:
        return skjema_api.create_skjema(**locals())

    def delete_skjema(self, skjema_id: int):
        return skjema_api.delete_skjema(skjema_id=skjema_id)

    def _process_result(self, result: OperationResult) -> dict:
        if result.result == constants.OPERATION_OK:
            return result.result_json

        if result.result == constants.OPERATION_ERROR:
            if self.suppress_exceptions:
                return result.result_json
            errors = result.result_json["errors"]
            raise errors[len(errors) - 1]["exception"]

        return {"result": "Undefined result.  This shouldn't happen." }
