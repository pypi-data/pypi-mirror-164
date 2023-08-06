"""aasas

https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#custom-connection-types
"""
import json
from json import JSONDecodeError
from typing import Any, Dict, Optional

import requests


from airflow.providers.http.hooks.http import HttpHook


class OrchestrationHttpHook(HttpHook):
    """Orchestration sensor class."""

    conn_name_attr = "http_conn_id"
    default_conn_name = "y42demo_default"
    conn_type = "y42demo_orchestration"
    hook_name = "Y42demo Orchestration"

    def get_conn(self, headers: Optional[Dict[Any, Any]] = None) -> requests.Session:
        """Returns http session for use with requests."""
        session = requests.Session()

        if self.http_conn_id:
            conn = self.get_connection(self.http_conn_id)

            if conn.host and "://" in conn.host:
                self.base_url = conn.host
            else:
                host = conn.host if conn.host else ""
                self.base_url = "https" + "://" + host

            extra = self._extra_to_dict(conn.extra)
            if not headers:
                headers = {}

            headers.update(
                {
                    "Content-Type": "application/json",
                    # "User-Agent": "orchestration-api/2",
                    "x-storage-type": extra["x_storage_type"],
                    "x-storage-id": extra["x_storage_id"],
                    "x-storage-branch": extra["x_storage_branch"],
                    "Authorization": extra["authorization_token"],
                }
            )

        if headers:
            session.headers.update(headers)

        self.log.info("Headers")
        self.log.info(session.headers)
        return session

    @property
    def company_id(self) -> int:
        """Get company id."""
        conn = self.get_connection(self.http_conn_id)
        extra = self._extra_to_dict(conn.extra)
        return int(extra["company_id"])

    @classmethod
    def get_connection_form_widgets(cls) -> Dict[str, Any]:
        """Returns connection widgets to add to connection form"""
        from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
        from flask_babel import lazy_gettext
        from wtforms import IntegerField, StringField

        return {
            "company_id": IntegerField(lazy_gettext("Company Id"), widget=BS3TextFieldWidget()),
            "x_storage_type": StringField(lazy_gettext("Storage Type"), widget=BS3TextFieldWidget()),
            "x_storage_id": StringField(lazy_gettext("Storage Id"), widget=BS3TextFieldWidget()),
            "x_storage_branch": StringField(lazy_gettext("Storage Branch"), widget=BS3TextFieldWidget()),
            "authorization_token": StringField(lazy_gettext("Authorization Token"), widget=BS3TextFieldWidget()),
        }

    @classmethod
    def get_ui_field_behaviour(cls) -> Dict[str, Any]:
        """Returns custom field behaviour."""
        return {
            "hidden_fields": [
                "port",
                "login",
                "password",
                "schema",
                "extra",
            ],
            "placeholders": {},
            "relabeling": {},
        }

    def test_connection(self):
        """Test HTTP Connection"""
        return True, "Connection successfully tested"

    def _extra_to_dict(self, extra: str) -> Dict:
        """Returns the extra property by deserializing json."""
        obj = {}
        try:
            obj = json.loads(extra)
        except JSONDecodeError:
            self.log.exception("Failed parsing the json for conn_id %s", self.http_conn_id)
        return obj
