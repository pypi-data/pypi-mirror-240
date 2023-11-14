from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_lookup_by_file_exact_lookup_file_collection_name_post import (
    BodyLookupByFileExactLookupFileCollectionNamePost,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    collection_name: str,
    *,
    multipart_data: BodyLookupByFileExactLookupFileCollectionNamePost,
) -> Dict[str, Any]:
    pass

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/exact/lookup/file/{collection_name}".format(
            collection_name=collection_name,
        ),
        "files": multipart_multipart_data,
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
    multipart_data: BodyLookupByFileExactLookupFileCollectionNamePost,
) -> Response[Union[Any, HTTPValidationError]]:
    """Lookup By File

     Lookup into a collection using a file

    Args:
        collection_name (str):
        multipart_data (BodyLookupByFileExactLookupFileCollectionNamePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        collection_name=collection_name,
        multipart_data=multipart_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_name: str,
    *,
    client: AuthenticatedClient,
    multipart_data: BodyLookupByFileExactLookupFileCollectionNamePost,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Lookup By File

     Lookup into a collection using a file

    Args:
        collection_name (str):
        multipart_data (BodyLookupByFileExactLookupFileCollectionNamePost):

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
    ).parsed


async def asyncio_detailed(
    collection_name: str,
    *,
    client: AuthenticatedClient,
    multipart_data: BodyLookupByFileExactLookupFileCollectionNamePost,
) -> Response[Union[Any, HTTPValidationError]]:
    """Lookup By File

     Lookup into a collection using a file

    Args:
        collection_name (str):
        multipart_data (BodyLookupByFileExactLookupFileCollectionNamePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        collection_name=collection_name,
        multipart_data=multipart_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_name: str,
    *,
    client: AuthenticatedClient,
    multipart_data: BodyLookupByFileExactLookupFileCollectionNamePost,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Lookup By File

     Lookup into a collection using a file

    Args:
        collection_name (str):
        multipart_data (BodyLookupByFileExactLookupFileCollectionNamePost):

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
        )
    ).parsed
