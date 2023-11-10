from typing import Annotated
from fastapi import Header, HTTPException, status

from pykeutilsfastapi.tenant import tenant_extractor


class TenantName:
    """
    Dependency class for FastAPI. It returns the full tenant name.
    :param default_tenant: Default tenant.
    """

    def __init__(
            self,
            default_tenant: str = 'public',
    ):
        self.default_tenant = default_tenant

    def __call__(
            self,
            x_tenant_id: Annotated[str | None, Header()] = None,
            origin: Annotated[str | None, Header()] = None,
    ) -> str:
        return f"tenant_{tenant_extractor(str(origin), x_tenant_id, self.default_tenant)}"