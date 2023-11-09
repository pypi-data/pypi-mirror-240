from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_dedicated_deployment_request import CreateDedicatedDeploymentRequest
from ...models.create_hybrid_deployment_request import CreateHybridDeploymentRequest
from ...models.create_standard_deployment_request import CreateStandardDeploymentRequest
from ...models.deployment import Deployment
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    organization_id: str,
    *,
    json_body: Union[
        "CreateDedicatedDeploymentRequest", "CreateHybridDeploymentRequest", "CreateStandardDeploymentRequest"
    ],
) -> Dict[str, Any]:
    pass

    json_json_body: Dict[str, Any]

    if isinstance(json_body, CreateDedicatedDeploymentRequest):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, CreateHybridDeploymentRequest):
        json_json_body = json_body.to_dict()

    else:
        json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/organizations/{organizationId}/deployments".format(
            organizationId=organization_id,
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
    *,
    client: AuthenticatedClient,
    json_body: Union[
        "CreateDedicatedDeploymentRequest", "CreateHybridDeploymentRequest", "CreateStandardDeploymentRequest"
    ],
) -> Response[Union[Deployment, Error]]:
    """Create a Deployment

     Create a Deployment in the Organization. An Astro Deployment is an Airflow environment that is
    powered by all core Airflow components.

    Args:
        organization_id (str):
        json_body (Union['CreateDedicatedDeploymentRequest', 'CreateHybridDeploymentRequest',
            'CreateStandardDeploymentRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Deployment, Error]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Union[
        "CreateDedicatedDeploymentRequest", "CreateHybridDeploymentRequest", "CreateStandardDeploymentRequest"
    ],
) -> Optional[Union[Deployment, Error]]:
    """Create a Deployment

     Create a Deployment in the Organization. An Astro Deployment is an Airflow environment that is
    powered by all core Airflow components.

    Args:
        organization_id (str):
        json_body (Union['CreateDedicatedDeploymentRequest', 'CreateHybridDeploymentRequest',
            'CreateStandardDeploymentRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Deployment, Error]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Union[
        "CreateDedicatedDeploymentRequest", "CreateHybridDeploymentRequest", "CreateStandardDeploymentRequest"
    ],
) -> Response[Union[Deployment, Error]]:
    """Create a Deployment

     Create a Deployment in the Organization. An Astro Deployment is an Airflow environment that is
    powered by all core Airflow components.

    Args:
        organization_id (str):
        json_body (Union['CreateDedicatedDeploymentRequest', 'CreateHybridDeploymentRequest',
            'CreateStandardDeploymentRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Deployment, Error]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Union[
        "CreateDedicatedDeploymentRequest", "CreateHybridDeploymentRequest", "CreateStandardDeploymentRequest"
    ],
) -> Optional[Union[Deployment, Error]]:
    """Create a Deployment

     Create a Deployment in the Organization. An Astro Deployment is an Airflow environment that is
    powered by all core Airflow components.

    Args:
        organization_id (str):
        json_body (Union['CreateDedicatedDeploymentRequest', 'CreateHybridDeploymentRequest',
            'CreateStandardDeploymentRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Deployment, Error]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
