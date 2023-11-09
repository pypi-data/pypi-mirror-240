from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cluster_options import ClusterOptions
from ...models.error import Error
from ...models.get_cluster_options_provider import GetClusterOptionsProvider
from ...models.get_cluster_options_type import GetClusterOptionsType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    provider: Union[Unset, None, GetClusterOptionsProvider] = UNSET,
    type: GetClusterOptionsType,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_provider: Union[Unset, None, str] = UNSET
    if not isinstance(provider, Unset):
        json_provider = provider.value if provider else None

    params["provider"] = json_provider

    json_type = type.value

    params["type"] = json_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/organizations/{organizationId}/cluster-options".format(
            organizationId=organization_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, List["ClusterOptions"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ClusterOptions.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, List["ClusterOptions"]]]:
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
    provider: Union[Unset, None, GetClusterOptionsProvider] = UNSET,
    type: GetClusterOptionsType,
) -> Response[Union[Error, List["ClusterOptions"]]]:
    """Get cluster options

     Get all possible options for configuring a cluster.

    Args:
        organization_id (str):
        provider (Union[Unset, None, GetClusterOptionsProvider]):
        type (GetClusterOptionsType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['ClusterOptions']]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        provider=provider,
        type=type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    provider: Union[Unset, None, GetClusterOptionsProvider] = UNSET,
    type: GetClusterOptionsType,
) -> Optional[Union[Error, List["ClusterOptions"]]]:
    """Get cluster options

     Get all possible options for configuring a cluster.

    Args:
        organization_id (str):
        provider (Union[Unset, None, GetClusterOptionsProvider]):
        type (GetClusterOptionsType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, List['ClusterOptions']]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        provider=provider,
        type=type,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    provider: Union[Unset, None, GetClusterOptionsProvider] = UNSET,
    type: GetClusterOptionsType,
) -> Response[Union[Error, List["ClusterOptions"]]]:
    """Get cluster options

     Get all possible options for configuring a cluster.

    Args:
        organization_id (str):
        provider (Union[Unset, None, GetClusterOptionsProvider]):
        type (GetClusterOptionsType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, List['ClusterOptions']]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        provider=provider,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    provider: Union[Unset, None, GetClusterOptionsProvider] = UNSET,
    type: GetClusterOptionsType,
) -> Optional[Union[Error, List["ClusterOptions"]]]:
    """Get cluster options

     Get all possible options for configuring a cluster.

    Args:
        organization_id (str):
        provider (Union[Unset, None, GetClusterOptionsProvider]):
        type (GetClusterOptionsType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, List['ClusterOptions']]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            provider=provider,
            type=type,
        )
    ).parsed
