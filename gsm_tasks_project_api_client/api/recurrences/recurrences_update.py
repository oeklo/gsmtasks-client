from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.recurrence import Recurrence
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: Recurrence,
    multipart_data: Recurrence,
    json_body: Recurrence,
) -> Dict[str, Any]:
    url = "{}/recurrences/{id}/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Recurrence]:
    if response.status_code == 200:
        response_200 = Recurrence.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Recurrence]:
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
    form_data: Recurrence,
    multipart_data: Recurrence,
    json_body: Recurrence,
) -> Response[Recurrence]:
    """
    Args:
        id (str):
        multipart_data (Recurrence):
        json_body (Recurrence):

    Returns:
        Response[Recurrence]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
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
    form_data: Recurrence,
    multipart_data: Recurrence,
    json_body: Recurrence,
) -> Optional[Recurrence]:
    """
    Args:
        id (str):
        multipart_data (Recurrence):
        json_body (Recurrence):

    Returns:
        Response[Recurrence]
    """

    return sync_detailed(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: Recurrence,
    multipart_data: Recurrence,
    json_body: Recurrence,
) -> Response[Recurrence]:
    """
    Args:
        id (str):
        multipart_data (Recurrence):
        json_body (Recurrence):

    Returns:
        Response[Recurrence]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    form_data: Recurrence,
    multipart_data: Recurrence,
    json_body: Recurrence,
) -> Optional[Recurrence]:
    """
    Args:
        id (str):
        multipart_data (Recurrence):
        json_body (Recurrence):

    Returns:
        Response[Recurrence]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
