from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_organizations_product import ListOrganizationsProduct
from ...models.list_organizations_sorts_item import ListOrganizationsSortsItem
from ...models.list_organizations_support_plan import ListOrganizationsSupportPlan
from ...models.organizations_paginated import OrganizationsPaginated
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    support_plan: Union[Unset, None, ListOrganizationsSupportPlan] = UNSET,
    product: Union[Unset, None, ListOrganizationsProduct] = UNSET,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    sorts: Union[Unset, None, List[ListOrganizationsSortsItem]] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_support_plan: Union[Unset, None, str] = UNSET
    if not isinstance(support_plan, Unset):
        json_support_plan = support_plan.value if support_plan else None

    params["supportPlan"] = json_support_plan

    json_product: Union[Unset, None, str] = UNSET
    if not isinstance(product, Unset):
        json_product = product.value if product else None

    params["product"] = json_product

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
        "url": "/organizations",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, OrganizationsPaginated]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OrganizationsPaginated.from_dict(response.json())

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
) -> Response[Union[Error, OrganizationsPaginated]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    support_plan: Union[Unset, None, ListOrganizationsSupportPlan] = UNSET,
    product: Union[Unset, None, ListOrganizationsProduct] = UNSET,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    sorts: Union[Unset, None, List[ListOrganizationsSortsItem]] = UNSET,
) -> Response[Union[Error, OrganizationsPaginated]]:
    """List Organizations

     List the details about all Organizations that you have access to. Requires using a personal access
    token (PAT) for authentication.

    Args:
        support_plan (Union[Unset, None, ListOrganizationsSupportPlan]):
        product (Union[Unset, None, ListOrganizationsProduct]):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.
        sorts (Union[Unset, None, List[ListOrganizationsSortsItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, OrganizationsPaginated]]
    """

    kwargs = _get_kwargs(
        support_plan=support_plan,
        product=product,
        offset=offset,
        limit=limit,
        sorts=sorts,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    support_plan: Union[Unset, None, ListOrganizationsSupportPlan] = UNSET,
    product: Union[Unset, None, ListOrganizationsProduct] = UNSET,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    sorts: Union[Unset, None, List[ListOrganizationsSortsItem]] = UNSET,
) -> Optional[Union[Error, OrganizationsPaginated]]:
    """List Organizations

     List the details about all Organizations that you have access to. Requires using a personal access
    token (PAT) for authentication.

    Args:
        support_plan (Union[Unset, None, ListOrganizationsSupportPlan]):
        product (Union[Unset, None, ListOrganizationsProduct]):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.
        sorts (Union[Unset, None, List[ListOrganizationsSortsItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, OrganizationsPaginated]
    """

    return sync_detailed(
        client=client,
        support_plan=support_plan,
        product=product,
        offset=offset,
        limit=limit,
        sorts=sorts,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    support_plan: Union[Unset, None, ListOrganizationsSupportPlan] = UNSET,
    product: Union[Unset, None, ListOrganizationsProduct] = UNSET,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    sorts: Union[Unset, None, List[ListOrganizationsSortsItem]] = UNSET,
) -> Response[Union[Error, OrganizationsPaginated]]:
    """List Organizations

     List the details about all Organizations that you have access to. Requires using a personal access
    token (PAT) for authentication.

    Args:
        support_plan (Union[Unset, None, ListOrganizationsSupportPlan]):
        product (Union[Unset, None, ListOrganizationsProduct]):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.
        sorts (Union[Unset, None, List[ListOrganizationsSortsItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, OrganizationsPaginated]]
    """

    kwargs = _get_kwargs(
        support_plan=support_plan,
        product=product,
        offset=offset,
        limit=limit,
        sorts=sorts,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    support_plan: Union[Unset, None, ListOrganizationsSupportPlan] = UNSET,
    product: Union[Unset, None, ListOrganizationsProduct] = UNSET,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    sorts: Union[Unset, None, List[ListOrganizationsSortsItem]] = UNSET,
) -> Optional[Union[Error, OrganizationsPaginated]]:
    """List Organizations

     List the details about all Organizations that you have access to. Requires using a personal access
    token (PAT) for authentication.

    Args:
        support_plan (Union[Unset, None, ListOrganizationsSupportPlan]):
        product (Union[Unset, None, ListOrganizationsProduct]):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.
        sorts (Union[Unset, None, List[ListOrganizationsSortsItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, OrganizationsPaginated]
    """

    return (
        await asyncio_detailed(
            client=client,
            support_plan=support_plan,
            product=product,
            offset=offset,
            limit=limit,
            sorts=sorts,
        )
    ).parsed
