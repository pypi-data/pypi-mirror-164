"""Module for handling the different types of MarketPlace apps and their
capabilities.
.. currentmodule:: marketplace.app
.. moduleauthor:: Pablo de Andres, Pranjali Singh (Fraunhofer IWM)
"""
import warnings

from packaging.version import parse

from ..client import MarketPlaceClient
from .utils import camel_to_snake
from .v0 import MarketPlaceApp as _MarketPlaceApp_v0
from .v0_0_1 import MarketPlaceApp as _MarketPlaceApp_v0_0_1


class MarketPlaceApp(_MarketPlaceApp_v0_0_1):
    def __init__(self, *args, **kwargs):
        warnings.warn(
            "The MarketPlaceApp class is deprecated as of v0.2.0 and will be "
            "removed in v1. Please use the get_app() function instead."
        )
        super().__init__(*args, **kwargs)


def get_app(app_id, marketplace_host_url=None, access_token=None, **kwargs):
    """Get an app instance.
    Args:
        app_id (str): client id of the app
        **kwargs: keyword arguments for the app
    Returns:
        MarketPlaceApp: app instance
    """
    client = MarketPlaceClient(
        marketplace_host_url=marketplace_host_url, access_token=access_token
    )

    # Getting api version and list of capabilities for the application

    app_service_path = f"application-service/applications/{app_id}"
    app_info = client.get(path=app_service_path).json()
    app_api_version = parse(app_info["api_version"])

    capabilities = []
    for capability in app_info["capabilities"]:
        capabilities.append(camel_to_snake(capability["name"]))

    if app_api_version == parse("0.0.1"):
        return _MarketPlaceApp_v0_0_1(
            app_id,
            marketplace_host_url=marketplace_host_url,
            access_token=access_token,
            capabilities=capabilities,
            **kwargs,
        )
    elif parse("0.0.1") < app_api_version <= parse("0.3.0"):
        return _MarketPlaceApp_v0(client, app_id, app_info, **kwargs)
    else:
        raise RuntimeError(f"App API version ({app_api_version}) not supported.")


__all__ = [
    "MarketPlaceApp",
]
