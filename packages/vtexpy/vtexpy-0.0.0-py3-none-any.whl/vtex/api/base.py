from logging import getLogger
from typing import Dict, Optional


class BaseAPI:
    """
    Base client for all VTEX API collections.
    """

    _BASE_URL = "https://{account_name}.{environment}.com.br/{endpoint}"
    _APP_KEY_HEADER = "X-VTEX-API-AppKey"
    _APP_TOKEN_HEADER = "X-VTEX-API-AppToken"
    _DEFAULT_TIMEOUT = 60.0

    def __init__(
        self: "BaseAPI",
        account_name: Optional[str] = None,
        app_key: Optional[str] = None,
        app_token: Optional[str] = None,
        environment: Optional[str] = None,
    ) -> None:
        self._account_name = account_name
        self._app_key = app_key
        self._app_token = app_token
        self._environment = environment
        self._logger = getLogger(type(self).__name__)

    # def _make_request(
    #     self: "BaseAPI",
    #     *,
    #     method: Callable[..., Response],
    #     domain: str,
    #     endpoint: str,
    #     subdomain: str | None = None,
    #     **kwargs: Any,
    # ) -> VTEXResponseDTO:
    #     kwargs["headers"] = {**kwargs.get("headers", {}), **self._get_headers()}
    #     kwargs["timeout"] = kwargs.get("timeout", self.DEFAULT_TIMEOUT)
    #
    #     url = self._get_url(
    #         subdomain=subdomain or self._subdomain,
    #         domain=domain,
    #         endpoint=endpoint,
    #     )
    #     try:
    #         response = method(url, **kwargs)
    #     except HTTPError as exception:
    #         with logger.contextualize(
    #             request={
    #                 "method": method,
    #                 "url": url,
    #                 "kwargs": self._omit_secrets(**kwargs),
    #             },
    #         ):
    #             logger.error("Error calling VTEX API")
    #
    #         raise VTEXError(str(exception)) from None
    #
    #     if not response.is_success:
    #         with logger.contextualize(
    #             request={
    #                 "method": method,
    #                 "url": url,
    #                 "kwargs": self._omit_secrets(**kwargs),
    #             },
    #             response={
    #                 "data": response.content.decode("utf-8"),
    #                 "status": response.status_code,
    #                 "headers": dict(response.headers),
    #             },
    #         ):
    #             logger.error(f"VTEX API returned status {response.status_code}")
    #
    #         exception = VTEXError(response.content.decode("utf-8"))
    #         if celery_app.current_task:
    #             if response.status_code == 429:
    #                 exception = VTEXTooManyRequestsError(
    #                     retry_after=int(
    #                         response.headers.get(
    #                             "retry-after",
    #                             VTEXTooManyRequestsError.retry_after,
    #                         ),
    #                     ),
    #                 )
    #             elif response.is_server_error:
    #                 exception = VTEXServerError()
    #
    #             if hasattr(exception, "retry_after"):
    #                 raise celery_app.current_task.retry(
    #                     exc=exception,
    #                     countdown=exception.retry_after,
    #                     queue=get_queue(task=celery_app.current_task),
    #                 )
    #
    #         raise exception

    def _get_url(
        self:  "BaseAPI",
        endpoint: str,
        account_name: Optional[str] = None,
        environment: Optional[str] = None,
    ) -> str:
        if not (account_name or self._account_name):
            raise ValueError("Missing account_name")

        if not (environment or self._environment):
            raise ValueError("Missing environment")

        return self._BASE_URL.format(
            endpoint=endpoint,
            account_name=account_name or self._account_name,
            environment=environment or self._environment,
        )

    def _get_headers(
        self:  "BaseAPI",
        app_key: Optional[str] = None,
        app_token: Optional[str] = None,
    ) -> Dict[str, str]:
        if not (app_key or self._app_key):
            raise ValueError("Missing app_key")

        if not (app_token or self._app_token):
            raise ValueError("Missing app_token")

        return {
            "Content-Type": "application/json",
            self._APP_KEY_HEADER: app_key or self._app_key,
            self._APP_TOKEN_HEADER: app_token or self._app_token,
        }

