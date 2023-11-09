from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cluster import Cluster
from ...models.error import Error
from ...models.update_cluster_request import UpdateClusterRequest
from ...types import Response


def _get_kwargs(
    organization_id: str,
    cluster_id: str,
    *,
    json_body: UpdateClusterRequest,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/organizations/{organizationId}/clusters/{clusterId}".format(
            organizationId=organization_id,
            clusterId=cluster_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Cluster, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Cluster.from_dict(response.json())

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
    if response.status_code == HTTPStatus.PRECONDITION_FAILED:
        response_412 = Error.from_dict(response.json())

        return response_412
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Cluster, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    cluster_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateClusterRequest,
) -> Response[Union[Cluster, Error]]:
    """Update a cluster

     Update a cluster in the Organization.

    Args:
        organization_id (str):
        cluster_id (str):
        json_body (UpdateClusterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Cluster, Error]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        cluster_id=cluster_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    cluster_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateClusterRequest,
) -> Optional[Union[Cluster, Error]]:
    """Update a cluster

     Update a cluster in the Organization.

    Args:
        organization_id (str):
        cluster_id (str):
        json_body (UpdateClusterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Cluster, Error]
    """

    return sync_detailed(
        organization_id=organization_id,
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    cluster_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateClusterRequest,
) -> Response[Union[Cluster, Error]]:
    """Update a cluster

     Update a cluster in the Organization.

    Args:
        organization_id (str):
        cluster_id (str):
        json_body (UpdateClusterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Cluster, Error]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        cluster_id=cluster_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    cluster_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateClusterRequest,
) -> Optional[Union[Cluster, Error]]:
    """Update a cluster

     Update a cluster in the Organization.

    Args:
        organization_id (str):
        cluster_id (str):
        json_body (UpdateClusterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Cluster, Error]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            cluster_id=cluster_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
