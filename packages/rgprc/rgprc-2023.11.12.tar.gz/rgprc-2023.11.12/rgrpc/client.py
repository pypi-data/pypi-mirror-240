import grpc
import logging

from .reflected_method import ReflectedMethod

from google.protobuf.descriptor_pool import DescriptorPool
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import (
    ProtoReflectionDescriptorDatabase,
)
from typing import Any, Dict, List, Optional, Union, Iterator


class Client:
    logger = logging.getLogger(__name__)

    def __init__(
        self,
        address: str,
        secure_channel: bool = False,
        credentials: Optional[grpc.ChannelCredentials] = None,
    ):
        """
        Initialize a grpc client to a reflection enabled server.
        Methods are discovered at runtime using reflection.
        :param address: Address of the server
        :param secure_channel: Whether to use a secure channel
        :param credentials: Credentials to use for secure channel
        """
        if secure_channel:
            if credentials is None:
                raise Exception("Secure channel requested but no credentials provided")
            self.channel = grpc.secure_channel(address, credentials)
        else:
            self.channel = grpc.insecure_channel(address)
        self.reflection_db = ProtoReflectionDescriptorDatabase(self.channel)
        self.descriptor_pool = DescriptorPool(self.reflection_db)
        self.reflected_methods = {}
        for service in self.reflection_db.get_services():
            for method_full_name in self.get_method_full_names(service):
                method_desc = self.descriptor_pool.FindMethodByName(method_full_name)
                self.reflected_methods[method_full_name] = ReflectedMethod(
                    self.channel, method_desc
                )

    def get_services(self) -> List[str]:
        """
        List the names of available services.
        :return: List of service names as strings
        """
        return self.reflection_db.get_services()

    def get_method_names(self, service: str) -> List[str]:
        """
        List of method names for a given named service
        :param service: Service name as string
        :return: List of method names as strings
        """
        if service not in self.get_services():
            raise ValueError(f"Service {service} not available")

        return [
            method.name
            for method in self.descriptor_pool.FindServiceByName(service).methods
        ]

    def get_method_full_names(self, service: str) -> List[str]:
        """
        List of method full names for a given named service
        :param service: Service name as string
        :return: List of method full names as strings
        """
        if service not in self.get_services():
            raise ValueError(f"Service {service} not available")

        return [
            method.full_name
            for method in self.descriptor_pool.FindServiceByName(service).methods
        ]

    def request(
        self, service: str, method_name: str, request: Union[Iterator, Dict[str, Any]]
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """
        Make a request to a given service and method with a given request
        :param service: Service name as string
        :param method_name: Method name as string
        :param json_request: Request as a dict
        :return: Response as a dict
        """

        reflected_method = self.reflected_methods[f"{service}.{method_name}"]

        # Make request
        return reflected_method.request(request, {})
