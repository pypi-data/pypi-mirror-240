from functools import wraps
from typing import Any, Callable, Optional
import inspect


class SuvOperationContext:

    state: dict[str, Any]
    func_kwargs: dict[str, Any]
    arg_validator: Callable[["SuvOperationContext", dict], None]

    def __init__(self, validator: Callable[["SuvOperationContext", dict], None] = None, func_kwargs: dict[str, Any] = None):
        self.arg_validator = validator
        self.state = {
            "log": [],
            "errors": []
        }
        self.func_kwargs = func_kwargs

    def __enter__(self):
        try:
            if self.func_kwargs and self.arg_validator:
                self.arg_validator(self, **self.func_kwargs)

            return self
        except Exception as e:
            self.__exit__(type(e), e, e.__traceback__)
            raise

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type is not None:
            if self.state["errors"]:
                print("Errors flagged during operation:")
                for error in self.state["errors"]:
                    print(error)
            return False
        return True

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.arg_validator is not None:
                self.arg_validator(**kwargs)
            self.func_args = args
            self.func_kwargs = kwargs
            with self._recreate_context_manager():
                sig = inspect.signature(func)
                if "context" in sig.parameters or "kwargs" in sig.parameters:
                    return func(*args, **kwargs, context=self)
                return func(*args, **kwargs)

        return wrapper

    def _recreate_context_manager(self):
        return self

    def log(self, level: str, operation: str, message: str = "", result: str = "OK"):
        self.state["log"].append({
            "level": level,
            "operation": operation,
            "message": message,
            "result": result
        })

    def set_error(self, error_type: str, error_msg: str, exception: Exception):
        self.state["errors"].append({
            "error_type": error_type,
            "error_message": error_msg,
            "exception": exception
        })

    def errors(self) -> dict:
        return {"errors": self.state["errors"]}


###########  REMOVE!

# @SuvOperationContext()
# def try_empty_args_1():
#     print("Hello from mister empty 1!")
#
#
# @SuvOperationContext(stuff="STUFF")
# def try_empty_args_2():
#     print("Hello from mister empty 2!")
#
#
# @SuvOperationContext()
# def try_func_args_1(a):
#     print("Hello from func 1", a)


def bob_validator(**kwargs):
    if "bob" not in kwargs:
        raise ValueError("No bob here!")
    if len(kwargs["bob"]) < 5:
        raise ValueError(f"Not enough bob!  (bob was '{kwargs['bob']}')")


@SuvOperationContext(validator=bob_validator)
def try_func_args_2(a, bob, **kwargs):
    print("Hello from func 2", a, bob)
    if "context" in kwargs:
        kwargs["context"].state["visited"] = "func 2"


@SuvOperationContext(validator=bob_validator)
def try_func_args_3(a, bob, context: SuvOperationContext):
    print("Hello from func 3", a, bob)
    print(context.state)
    context.log("info", "visit", "visited func 3")
    try:
        b = 10 / a
        print(f"10 / {a} = {b}")
    except Exception as e:
        context.set_error(
            type(e).__name__,
            f"An error occurred dividing 10 with {a}",
            e
        )
        raise


# def try_func_args_4(a, bob):
#     with SuvOperationContext(validator=bob_validator, params=locals()) as s:
#         print("Hello from func 4", a, bob)

#try_empty_args_1()
#try_empty_args_2()
#try_func_args_1(1)
#try_func_args_2(2, bob="Snobb")
#try_func_args_3(0, bob="Snobb")
# try_func_args_3(3, bob="Globs")
#try_func_args_4(a=5, bob="Tobb")
