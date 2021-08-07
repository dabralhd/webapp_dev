import connexion
import six

from swagger_server.models.app_creation_result import AppCreationResult  # noqa: E501
from swagger_server.models.app_manager_error import AppManagerError  # noqa: E501
from swagger_server.models.app_target import AppTarget  # noqa: E501
from swagger_server.models.app_type import AppType  # noqa: E501
from swagger_server.models.application import Application  # noqa: E501
from swagger_server.models.set_env_result import SetEnvResult  # noqa: E501
from swagger_server import util


def create(app_name, user_uuid, app_type, app_target, dnn_model_name=None, app_code=None, board_name=None):  # noqa: E501
    """crete a new application instance

    create a app-instance by importing a NN model # noqa: E501

    :param app_name: string representing name of demonstration to create
    :type app_name: str
    :param user_uuid: id of the user creating the application
    :type user_uuid: str
    :param app_type: type of application e.g. sesor, audio, video etc.
    :type app_type: dict | bytes
    :param app_target: target on which applicaiton can run e.g. PC, board, both
    :type app_target: dict | bytes
    :param dnn_model_name: 
    :type dnn_model_name: strstr
    :param app_code: 
    :type app_code: strstr
    :param board_name: board on which this applicaiton is supported
    :type board_name: str

    :rtype: Application
    """
    if connexion.request.is_json:
        app_type = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        app_target = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def retrieve(app_uuid, user_uuid=None):  # noqa: E501
    """set execution environment and executes a given application

    This command executes a given demo on PC. # noqa: E501

    :param app_uuid: universal unique id of the demo
    :type app_uuid: str
    :param user_uuid: universal unique id of the user who is retrieving the demo application
    :type user_uuid: str

    :rtype: AppCreationResult
    """
    return 'do some magic!'


def retrieve_0(app_uuid, user_uuid=None):  # noqa: E501
    """retrieve metadata about an application

    This command retrieves metadata about an application # noqa: E501

    :param app_uuid: universal unique id of the demo
    :type app_uuid: str
    :param user_uuid: universal unique id of the user who is retrieving the demo application
    :type user_uuid: str

    :rtype: AppCreationResult
    """
    return 'do some magic!'


def setenv(app_uuid):  # noqa: E501
    """set execution environment

    This command sets the execution environment for a given application # noqa: E501

    :param app_uuid: universal unique id of the demo
    :type app_uuid: str

    :rtype: SetEnvResult
    """
    return 'do some magic!'
