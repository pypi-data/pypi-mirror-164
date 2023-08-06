from typing import Any, Dict, List, Tuple, Union

import logging

from .dataclasses import (
    BuiltinCallable,
    ValidationResult,
    ValidationStep,
    load_ValidationStep,
)
from .exceptions import ParsingError, ValidationError
from .path_matching import path_matches_pattern

logger = logging.getLogger(__name__)


def run_BuiltinCallable(target: Any, builtin: BuiltinCallable) -> Any:
    return builtin.resolved_function(
        target,
        **builtin.args,
    )


def run_ValidationStep(filepath: str, step: ValidationStep) -> ValidationResult:
    if step.processor:
        processed = run_BuiltinCallable(
            filepath,
            step.processor,
        )  # type: Union[Any, str]
    else:
        processed = filepath

    return ValidationResult(
        filepath=filepath,
        results=[
            run_BuiltinCallable(processed, validator) for validator in step.validators
        ],
    )


def run_validation(
    file_list: List[str], validation_steps: List[Dict[str, Any]]
) -> List[ValidationResult]:
    loaded = map(load_ValidationStep, validation_steps)

    results = []
    for validation_step in loaded:
        for filepath in file_list:
            if path_matches_pattern(filepath, validation_step.path_suffix):
                results.append(
                    run_ValidationStep(
                        filepath,
                        validation_step,
                    )
                )

    return results
