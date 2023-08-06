from hrthy_core.events.events.base_event import BaseEvent, BasePayload
from hrthy_core.security.security import Requester


class CompanyCreatedPayload(BasePayload):
    name: str
    email: str
    active: bool


class CompanyUpdatedPayload(CompanyCreatedPayload):
    pass


class CompanyDeletedPayload(BasePayload):
    pass


class CompanyRestoredPayload(BasePayload):
    pass


class CompanyCreatedEvent(BaseEvent):
    requester: Requester = None
    type = 'CompanyCreatedEvent'
    payload: CompanyCreatedPayload


class CompanyUpdatedEvent(BaseEvent):
    type = 'CompanyUpdatedEvent'
    payload: CompanyUpdatedPayload


class CompanyDeletedEvent(BaseEvent):
    type = 'CompanyDeletedEvent'
    payload: CompanyDeletedPayload


class CompanyRestoredEvent(BaseEvent):
    type = 'CompanyRestoredEvent'
    payload: CompanyRestoredPayload
