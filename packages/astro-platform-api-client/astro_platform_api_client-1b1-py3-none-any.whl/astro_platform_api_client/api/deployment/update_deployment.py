from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deployment import Deployment
from ...models.error import Error
from ...models.update_dedicated_deployment_request import UpdateDedicatedDeploymentRequest
from ...models.update_hybrid_deployment_request import UpdateHybridDeploymentRequest
from ...models.update_standard_deployment_request import UpdateStandardDeploymentRequest
from ...types import Response


def _get_kwargs(
    organization_id: str,
    deployment_id: str,
    *,
    json_body: Union[
        "UpdateDedicatedDeploymentRequest", "UpdateHybridDeploymentRequest", "UpdateStandardDeploymentRequest"
    ],
) -> Dict[str, Any]:
    pass

    json_json_body: Dict[str, Any]

    if isinstance(json_body, UpdateDedicatedDeploymentRequest):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, UpdateHybridDeploymentRequest):
        json_json_body = json_body.to_dict()

    else:
        json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/organizations/{organizationId}/deployments/{deploymentId}".format(
            organizationId=organization_id,
            deploymentId=deployment_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Deployment, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Deployment.from_dict(response.json())

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
) -> Response[Union[Deployment, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    deployment_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Union[
        "UpdateDedicatedDeploymentRequest", "UpdateHybridDeploymentRequest", "UpdateStandardDeploymentRequest"
    ],
) -> Response[Union[Deployment, Error]]:
    """Update a Deployment

     Update a Deployment in the Organization.

    Args:
        organization_id (str):
        deployment_id (str):
        json_body (Union['UpdateDedicatedDeploymentRequest', 'UpdateHybridDeploymentRequest',
            'UpdateStandardDeploymentRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Deployment, Error]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        deployment_id=deployment_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    deployment_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Union[
        "UpdateDedicatedDeploymentRequest", "UpdateHybridDeploymentRequest", "UpdateStandardDeploymentRequest"
    ],
) -> Optional[Union[Deployment, Error]]:
    """Update a Deployment

     Update a Deployment in the Organization.

    Args:
        organization_id (str):
        deployment_id (str):
        json_body (Union['UpdateDedicatedDeploymentRequest', 'UpdateHybridDeploymentRequest',
            'UpdateStandardDeploymentRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Deployment, Error]
    """

    return sync_detailed(
        organization_id=organization_id,
        deployment_id=deployment_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    deployment_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Union[
        "UpdateDedicatedDeploymentRequest", "UpdateHybridDeploymentRequest", "UpdateStandardDeploymentRequest"
    ],
) -> Response[Union[Deployment, Error]]:
    """Update a Deployment

     Update a Deployment in the Organization.

    Args:
        organization_id (str):
        deployment_id (str):
        json_body (Union['UpdateDedicatedDeploymentRequest', 'UpdateHybridDeploymentRequest',
            'UpdateStandardDeploymentRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Deployment, Error]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        deployment_id=deployment_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    deployment_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Union[
        "UpdateDedicatedDeploymentRequest", "UpdateHybridDeploymentRequest", "UpdateStandardDeploymentRequest"
    ],
) -> Optional[Union[Deployment, Error]]:
    """Update a Deployment

     Update a Deployment in the Organization.

    Args:
        organization_id (str):
        deployment_id (str):
        json_body (Union['UpdateDedicatedDeploymentRequest', 'UpdateHybridDeploymentRequest',
            'UpdateStandardDeploymentRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Deployment, Error]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            deployment_id=deployment_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
