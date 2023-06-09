"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2015 gRPC authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import abc
import collections.abc
import grpc
import helloworld_pb2

class GreeterStub:
    """The greeting service definition."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    SayHello: grpc.UnaryUnaryMultiCallable[
        helloworld_pb2.HelloRequest,
        helloworld_pb2.HelloReply,
    ]
    """Sends a greeting"""
    SayHelloStreamReply: grpc.UnaryStreamMultiCallable[
        helloworld_pb2.HelloRequest,
        helloworld_pb2.HelloReply,
    ]

class GreeterServicer(metaclass=abc.ABCMeta):
    """The greeting service definition."""

    @abc.abstractmethod
    def SayHello(
        self,
        request: helloworld_pb2.HelloRequest,
        context: grpc.ServicerContext,
    ) -> helloworld_pb2.HelloReply:
        """Sends a greeting"""
    @abc.abstractmethod
    def SayHelloStreamReply(
        self,
        request: helloworld_pb2.HelloRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[helloworld_pb2.HelloReply]: ...

def add_GreeterServicer_to_server(servicer: GreeterServicer, server: grpc.Server) -> None: ...
