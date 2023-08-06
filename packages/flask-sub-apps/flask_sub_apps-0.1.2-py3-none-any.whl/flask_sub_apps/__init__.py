import logging
from typing import Iterable, Union, List

import flask
from flask import Flask

from flask_sub_apps import helpers, config
from flask_sub_apps.loader import ValidateFunction
from flask_sub_apps.models import SubApp
from flask_sub_apps.registry import AppRegistry


class FlaskSubApps:
    def __init__(
        self,
        app: flask.Flask = None,
        installed_sub_apps: List[str] = None,
        models_file: Union[str, List[str]] = None,
        commands_file: Union[str, List[str]] = None,
        routers_file: Union[str, List[str]] = None,
        registry: AppRegistry = None,
        is_valid_model: ValidateFunction = None,
        is_valid_command: ValidateFunction = None,
        is_valid_router: ValidateFunction = None,
        model_class: type = None,
        router_class: type = None,
        command_class: type = None,
    ):
        """
        Initialize FlaskSubApps extension.
        All arguments are optional except for app and defaults values are provided.

        :param app: Flask app to initialize FlaskSubApps with.
        :param installed_sub_apps: List of sub apps to install.
        :param models_file: Path to models file. List of paths is also accepted.
        :param commands_file: Path to commands module. List of paths is also accepted.
        :param routers_file: Path to routers module. List of paths is also accepted.
        :param registry: Instance of app registry to use.
        :param is_valid_model: Function to validate model.
        :param is_valid_command: Function to validate command.
        :param is_valid_router: Function to validate router.
        :param model_class: Model class to look for.
        :param router_class: Router class to look for.
        :param command_class: Command class to look for.
        """
        self._app = app
        self._registry: AppRegistry = registry or AppRegistry(
            is_valid_model=is_valid_model,
            is_valid_command=is_valid_command,
            is_valid_router=is_valid_router,
        )
        self._installed_sub_apps = installed_sub_apps or []
        self.init_config(
            models_file,
            commands_file,
            routers_file,
            model_class,
            router_class,
            command_class,
        )

        if app is not None:
            self.init_app(app)

    def init_app(self, flask_app: Flask):
        assert self._app is None, "FlaskSubApps already initialized."
        assert flask_app is not None, "Flask app is required."

        self._app = flask_app

        for module_name in self._installed_sub_apps:
            self._registry.register(module_name, flask_app=self._app)

        logging.info(
            f"Registered [{', '.join(map(helpers.in_quotes, self._registry.get_sub_apps()))}] sub-apps."
        )

    @property
    def routers(self):
        """Get all registered routers."""
        return self._registry.get_routers()

    @property
    def commands(self):
        """Get all registered commands."""
        return self._registry.get_commands()

    @property
    def models(self):
        """Get all registered models."""
        return self._registry.get_models()

    def get_model(self, model_name: str):
        """
        Get model by its name.

        :param model_name: Name of the model to find.
        :return: Model class if exists, None otherwise.
        """
        return self._registry.get_model(model_name)

    def __iter__(self) -> Iterable[SubApp]:
        return iter(self._registry.get_sub_apps())

    @staticmethod
    def init_config(
        models_file: str,
        commands_file: str,
        routers_file: str,
        model_class: type,
        router_class: type,
        command_class: type,
    ):
        """
        Initialize config with user defined config files.
        """
        if models_file is not None:
            config.MODELS_FILE = models_file
        if commands_file is not None:
            config.COMMANDS_FILE = commands_file
        if routers_file is not None:
            config.ROUTERS_FILE = routers_file
        if model_class is not None:
            config.DBModel = model_class
        if router_class is not None:
            config.Router = router_class
        if command_class is not None:
            config.Command = command_class
