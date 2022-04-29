from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.task_address_feature import TaskAddressFeature
from ...models.task_address_features_list_category import TaskAddressFeaturesListCategory
from ...models.task_address_features_list_format import TaskAddressFeaturesListFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    assignee: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, TaskAddressFeaturesListCategory] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, TaskAddressFeaturesListFormat] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/task_address_features/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["account"] = account

    params["assignee"] = assignee

    json_category: Union[Unset, None, str] = UNSET
    if not isinstance(category, Unset):
        json_category = category.value if category else None

    params["category"] = json_category

    params["cursor"] = cursor

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["owner"] = owner

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[TaskAddressFeature]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_paginated_task_address_feature_list_item_data in _response_200:
            componentsschemas_paginated_task_address_feature_list_item = TaskAddressFeature.from_dict(
                componentsschemas_paginated_task_address_feature_list_item_data
            )

            response_200.append(componentsschemas_paginated_task_address_feature_list_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[TaskAddressFeature]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    assignee: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, TaskAddressFeaturesListCategory] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, TaskAddressFeaturesListFormat] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Response[List[TaskAddressFeature]]:
    """
    Args:
        account (Union[Unset, None, str]):
        assignee (Union[Unset, None, str]):
        category (Union[Unset, None, TaskAddressFeaturesListCategory]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, TaskAddressFeaturesListFormat]):
        owner (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[List[TaskAddressFeature]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        assignee=assignee,
        category=category,
        cursor=cursor,
        format_=format_,
        owner=owner,
        page_size=page_size,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    assignee: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, TaskAddressFeaturesListCategory] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, TaskAddressFeaturesListFormat] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Optional[List[TaskAddressFeature]]:
    """
    Args:
        account (Union[Unset, None, str]):
        assignee (Union[Unset, None, str]):
        category (Union[Unset, None, TaskAddressFeaturesListCategory]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, TaskAddressFeaturesListFormat]):
        owner (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[List[TaskAddressFeature]]
    """

    return sync_detailed(
        client=client,
        account=account,
        assignee=assignee,
        category=category,
        cursor=cursor,
        format_=format_,
        owner=owner,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    assignee: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, TaskAddressFeaturesListCategory] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, TaskAddressFeaturesListFormat] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Response[List[TaskAddressFeature]]:
    """
    Args:
        account (Union[Unset, None, str]):
        assignee (Union[Unset, None, str]):
        category (Union[Unset, None, TaskAddressFeaturesListCategory]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, TaskAddressFeaturesListFormat]):
        owner (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[List[TaskAddressFeature]]
    """

    kwargs = _get_kwargs(
        client=client,
        account=account,
        assignee=assignee,
        category=category,
        cursor=cursor,
        format_=format_,
        owner=owner,
        page_size=page_size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account: Union[Unset, None, str] = UNSET,
    assignee: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, TaskAddressFeaturesListCategory] = UNSET,
    cursor: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, TaskAddressFeaturesListFormat] = UNSET,
    owner: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Optional[List[TaskAddressFeature]]:
    """
    Args:
        account (Union[Unset, None, str]):
        assignee (Union[Unset, None, str]):
        category (Union[Unset, None, TaskAddressFeaturesListCategory]):
        cursor (Union[Unset, None, int]):
        format_ (Union[Unset, None, TaskAddressFeaturesListFormat]):
        owner (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[List[TaskAddressFeature]]
    """

    return (
        await asyncio_detailed(
            client=client,
            account=account,
            assignee=assignee,
            category=category,
            cursor=cursor,
            format_=format_,
            owner=owner,
            page_size=page_size,
        )
    ).parsed
