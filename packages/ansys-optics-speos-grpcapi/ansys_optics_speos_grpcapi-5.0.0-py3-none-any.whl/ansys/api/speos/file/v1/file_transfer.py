"""Module to handle file transfer to a server.

This module allows to transfer files to and from a server

Examples
--------
>>> from ansys.api.speos import grpc_stub
>>> import ansys.api.speos.file.v1.file_transfer_pb2_grpc as file_transfer__v1__pb2_grpc
>>> stub = grpc_stub.get_stub_insecure_channel(
    target="localhost:50051",
    stub_type=file_transfer__v1__pb2_grpc.FileTransferServiceStub)
>>> from ansys.api.speos.file.v1 import file_transfer
>>> upload_response = file_transfer.upload_file(
        file_transfer_service_stub=stub,
        file_path="path/to/file")
>>> file_transfer.download_file(
            file_transfer_service_stub=stub,
            file_uri=upload_response.uri,
            download_location="path/to/download/location")
"""
import pathlib
import os.path
import ansys.api.speos.file.v1.file_transfer_pb2 as file_transfer__v1__pb2


def file_to_chunks(file, chunk_size=4000000):
    """Cut a file into chunks of specified chunk_size.

    Parameters
    ----------
    file : file object
    chunk_size : size
        number of bytes max in the chunk - default to 4000000

    Examples
    --------
    >>> from ansys.api.speos.file.v1 import file_transfer
    >>> with open("path/to/file", "rb") as file:
    >>>     chunk_iterator = file_transfer.file_to_chunks(file=file)
    >>>     # do something with chunk iterator
    """
    while buffer := file.read(chunk_size):
        chunk = file_transfer__v1__pb2.Chunk(binary=buffer, size=len(buffer))
        yield chunk

def upload_file(file_transfer_service_stub, file_path):
    """Upload a file to a server.

    Parameters
    ----------
    file_transfer_service_stub

    file_path : Path
        file's path to be uploaded

    Returns
    -------
    Upload_Response - object created from file_transfer.proto file, response of Upload procedure
    contains for example file uri and upload duration

    Examples
    --------
    >>> from ansys.api.speos import grpc_stub
    >>> import ansys.api.speos.file.v1.file_transfer_pb2_grpc as file_transfer__v1__pb2_grpc
    >>> stub = grpc_stub.get_stub_insecure_channel(
        target="localhost:50051",
        stub_type=file_transfer__v1__pb2_grpc.FileTransferServiceStub)
    >>> from ansys.api.speos.file.v1 import file_transfer
    >>> file_transfer.upload_file(
            file_transfer_service_stub=stub,
            file_path="path/to/file")
    """
    
    with open(file_path, 'rb') as file:
        chunk_iterator = file_to_chunks(file)

        metadata = [('file-name', os.path.basename(file_path)), ('file-size', str(os.path.getsize(file_path)))]
        upload_response = file_transfer_service_stub.Upload(chunk_iterator, metadata=metadata)

        return upload_response

def download_file(file_transfer_service_stub, file_uri, download_location):
    """Download a file from a server.

    Parameters
    ----------
    file_transfer_service_stub

    file_uri : Str
        file's uri on the server
    
    Examples
    --------
    >>> from ansys.api.speos import grpc_stub
    >>> import ansys.api.speos.file.v1.file_transfer_pb2_grpc as file_transfer__v1__pb2_grpc
    >>> stub = grpc_stub.get_stub_insecure_channel(
        target="localhost:50051",
        stub_type=file_transfer__v1__pb2_grpc.FileTransferServiceStub)
    >>> from ansys.api.speos.file.v1 import file_transfer
    >>> file_transfer.download_file(
            file_transfer_service_stub=stub,
            file_uri="uri_file_to_download",
            download_location="path/to/download/location")
    """
    
    chunks = file_transfer_service_stub.Download(file_transfer__v1__pb2.Download_Request(uri=file_uri))
    server_initial_metadata = dict(chunks.initial_metadata())
    file_path = os.path.join(download_location, server_initial_metadata['file-name'])
    with open(file_path, 'wb') as file:
        for chunk in chunks:
            file.write(chunk.binary)
    
        if int(server_initial_metadata['file-size']) != os.path.getsize(file_path):
            raise ValueError("File download incomplete")
