import os
import inspect
import copy
import time
import math
from typing import List, Union, Any, Literal
import requests
from .package_schemas import *
from .logging import setup_logger

# Get the custom logger
logger = setup_logger()


#####
# Exceptions
#####
class ComposoException(Exception):
    pass


# A composo user exception is cause by the user doing something wrong that that platform hasn't prevented them from doing. We should tell them somehow.
class ComposoUserException(ComposoException):
    pass


class ComposoCriticalException(ComposoException):
    pass


class ComposoDeveloperException(ComposoException):
    pass


#####
# Types
#####
class StrParam(str):
    def __new__(cls, description, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.description = description
        return obj

    def get_constraint_string(self):
        return None

    def validate(self, item):
        return

    @staticmethod
    def type_string():
        return "str"


class IntParam(int):
    def __new__(cls, description=None, min=None, max=None, *args, **kwargs):
        # Create an instance of the IntParam class
        obj = super().__new__(cls, *args, **kwargs)
        obj.description = description
        obj.min = min
        obj.max = max
        return obj

    def get_constraint_string(self):
        constraint_str = ""
        if self.min is not None:
            constraint_str += f"min:{str(self.min)}"
            if self.max is not None:
                constraint_str += "; "
        if self.max is not None:
            constraint_str += f"max:{str(self.max)}"
        return constraint_str

    def validate(self, value):
        if self.min and not value > self.min:
            raise ComposoUserException(
                f"Parameter is invalid. Value {value} does not exceed minimum value: {self.min}"
            )

        if self.max and not value < self.max:
            raise ComposoUserException(
                f"Parameter is invalid. Value {value} exceeds maximum value: {self.max}"
            )

        return True

    @staticmethod
    def type_string():
        return "int"


class FloatParam(float):
    def __new__(cls, description=None, min=None, max=None, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.description = description
        obj.min = min
        obj.max = max
        return obj

    def get_constraint_string(self):
        constraint_str = ""
        if self.min is not None:
            constraint_str += f"min:{str(self.min)}"
            if self.max is not None:
                constraint_str += "; "
        if self.max is not None:
            constraint_str += f"max:{str(self.max)}"
        return constraint_str

    def validate(self, value):
        if self.min and not value > self.min:
            raise ComposoUserException(
                f"Parameter is invalid. Value {value} does not exceed minimum value: {self.min}"
            )

        if self.max and not value < self.max:
            raise ComposoUserException(
                f"Parameter is invalid. Value {value} exceeds maximum value: {self.max}"
            )

        return True

    @staticmethod
    def type_string():
        return "float"


class MultiChoiceParam(str):
    def __new__(cls, choices: List[str] = None, description=None, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.description = description
        obj.choices = choices
        return obj

    def get_constraint_string(self):
        return f"options: {'; '.join(self.choices)}"

    def validate(self, value):
        if value not in self.choices:
            raise ComposoUserException(
                f"Parameter is invalid. Value {value} is not in the list of allowable values: {self.choices}"
            )

        return True

    @staticmethod
    def type_string():
        return "multichoice"


WORKABLE_TYPES = Union[StrParam, IntParam, FloatParam, MultiChoiceParam]


##### Event Ingress and Egress
class BackendEventGress:
    backend_url: str

    def __init__(self, app_registration: AppRegistration) -> None:
        self.app_registration = app_registration

        if os.environ.get("PACKAGE_ENV", "prod") == "local":
            logger.info("Connecting to Composo local")
            self.backend_url = "http://localhost:8000"
        elif os.environ.get("PACKAGE_ENV", "prod") == "dev":
            logger.info("Connecting to Composo dev")
            self.backend_url = (
                "https://composo-prod-backend-composo-dev-backend.azurewebsites.net"
            )
        elif os.environ.get("PACKAGE_ENV", "prod") == "test":
            logger.info("Connecting to Composo test")
            self.backend_url = (
                "http://composo-prod-backend-composo-test-backend.azurewebsites.net"
            )
        else:
            self.backend_url = "https://composo.ai"

    @staticmethod
    def is_valid_json(data):
        import json

        try:
            json.loads(data)
            return True
        except Exception:
            return False

    def make_request(
        self, method: Literal["post", "get", "put"], path, data: dict = None
    ):
        if not type(data) == dict or data is None:
            raise ComposoDeveloperException(
                "Data must be a dict or None. Something's gone wrong."
            )

        headers = {"Content-Type": "application/json"} # No API key required any more
        url = self.backend_url + path

        tries = 0
        max_tries = 100
        while tries < max_tries:
            try:
                if method.lower() == "post":
                    response = requests.post(url, json=data, headers=headers)
                elif method.lower() == "get":
                    response = requests.get(url, headers=headers)
                elif method.lower() == "put":
                    response = requests.put(url, json=data, headers=headers)
                else:
                    raise ValueError(
                        'Invalid method. Available options are "post", "get", and "put".'
                    )
                    
                if tries > 0:
                    logger.info("Connection to Composo backend re-established")

                return response

            except requests.exceptions.ConnectionError as e:
                logger.info(
                    f"Could not connect to Composo backend. Retry {tries + 1} of {max_tries}"
                )
                time.sleep(max(10 * (tries / 10) ** 2, 10))
                tries += 1

            except Exception as e:
                raise ComposoDeveloperException(
                    f"There was an unexpected error in backend polling: {str(e)}"
                )

        raise ComposoCriticalException(
            f"Could not connect to Composo backend after {max_tries} tries."
        )


class LiveEventIngress(BackendEventGress):
    def event_poll(self):
        response = self.make_request(
            method="post", path="/api/run/package", data=self.app_registration.dict()
        )
        if response.status_code == 200:
            json_response = response.json()

            for event_type in [PollResponse, AppDeletionEvent]:
                try:
                    parsed_event = event_type.parse_obj(json_response)
                    return parsed_event

                except Exception as e:
                    pass  # Try the next event type

            raise ComposoDeveloperException(
                f"Could not parse the response from the backend into a known response type: {response}"
            )

        else:
            raise ComposoDeveloperException(
                f"The backend is returning an error from polling, this should never happen: {response}"
            )


class LiveEventEgress(BackendEventGress):
    def report_run_results(self, run_result: RunResult, run_id):
        response = self.make_request(
            "put", path=f"/api/run/package/{run_id}", data=run_result.dict()
        )
        if response.status_code == 200:
            logger.info("Run completed and results reported")
        else:
            raise ComposoDeveloperException(
                f"The backend is returning a non 200 status code from reporting run results, this should never happen: {response}"
            )


def experiment_controller(
    func,
    demo_args,
    demo_kwargs,
    demo_globals,
    api_key="FAKE_KEY_FOR_TESTING",
    event_ingress=None,
    event_egress=None,
):
    """
    Args:
        event_ingress (_type_): server-side events from polling
        event_egress (_type_): various backend methods

    """
    logger.info("Composo Experiment is activated")
    # TODO: You need to freeze the global state when this is launched because you might want to change global state in the experiment but not

    vars_format_schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "is_kwarg": {"type": "boolean"},
                "is_fixed": {"type": "boolean"},
                "instantiated_type": {"type": "any"},
                "type": {"type": "any"},
                "str_type": {"type": "string"},
                "description": {"type": "string"},
                "demo": {"type": "string"},
                "constraints": {"type": "string"},
            },
            "required": ["name", "type", "description", "demo", "constraints"],
        },
    }

    signature = inspect.signature(func)

    inspected_args = {
        param.name: param.annotation
        for param in signature.parameters.values()
        if param.default == inspect.Parameter.empty
    }
    inspected_kwargs = {
        param.name: param.annotation
        for param in signature.parameters.values()
        if param.default != inspect.Parameter.empty
    }

    all_vars = []

    # Demo args as dict
    if not len(inspected_args.keys()) == len(demo_args):
        raise ComposoCriticalException("Number of demo args does not match function")

    demo_args = dict(zip(inspected_args.keys(), list(demo_args)))
    all_demos = {**demo_args, **demo_kwargs}

    for name, _type in {**inspected_args, **inspected_kwargs}.items():
        is_kwarg = name in inspected_kwargs.keys()
        # check if variable is tagged
        if _type in WORKABLE_TYPES.__args__ or type(_type) in WORKABLE_TYPES.__args__:
            is_fixed = False
            try:
                # This is a pure type
                this_arg_type = _type.__bases__[0]  # Assuming one base type
                description = None
                constraint_string = None
                instantiated_type = None
            except AttributeError as e:
                # This is an 'instantiated' type
                this_arg_type = type(_type).__bases__[0]  # Assuming one base type
                description = _type.description
                constraint_string = _type.get_constraint_string()
                instantiated_type = _type

            str_type = _type.type_string()

            all_vars.append(
                {
                    "name": name,
                    "is_kwarg": is_kwarg,
                    "is_fixed": is_fixed,
                    "instantiated_type": instantiated_type,
                    "type": this_arg_type,
                    "str_type": str_type,
                    "description": description,
                    "demo": all_demos[name],
                    "constraints": constraint_string,
                }
            )
        else:
            # These are variables that aren't annotated by the user
            is_fixed = True
            all_vars.append(
                {
                    "name": name,
                    "is_kwarg": is_kwarg,
                    "is_fixed": is_fixed,
                    "instantiated_type": None,
                    "type": None,
                    "str_type": None,
                    "description": None,
                    "demo": all_demos[name],
                    "constraints": None,
                }
            )

    app_registration = AppRegistration(
        api_key=api_key,
        parameters=[x["name"] for x in all_vars if not x["is_fixed"]],
        types=[x["str_type"] for x in all_vars if not x["is_fixed"]],
        demo_values=[x["demo"] for x in all_vars if not x["is_fixed"]],
        descriptions=[x["description"] for x in all_vars if not x["is_fixed"]],
        constraints=[x["constraints"] for x in all_vars if not x["is_fixed"]],
    )

    if event_ingress is None or event_egress is None:
        logger.info("Initialising live connection to Composo")
        if api_key is None:
            raise ValueError("api_key must be provided")
        event_ingress = LiveEventIngress(app_registration)
        event_egress = LiveEventEgress(app_registration)
    elif (event_ingress is None and event_egress is not None) or (
        event_ingress is not None and event_egress is None
    ):
        raise ValueError(
            "event_ingress and event_egress must both be None or both be not None"
        )

    def run_experiment(replacement_vars: dict):
        # Checking all user provided args are also tagged args
        logger.info("Experiment initiated")
        if not all(
            key in [x["name"] for x in all_vars] for key in replacement_vars.keys()
        ):
            raise ComposoDeveloperException(
                f"The user has somehow been allowed to provide args that are not tagged. Provided args: {replacement_vars.keys()}. Tagged args: {[x['name'] for x in all_vars]} "
            )

        # Creating a working copy of all_vars
        working_all_vars = copy.deepcopy(all_vars)
        for i in range(len(working_all_vars)):
            working_all_vars[i]["working_value"] = working_all_vars[i]["demo"]

        for arg_name, arg_value in replacement_vars.items():
            this_var = [x for x in all_vars if x["name"] == arg_name][0]
            this_var_type = this_var["type"]
            try:
                typed_value = this_var_type(arg_value)
            except Exception as e:
                raise ComposoUserException(
                    f"The provided arg could not be converted to required type: {this_var['type']}. Arg value was {arg_value}"
                )

            if this_var["instantiated_type"] is not None:
                this_var["instantiated_type"].validate(typed_value)

            # Inserting the new arg into the working copy
            all_var_index = [
                i for i, x in enumerate(working_all_vars) if x["name"] == arg_name
            ][0]
            working_all_vars[all_var_index]["working_value"] = typed_value

        # deconstructing into args and kwargs
        working_args = [
            x["working_value"] for x in working_all_vars if not x["is_kwarg"]
        ]
        working_kwargs = {
            x["name"]: x["working_value"] for x in working_all_vars if x["is_kwarg"]
        }

        try:
            ret_val = func(*working_args, **working_kwargs)
        except Exception as e:
            raise ComposoUserException(
                f"The linked function produced an error: {str(e)}"
            )

        return ret_val

    previously_noted_app_ids = []

    logger.info("Connected and listening.")
    while True:
        try:
            time.sleep(3)
            event = event_ingress.event_poll()

            if isinstance(event, AppDeletionEvent):
                logger.info("AppDeletionEvent Received")
                return  # return from the experiment controller

            elif isinstance(event, PollResponse):
                registered_apps = event.registered_apps
                for registered_app in registered_apps:
                    if registered_app not in previously_noted_app_ids:
                        logger.info(f"App registered: {registered_app}")
                        previously_noted_app_ids.append(registered_app)

                if event.run_trigger is not None:
                    logger.info("New Evaluation Run Triggered")
                    case_results = []

                    ########################################
                    ### Inner loop running the test cases
                    ### Errors here should be caught and inserted into the case_results
                    ########################################
                    for i, case in enumerate(event.run_trigger.cases):
                        try:
                            ret = run_experiment(case.vars)
                            case_results.append(CaseResult(value=ret, error=None))
                        except ComposoUserException as e:
                            case_results.append(
                                CaseResult(value=None, error="ERROR: " + str(e))
                            )
                        except Exception as e:
                            if os.environ.get("PACKAGE_ENV", "prod") != "prod":
                                print(
                                    f"Unidentified exception caught with case {case}: {str(e)}"
                                )
                            case_results.append(
                                CaseResult(
                                    value=None,
                                    error="ERROR: The composo package has failed with an unidentified error. Please contact composo support.",
                                )
                            )

                        # TODO: Don't report run results every time, if you've got a lot of cases you'll be spamming the server, it should be time based

                        event_egress.report_run_results(
                            RunResult(
                                results=case_results,
                                error=None,
                                progress=math.floor(
                                    100 * float(i + 1) / len(event.run_trigger.cases)
                                ),
                            ),
                            run_id=event.run_trigger.run_id,
                        )

                    if not (
                        math.floor(100 * float(i + 1) / len(event.run_trigger.cases))
                        == 100
                    ):
                        raise ComposoDeveloperException(
                            "The run progress was not reported as 100%"
                        )

        except ComposoDeveloperException as e:
            if os.environ.get("PACKAGE_ENV", "prod") != "prod":
                print(f"Composo Developer Exception caught: {str(e)}")
            pass
        except ComposoUserException as e:
            print(f"Composo User Exception caught: {str(e)}")
        except ComposoCriticalException as e:
            raise e
        except Exception as e:
            # If it's an indentified exception, let's just continue and hope everything is ok
            if os.environ.get("PACKAGE_ENV", "prod") != "prod":
                print(f"Unidentified exception caught: {str(e)}")
            pass


def generate_api_key():
    import secrets
    import string

    key_length = 32
    # Define a character set from which the key will be generated
    characters = string.ascii_uppercase + string.digits
    api_key = "".join(secrets.choice(characters) for _ in range(key_length - 3))
    api_key = "cp-" + api_key
    return api_key


class Composo:
    # @classmethod
    # def activate(cls):
    #     """_summary_
    #     Sets up variable tracing. This is only needed if you want to force-change variables INSIDE
    #     the test function - you don't need it for changing args or globals
    #     """
    #     # Adding a tracers
    #     def variable_intercepter(frame, event, arg):
    #         # consider checking if event == "line" and the line is a variable assignment
    #         modification_tasks = {
    #             'a': 2,
    #             'c': 4
    #         }

    #         # Applying modification tasks to locals
    #         local_dict_copy = frame.f_locals
    #         for item in modification_tasks.keys() & frame.f_locals.keys():
    #             local_dict_copy[item] = modification_tasks[item]
    #         save_locals(local_dict_copy)

    #         return variable_intercepter

    #     sys.settrace(variable_intercepter)
    #     threading.settrace(variable_intercepter)

    @classmethod
    def link(cls, api_key=None):
        cls.api_key = api_key

        def actual_decorator(func):  # This is the actual decorator.
            def wrapped_func(*args, **kwargs):
                if not hasattr(Composo, "activated"):
                    cls.activated = True

                    if cls.api_key is None:
                        api_key = generate_api_key()
                    else:
                        api_key = cls.api_key

                    logger.info("########################################")
                    logger.info("######### Your Composo API Key #########")
                    logger.info("### " + api_key + " ###")
                    logger.info("########################################")
                    # TODO: run func a few times to check that it's pure/idempotent
                    try:
                        result = func(*args, **kwargs)
                    except Exception as e:
                        raise Exception(
                            "The function invocation has errors. Please fix before linking to Composo. Error: "
                            + str(e)
                        )

                    permissable_return_types = [int, float, str]
                    result_type = type(result)
                    if result_type not in permissable_return_types:
                        raise Exception(
                            f"The linked function returned type: {result_type}. Supported return types are {', '.join([x.__name__ for x in permissable_return_types])}"
                        )

                    experiment_controller(
                        func, args, kwargs, func.__globals__, api_key=api_key
                    )

                    # hmmm, this might need to be threaded
                    # threaded_controller = threading.Thread(target=lambda: threaded_experiment_controller(func, args, kwargs, func.__globals__))
                    # threaded_controller.start()

                    return result
                else:
                    result = func(*args, **kwargs)

            return wrapped_func

        return actual_decorator
