# -*- coding: utf-8 -*-
import logging
from typing import Any, Dict
from matos_aws_provider.lib import factory
from matos_aws_provider.lib.base_provider import BaseProvider

logger = logging.getLogger(__name__)


class AwsECS(BaseProvider):
    def __init__(self,
                 resource: Dict,
                 **kwargs,
                 ) -> None:
        """
        """
        try:
            super().__init__(**kwargs, client_type="ecs")
            self.resource = resource if resource else {}
        except Exception as ex:
            logger.error(ex)

    def get_inventory(self) -> Any:
        """
        Fetches ecs details.
        """
        clusters = self.conn.list_clusters()
        return [{"clusterArns": item, "type": "ecs"} for item in clusters.get('clusterArns', [])]

    def get_resources(self) -> Any:
        """
        Fetches ecs details.
        """
        services = self.conn.list_services(
            cluster=self.resource.get('clusterArns')
        )
        services = self.conn.describe_services(
            cluster=self.resource.get('clusterArns'),
            services=services.get('serviceArns')
        ).get('services') if len(services.get('serviceArns', [])) else []
        resource = {
            "clusterArns": self.resource.get('clusterArns'),
            "services": services
        }

        return resource


def register() -> Any:
    """Register class method

    Returns:
        Any: register class
    """
    factory.register("ecs", AwsECS)
