from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_put_entry_by_file_exact_hash_collection_name_file_put import (
    BodyPutEntryByFileExactHashCollectionNameFilePut,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_name: str,
    *,
    multipart_data: BodyPutEntryByFileExactHashCollectionNameFilePut,
    foreign_key: Union[None, Unset, int, str] = UNSET,
    metadata: Union[Unset, None, str] = UNSET,
    upsert: Union[Unset, None, bool] = False,
    timestamp: Union[Unset, None, str] = UNSET,
    store_raw_data: Union[Unset, None, bool] = True,
    ingest_source: Union[Unset, None, str] = UNSET,
    container_type: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_foreign_key: Union[None, Unset, int, str]
    if isinstance(foreign_key, Unset):
        json_foreign_key = UNSET
    elif foreign_key is None:
        json_foreign_key = None

    else:
        json_foreign_key = foreign_key

    params["foreign_key"] = json_foreign_key

    params["metadata"] = metadata

    params["upsert"] = upsert

    params["timestamp"] = timestamp

    params["store_raw_data"] = store_raw_data

    params["ingest_source"] = ingest_source

    params["container_type"] = container_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "put",
        "url": "/exact/hash/{collection_name}/file".format(
            collection_name=collection_name,
        ),
        "files": multipart_multipart_data,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, response.json())
        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_name: str,
    *,
    client: AuthenticatedClient,
    multipart_data: BodyPutEntryByFileExactHashCollectionNameFilePut,
    foreign_key: Union[None, Unset, int, str] = UNSET,
    metadata: Union[Unset, None, str] = UNSET,
    upsert: Union[Unset, None, bool] = False,
    timestamp: Union[Unset, None, str] = UNSET,
    store_raw_data: Union[Unset, None, bool] = True,
    ingest_source: Union[Unset, None, str] = UNSET,
    container_type: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    """Put Entry By File

    Args:
        collection_name (str):
        foreign_key (Union[None, Unset, int, str]):
        metadata (Union[Unset, None, str]):
        upsert (Union[Unset, None, bool]):
        timestamp (Union[Unset, None, str]):
        store_raw_data (Union[Unset, None, bool]):  Default: True.
        ingest_source (Union[Unset, None, str]):
        container_type (Union[Unset, None, str]):
        multipart_data (BodyPutEntryByFileExactHashCollectionNameFilePut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        collection_name=collection_name,
        multipart_data=multipart_data,
        foreign_key=foreign_key,
        metadata=metadata,
        upsert=upsert,
        timestamp=timestamp,
        store_raw_data=store_raw_data,
        ingest_source=ingest_source,
        container_type=container_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_name: str,
    *,
    client: AuthenticatedClient,
    multipart_data: BodyPutEntryByFileExactHashCollectionNameFilePut,
    foreign_key: Union[None, Unset, int, str] = UNSET,
    metadata: Union[Unset, None, str] = UNSET,
    upsert: Union[Unset, None, bool] = False,
    timestamp: Union[Unset, None, str] = UNSET,
    store_raw_data: Union[Unset, None, bool] = True,
    ingest_source: Union[Unset, None, str] = UNSET,
    container_type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Put Entry By File

    Args:
        collection_name (str):
        foreign_key (Union[None, Unset, int, str]):
        metadata (Union[Unset, None, str]):
        upsert (Union[Unset, None, bool]):
        timestamp (Union[Unset, None, str]):
        store_raw_data (Union[Unset, None, bool]):  Default: True.
        ingest_source (Union[Unset, None, str]):
        container_type (Union[Unset, None, str]):
        multipart_data (BodyPutEntryByFileExactHashCollectionNameFilePut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        collection_name=collection_name,
        client=client,
        multipart_data=multipart_data,
        foreign_key=foreign_key,
        metadata=metadata,
        upsert=upsert,
        timestamp=timestamp,
        store_raw_data=store_raw_data,
        ingest_source=ingest_source,
        container_type=container_type,
    ).parsed


async def asyncio_detailed(
    collection_name: str,
    *,
    client: AuthenticatedClient,
    multipart_data: BodyPutEntryByFileExactHashCollectionNameFilePut,
    foreign_key: Union[None, Unset, int, str] = UNSET,
    metadata: Union[Unset, None, str] = UNSET,
    upsert: Union[Unset, None, bool] = False,
    timestamp: Union[Unset, None, str] = UNSET,
    store_raw_data: Union[Unset, None, bool] = True,
    ingest_source: Union[Unset, None, str] = UNSET,
    container_type: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    """Put Entry By File

    Args:
        collection_name (str):
        foreign_key (Union[None, Unset, int, str]):
        metadata (Union[Unset, None, str]):
        upsert (Union[Unset, None, bool]):
        timestamp (Union[Unset, None, str]):
        store_raw_data (Union[Unset, None, bool]):  Default: True.
        ingest_source (Union[Unset, None, str]):
        container_type (Union[Unset, None, str]):
        multipart_data (BodyPutEntryByFileExactHashCollectionNameFilePut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        collection_name=collection_name,
        multipart_data=multipart_data,
        foreign_key=foreign_key,
        metadata=metadata,
        upsert=upsert,
        timestamp=timestamp,
        store_raw_data=store_raw_data,
        ingest_source=ingest_source,
        container_type=container_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_name: str,
    *,
    client: AuthenticatedClient,
    multipart_data: BodyPutEntryByFileExactHashCollectionNameFilePut,
    foreign_key: Union[None, Unset, int, str] = UNSET,
    metadata: Union[Unset, None, str] = UNSET,
    upsert: Union[Unset, None, bool] = False,
    timestamp: Union[Unset, None, str] = UNSET,
    store_raw_data: Union[Unset, None, bool] = True,
    ingest_source: Union[Unset, None, str] = UNSET,
    container_type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Put Entry By File

    Args:
        collection_name (str):
        foreign_key (Union[None, Unset, int, str]):
        metadata (Union[Unset, None, str]):
        upsert (Union[Unset, None, bool]):
        timestamp (Union[Unset, None, str]):
        store_raw_data (Union[Unset, None, bool]):  Default: True.
        ingest_source (Union[Unset, None, str]):
        container_type (Union[Unset, None, str]):
        multipart_data (BodyPutEntryByFileExactHashCollectionNameFilePut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            collection_name=collection_name,
            client=client,
            multipart_data=multipart_data,
            foreign_key=foreign_key,
            metadata=metadata,
            upsert=upsert,
            timestamp=timestamp,
            store_raw_data=store_raw_data,
            ingest_source=ingest_source,
            container_type=container_type,
        )
    ).parsed
