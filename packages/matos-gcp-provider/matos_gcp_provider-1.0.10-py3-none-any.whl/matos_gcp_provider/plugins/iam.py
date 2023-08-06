# -*- coding: utf-8 -*-
# pylint: disable=E1101
from typing import Any, Dict
from googleapiclient import discovery
from matos_gcp_provider.lib import factory
from matos_gcp_provider.lib.base_provider import BaseProvider


class IAM(BaseProvider):
    """GCP cloud iam class

    Args:
        BaseProvider (Class): Base provider class
    """

    def __init__(self, resource: Dict, **kwargs) -> None:
        """
        Construct IAM service
        """
        self.resource = resource
        self.resource_type = "iam"
        self.project_id = resource.pop("project_id")
        super().__init__(**kwargs)

    def get_inventory(self) -> Any:
        """
        Service discovery
        """
        polices = []
        service = discovery.build(
            "cloudresourcemanager", "v1", credentials=self.credentials
        )

        iam_policies = (
            service.projects().getIamPolicy(resource=self.project_id).execute()
        )

        for iam_policy in iam_policies.get("bindings"):
            polices.append({"type": self.resource_type, **iam_policy})
        return polices


def register() -> Any:
    """Register plugins type"""
    factory.register("iam", IAM)
