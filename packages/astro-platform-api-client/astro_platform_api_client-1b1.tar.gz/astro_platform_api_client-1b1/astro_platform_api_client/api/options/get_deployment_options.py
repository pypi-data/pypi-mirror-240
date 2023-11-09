from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deployment_options import DeploymentOptions
from ...models.error import Error
from ...models.get_deployment_options_cloud_provider import GetDeploymentOptionsCloudProvider
from ...models.get_deployment_options_deployment_type import GetDeploymentOptionsDeploymentType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    deployment_id: Union[Unset, None, str] = UNSET,
    deployment_type: Union[Unset, None, GetDeploymentOptionsDeploymentType] = UNSET,
    cloud_provider: Union[Unset, None, GetDeploymentOptionsCloudProvider] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["deploymentId"] = deployment_id

    json_deployment_type: Union[Unset, None, str] = UNSET
    if not isinstance(deployment_type, Unset):
        json_deployment_type = deployment_type.value if deployment_type else None

    params["deploymentType"] = json_deployment_type

    json_cloud_provider: Union[Unset, None, str] = UNSET
    if not isinstance(cloud_provider, Unset):
        json_cloud_provider = cloud_provider.value if cloud_provider else None

    params["cloudProvider"] = json_cloud_provider

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/organizations/{organizationId}/deployment-options".format(
            organizationId=organization_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeploymentOptions, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeploymentOptions.from_dict(response.json())

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
) -> Response[Union[DeploymentOptions, Error]]:
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
    deployment_id: Union[Unset, None, str] = UNSET,
    deployment_type: Union[Unset, None, GetDeploymentOptionsDeploymentType] = UNSET,
    cloud_provider: Union[Unset, None, GetDeploymentOptionsCloudProvider] = UNSET,
) -> Response[Union[DeploymentOptions, Error]]:
    """Get Deployment options

     Get the options available for configuring a Deployment.

    Args:
        organization_id (str):
        deployment_id (Union[Unset, None, str]):
        deployment_type (Union[Unset, None, GetDeploymentOptionsDeploymentType]):
        cloud_provider (Union[Unset, None, GetDeploymentOptionsCloudProvider]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeploymentOptions, Error]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        deployment_id=deployment_id,
        deployment_type=deployment_type,
        cloud_provider=cloud_provider,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    deployment_id: Union[Unset, None, str] = UNSET,
    deployment_type: Union[Unset, None, GetDeploymentOptionsDeploymentType] = UNSET,
    cloud_provider: Union[Unset, None, GetDeploymentOptionsCloudProvider] = UNSET,
) -> Optional[Union[DeploymentOptions, Error]]:
    """Get Deployment options

     Get the options available for configuring a Deployment.

    Args:
        organization_id (str):
        deployment_id (Union[Unset, None, str]):
        deployment_type (Union[Unset, None, GetDeploymentOptionsDeploymentType]):
        cloud_provider (Union[Unset, None, GetDeploymentOptionsCloudProvider]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeploymentOptions, Error]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        deployment_id=deployment_id,
        deployment_type=deployment_type,
        cloud_provider=cloud_provider,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    deployment_id: Union[Unset, None, str] = UNSET,
    deployment_type: Union[Unset, None, GetDeploymentOptionsDeploymentType] = UNSET,
    cloud_provider: Union[Unset, None, GetDeploymentOptionsCloudProvider] = UNSET,
) -> Response[Union[DeploymentOptions, Error]]:
    """Get Deployment options

     Get the options available for configuring a Deployment.

    Args:
        organization_id (str):
        deployment_id (Union[Unset, None, str]):
        deployment_type (Union[Unset, None, GetDeploymentOptionsDeploymentType]):
        cloud_provider (Union[Unset, None, GetDeploymentOptionsCloudProvider]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeploymentOptions, Error]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        deployment_id=deployment_id,
        deployment_type=deployment_type,
        cloud_provider=cloud_provider,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    deployment_id: Union[Unset, None, str] = UNSET,
    deployment_type: Union[Unset, None, GetDeploymentOptionsDeploymentType] = UNSET,
    cloud_provider: Union[Unset, None, GetDeploymentOptionsCloudProvider] = UNSET,
) -> Optional[Union[DeploymentOptions, Error]]:
    """Get Deployment options

     Get the options available for configuring a Deployment.

    Args:
        organization_id (str):
        deployment_id (Union[Unset, None, str]):
        deployment_type (Union[Unset, None, GetDeploymentOptionsDeploymentType]):
        cloud_provider (Union[Unset, None, GetDeploymentOptionsCloudProvider]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeploymentOptions, Error]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            deployment_id=deployment_id,
            deployment_type=deployment_type,
            cloud_provider=cloud_provider,
        )
    ).parsed
