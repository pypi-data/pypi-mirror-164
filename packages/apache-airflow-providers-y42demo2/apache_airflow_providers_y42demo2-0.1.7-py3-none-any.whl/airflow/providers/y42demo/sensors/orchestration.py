from typing import Union, Any

from airflow.sensors.base import (
    BaseSensorOperator,
    PokeReturnValue,
)
from airflow.utils.context import Context

from ..hooks.orchestration import OrchestrationHttpHook


class OrchestrationSensor(BaseSensorOperator):
    """Orchestration sensor class."""

    default_conn_name = "y42demo_default"

    def __init__(
        self,
        *,
        location: str,
        http_conn_id: str = default_conn_name,
        **kwargs,
    ) -> None:

        super().__init__(**kwargs)
        self.http_conn_id = http_conn_id
        self._run_id = None
        self._location = location

    def execute(self, context: "Context") -> Any:
        """Overridden to allow messages to be passed"""

        hook = OrchestrationHttpHook(method="POST", http_conn_id=self.http_conn_id)
        response = hook.run(
            endpoint=f"/api/2/orchestrations/company/{hook.company_id}/trigger",
            json={"location": self._location},
        )
        assert response.status_code == 201
        data = response.json()
        self.log.info("Data: %s", data)
        self._run_id = data["run_id"]
        return super().execute(context)

    def poke(self, context: Context) -> Union[bool, PokeReturnValue]:
        """Poke sensor."""
        hook = OrchestrationHttpHook(method="GET", http_conn_id=self.http_conn_id)
        response = hook.run(
            endpoint=f"/api/2/orchestrations/company/{hook.company_id}/{self._run_id}",
            headers={
                "x-storage-location": self._location,
            },
        )
        data = response.json()
        self.log.info("Data: %s", data)
        return data["status"] == "ready"
