from types import ModuleType
from typing import Any, Callable, Dict, List, Optional, Tuple

from dataclasses import dataclass, field

from .. import processors, validators
from .schemas import ValidationStepSchema
from .utils import resolve_function


@dataclass
class BuiltinCallable:

    """Resolved builtin callable function."""

    resolved_function: Callable[..., Tuple[Any, bool]]
    args: Dict[str, Any]


@dataclass
class ValidationStep:

    path_suffix: str
    processor: Optional[BuiltinCallable] = None
    validators: List[BuiltinCallable] = field(default_factory=lambda: [])


@dataclass
class ValidationResult:

    filepath: str
    results: List[Any] = field(default_factory=lambda: [])


validation_step_schema = ValidationStepSchema()


def validate_ValidationStep_data(data: dict) -> dict:  # type: ignore
    return validation_step_schema.load(data)  # type: ignore


def load_BuiltinCallable(mod: ModuleType, data: dict) -> BuiltinCallable:  # type: ignore
    return BuiltinCallable(
        resolved_function=resolve_function(
            mod,
            data["name"],
        ),
        args=data["args"],
    )


def load_ValidationStep(data: dict) -> ValidationStep:  # type: ignore
    validated = validate_ValidationStep_data(data)

    processor_data = validated.get("processor")

    if processor_data:
        loaded_processor = load_BuiltinCallable(
            processors, processor_data
        )  # type: Optional[BuiltinCallable]
    else:
        loaded_processor = None

    loaded_validators = [
        load_BuiltinCallable(validators, validator_data)
        for validator_data in validated["validators"]
    ]

    return ValidationStep(
        path_suffix=data["path_suffix"],
        processor=loaded_processor,
        validators=loaded_validators,
    )
