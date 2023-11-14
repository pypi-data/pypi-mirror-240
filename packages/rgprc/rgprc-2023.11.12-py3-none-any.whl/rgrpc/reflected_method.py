# mypy: ignore-errors
from google.protobuf.message_factory import GetMessageClass
from google.protobuf.descriptor import MethodDescriptor
from google.protobuf.json_format import MessageToDict, ParseDict

from typing import Any, Dict, Iterator, List, Union


class ReflectedMethod:
    def __init__(self, channel, method_desc: MethodDescriptor):
        """
        Build a method handler for a given method full name
        """
        self.input_prototype = GetMessageClass(method_desc.input_type)
        self.output_prototype = GetMessageClass(method_desc.output_type)

        if method_desc.client_streaming and method_desc.server_streaming:
            abstract_handler = channel.stream_stream
            req_parser = self.parse_stream_request
            res_parser = self.parse_stream_response
        elif method_desc.client_streaming:
            abstract_handler = channel.stream_unary
            req_parser = self.parse_stream_request
            res_parser = self.parse_unary_response
        elif method_desc.server_streaming:
            abstract_handler = channel.unary_stream
            req_parser = self.parse_unary_request
            res_parser = self.parse_stream_response
        else:
            abstract_handler = channel.unary_unary
            req_parser = self.parse_unary_request
            res_parser = self.parse_unary_response

        self.handler = abstract_handler(
            f"/{method_desc.containing_service.full_name}/{method_desc.name}",
            self.input_prototype.SerializeToString,
            self.output_prototype.FromString,
        )

        self.request_parser = req_parser
        self.response_parser = res_parser

    def parse_stream_request(
        self, json_request_iter: Iterator, options
    ) -> Iterator[Dict[str, Any]]:
        requests = []
        for request in json_request_iter:
            requests.append(ParseDict(request, self.input_prototype(), **options))
        return iter(requests)

    def parse_unary_request(self, json_request: Dict[str, Any], options) -> Any:
        return ParseDict(json_request, self.input_prototype(), **options)

    def parse_stream_response(
        self, response_iter: Iterator, options
    ) -> List[Dict[str, Any]]:
        responses = []
        for response in response_iter:
            responses.append(MessageToDict(response, **options))
        return responses

    def parse_unary_response(self, response: Any, options) -> Dict[str, Any]:
        return MessageToDict(response, **options)

    def request(
        self, requests: Union[Iterator, Dict[str, Any]], options={}
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """
        Make a request to a given service and method with a given request
        :param json_request: Request as a dict
        :return: Response as a dict
        """

        return self.response_parser(
            (self.handler(self.request_parser(requests, options), timeout=10)), options
        )
