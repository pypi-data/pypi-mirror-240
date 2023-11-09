from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.clusters_paginated import ClustersPaginated
from ...models.error import Error
from ...models.list_clusters_provider import ListClustersProvider
from ...models.list_clusters_sorts_item import ListClustersSortsItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    provider: Union[Unset, None, ListClustersProvider] = UNSET,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    sorts: Union[Unset, None, List[ListClustersSortsItem]] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_provider: Union[Unset, None, str] = UNSET
    if not isinstance(provider, Unset):
        json_provider = provider.value if provider else None

    params["provider"] = json_provider

    params["offset"] = offset

    params["limit"] = limit

    json_sorts: Union[Unset, None, List[str]] = UNSET
    if not isinstance(sorts, Unset):
        if sorts is None:
            json_sorts = None
        else:
            json_sorts = []
            for sorts_item_data in sorts:
                sorts_item = sorts_item_data.value

                json_sorts.append(sorts_item)

    params["sorts"] = json_sorts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/organizations/{organizationId}/clusters".format(
            organizationId=organization_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClustersPaginated, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ClustersPaginated.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ClustersPaginated, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    provider: Union[Unset, None, ListClustersProvider] = UNSET,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    sorts: Union[Unset, None, List[ListClustersSortsItem]] = UNSET,
) -> Response[Union[ClustersPaginated, Error]]:
    """List clusters

     List clusters in an Organization.

    Args:
        organization_id (str):
        provider (Union[Unset, None, ListClustersProvider]):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.
        sorts (Union[Unset, None, List[ListClustersSortsItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClustersPaginated, Error]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        provider=provider,
        offset=offset,
        limit=limit,
        sorts=sorts,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    provider: Union[Unset, None, ListClustersProvider] = UNSET,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    sorts: Union[Unset, None, List[ListClustersSortsItem]] = UNSET,
) -> Optional[Union[ClustersPaginated, Error]]:
    """List clusters

     List clusters in an Organization.

    Args:
        organization_id (str):
        provider (Union[Unset, None, ListClustersProvider]):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.
        sorts (Union[Unset, None, List[ListClustersSortsItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClustersPaginated, Error]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        provider=provider,
        offset=offset,
        limit=limit,
        sorts=sorts,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    provider: Union[Unset, None, ListClustersProvider] = UNSET,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    sorts: Union[Unset, None, List[ListClustersSortsItem]] = UNSET,
) -> Response[Union[ClustersPaginated, Error]]:
    """List clusters

     List clusters in an Organization.

    Args:
        organization_id (str):
        provider (Union[Unset, None, ListClustersProvider]):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.
        sorts (Union[Unset, None, List[ListClustersSortsItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClustersPaginated, Error]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        provider=provider,
        offset=offset,
        limit=limit,
        sorts=sorts,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    provider: Union[Unset, None, ListClustersProvider] = UNSET,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    sorts: Union[Unset, None, List[ListClustersSortsItem]] = UNSET,
) -> Optional[Union[ClustersPaginated, Error]]:
    """List clusters

     List clusters in an Organization.

    Args:
        organization_id (str):
        provider (Union[Unset, None, ListClustersProvider]):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.
        sorts (Union[Unset, None, List[ListClustersSortsItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClustersPaginated, Error]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            provider=provider,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
    ).parsed
