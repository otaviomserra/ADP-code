import logging
from typing import Union

from google.protobuf.json_format import Parse, ParseError
from google.protobuf.message import DecodeError

from core.ils.external.organisation_event_pb2 import OrganisationEvent

logger = logging.getLogger(__name__)


def message_deserializer(message: bytes) -> Union[OrganisationEvent, None]:
    result = None

    try:
        result = Parse(
            message.decode("utf-8"),
            OrganisationEvent(),
            ignore_unknown_fields=False
        )
    except (DecodeError, ValueError, ParseError) as error:
        logger.error(f"Failed to parse OrganisationEvent: {str(error)}")

    return result
