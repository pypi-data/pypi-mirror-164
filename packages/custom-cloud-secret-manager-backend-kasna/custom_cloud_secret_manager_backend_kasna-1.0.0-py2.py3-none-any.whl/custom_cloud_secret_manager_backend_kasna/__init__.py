from typing import Optional

from airflow.providers.google.cloud.secrets.secret_manager import CloudSecretManagerBackend


class CustomCloudSecretManagerBackend(CloudSecretManagerBackend):
    def __init__(self, secret_lookup_prefix: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.secret_lookup_prefix = secret_lookup_prefix

    def get_variable(self, key: str) -> Optional[str]:
        if self.variables_prefix is None:
            return None

        if self.secret_lookup_prefix is not None:
            if not key.startswith(self.secret_lookup_prefix):
                return None

        return self._get_secret(self.variables_prefix, key)
