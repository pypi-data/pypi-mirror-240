from datetime import date
import json
from typing import Optional

from ssb_altinn3_util.models.skjemadata.skjemadata_request_models import SkjemaRequestModel

from dapla_suv_tools._internals.integration import api_client
from dapla_suv_tools._internals.util.operation_result import OperationResult
from dapla_suv_tools._internals.util.suv_operation_context import SuvOperationContext
from dapla_suv_tools._internals.util.validators import skjema_id_validator, ra_nummer_validator


@SuvOperationContext(validator=skjema_id_validator)
def get_skjema_by_id(*, skjema_id: int, context: SuvOperationContext = None) -> OperationResult:
    try:
        content: str = api_client._get(path=f"/skjemadata/skjema/{skjema_id}")
        content_json = json.loads(content)
        return OperationResult(success=True, value=content_json)

    except Exception as e:
        context.set_error(type(e).__name__, f"Failed to fetch for id {skjema_id}", e)
        return OperationResult(success=False, value=context.errors())


@SuvOperationContext(validator=ra_nummer_validator)
def get_skjema_by_ra_nummer(*, ra_nummer: str, max_results: int = 10, latest_only: bool = False, context: SuvOperationContext = None) -> dict:
    try:
        filters = json.dumps({"ra_nummer": ra_nummer})
        content: str = api_client._post(
            path=f"/skjemadata/skjema_paged?size={max_results}&order_by=versjon&asc=false", body_json=filters
        )

        result: dict = json.loads(content)

        if latest_only:
            return result["results"][0]

        return result["results"]

    except Exception as e:
        raise Exception(f"Failed to fetch for ra_nummer '{ra_nummer}'.", e)


@SuvOperationContext(validator=ra_nummer_validator)
def create_skjema(
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
        context: SuvOperationContext = None
) -> int:
    model = SkjemaRequestModel(
        ra_nummer=ra_nummer,
        versjon=versjon,
        undersokelse_nr=undersokelse_nr,
        gyldig_fra=gyldig_fra,
        gyldig_til=gyldig_til,
        endret_av=endret_av,
        datamodell=datamodell,
        beskrivelse=beskrivelse,
        navn_nb=navn_nb,
        navn_nn=navn_nn,
        navn_en=navn_en,
        infoside=infoside,
        eier=eier,
        kun_sky="J" if kun_sky else "N"
    )

    try:
        body = model.model_dump_json()
        content: str = api_client._post(path=f"/skjemadata/skjema", body_json=body)
        return json.loads(content)["id"]
    except Exception as e:
        raise Exception(f"Failed to create for ra_number '{ra_nummer}' - version '{versjon}'", e)


@SuvOperationContext(validator=skjema_id_validator)
def delete_skjema(*, skjema_id: int, context: SuvOperationContext = None) -> bool:
    pass
