import json

from dapla_suv_tools._internals.integration import api_client
from dapla_suv_tools._internals.util.operation_result import OperationResult
from dapla_suv_tools._internals.util.suv_operation_context import SuvOperationContext
from dapla_suv_tools._internals.util.validators import periode_id_validator, skjema_id_validator

PERIODE_PATH = "/skjemadata/periode"


@SuvOperationContext(validator=periode_id_validator)
def get_periode_by_id(*, periode_id: int, context: SuvOperationContext = None) -> OperationResult:
    try:
        content: str = api_client._get(path=f"{PERIODE_PATH}/{periode_id}", context=context)
        content_json = json.loads(content)
        context.log("info", "get_periode_by_id", f"Fetched periode with periode_id '{periode_id}'")

        return OperationResult(value=content_json, log=context.logs())
    except Exception as e:
        context.set_error(f"Failed to fetch for id {periode_id}", e)

        return OperationResult(success=False, value=context.errors(), log=context.logs())


@SuvOperationContext(validator=skjema_id_validator)
def get_perioder_by_skjema_id(*, skjema_id: int, context: SuvOperationContext = None) -> OperationResult:
    try:
        content: str = api_client._get(path=f"{PERIODE_PATH}/skjema/{skjema_id}", context=context)
        content_json = json.loads(content)
        context.log("info", "get_periode_by_skjema_id", f"Fetched perioder for skjema_id '{skjema_id}'")

        return OperationResult(value=content_json, log=context.logs())
    except Exception as e:
        context.set_error(f"Failed to fetch for skjema_id {skjema_id}", e)

        return OperationResult(success=False, value=context.errors(), log=context.logs())
