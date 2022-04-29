from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.client_role import ClientRole
from ...models.client_roles_partial_update_format import ClientRolesPartialUpdateFormat
from ...models.patched_client_role import PatchedClientRole
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedClientRole,
    multipart_data: PatchedClientRole,
    json_body: PatchedClientRole,
    format_: Union[Unset, None, ClientRolesPartialUpdateFormat] = UNSET,
) -> Dict[str, Any]:
    url = "{}/client_roles/{id}/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ClientRole]:
    if response.status_code == 200:
        response_200 = ClientRole.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ClientRole]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedClientRole,
    multipart_data: PatchedClientRole,
    json_body: PatchedClientRole,
    format_: Union[Unset, None, ClientRolesPartialUpdateFormat] = UNSET,
) -> Response[ClientRole]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, ClientRolesPartialUpdateFormat]):
        multipart_data (PatchedClientRole):
        json_body (PatchedClientRole):

    Returns:
        Response[ClientRole]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        format_=format_,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedClientRole,
    multipart_data: PatchedClientRole,
    json_body: PatchedClientRole,
    format_: Union[Unset, None, ClientRolesPartialUpdateFormat] = UNSET,
) -> Optional[ClientRole]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, ClientRolesPartialUpdateFormat]):
        multipart_data (PatchedClientRole):
        json_body (PatchedClientRole):

    Returns:
        Response[ClientRole]
    """

    return sync_detailed(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedClientRole,
    multipart_data: PatchedClientRole,
    json_body: PatchedClientRole,
    format_: Union[Unset, None, ClientRolesPartialUpdateFormat] = UNSET,
) -> Response[ClientRole]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, ClientRolesPartialUpdateFormat]):
        multipart_data (PatchedClientRole):
        json_body (PatchedClientRole):

    Returns:
        Response[ClientRole]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
        format_=format_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedClientRole,
    multipart_data: PatchedClientRole,
    json_body: PatchedClientRole,
    format_: Union[Unset, None, ClientRolesPartialUpdateFormat] = UNSET,
) -> Optional[ClientRole]:
    """
    Args:
        id (str):
        format_ (Union[Unset, None, ClientRolesPartialUpdateFormat]):
        multipart_data (PatchedClientRole):
        json_body (PatchedClientRole):

    Returns:
        Response[ClientRole]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
            format_=format_,
        )
    ).parsed
