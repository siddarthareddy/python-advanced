import re
import sys
from collections import OrderedDict
from itertools import chain
from typing import (
    Dict,
    Iterable,
    List,
    Match,
    Optional,
    Pattern,
    Sequence,
    Set,
    Any,
)

import setuptools

_INSTALL_REQUIRES: str = "install_requires"


_extras_pattern: Pattern = re.compile(r"^([^\[]+\[)([^\]]+)(\].*)$")


def consolidate_requirement_options(
    requirements: Iterable[str],
) -> Iterable[str]:
    requirement: str
    templates_options: Dict[str, Set[str]] = OrderedDict()
    traversed_requirements: Set[str] = set()
    for requirement in requirements:
        print(requirement)
        match: Optional[Match] = _extras_pattern.match(requirement)
        if match:
            groups: Sequence[str] = match.groups()
            no_extras_requirement: str = f"{groups[0][:-1]}{groups[2][1:]}"
            template: str = f"{groups[0]}{{}}{groups[2]}"
            if template not in templates_options:
                templates_options[template] = set()
            templates_options[template] |= set(groups[1].split(","))
            if no_extras_requirement in templates_options:
                del templates_options[no_extras_requirement]
        elif requirement not in traversed_requirements:
            templates_options[requirement] = None
    template: str
    options: Optional[List[str]]
    for template, options in templates_options.items():
        if options:
            yield template.format(",".join(sorted(options)))
        else:
            yield template


def setup(**kwargs: Any) -> None:
    """
    This `setup` script intercepts arguments to be passed to
    `setuptools.setup` in order to dynamically alter setup requirements
    while retaining a function call which can be easily parsed and altered
    by `setuptools-setup-versions`.
    """
    # Require the package "dataclasses" for python 3.6, but not later
    # python versions (since it's part of the standard library after 3.6)
    if sys.version_info[:2] == (3, 6):
        if _INSTALL_REQUIRES not in kwargs:
            kwargs[_INSTALL_REQUIRES] = []
        kwargs[_INSTALL_REQUIRES].append("dataclasses")
    # Add an "all" extra which includes all extra requirements
    if "extras_require" in kwargs:
        if "all" not in kwargs["extras_require"]:
            kwargs["extras_require"]["all"] = list(
                consolidate_requirement_options(
                    chain(
                        *(
                            values
                            for key, values in kwargs["extras_require"].items()
                            if key not in ("dev", "test")
                        )
                    )
                )
            )
        kwargs["extras_require"]["test"] = list(
            consolidate_requirement_options(
                chain(
                    *(
                        values
                        for key, values in kwargs["extras_require"].items()
                        if key not in ("dev", "all")
                    )
                )
            )
        )
        print(
            "extras_require[all]:\n"
            + "\n".join(
                f"- {requirement}"
                for requirement in kwargs["extras_require"]["all"]
            )
        )
        print(
            "extras_require[test]:\n"
            + "\n".join(
                f"- {requirement}"
                for requirement in kwargs["extras_require"]["test"]
            )
        )
    # Pass the modified keyword arguments to `setuptools.setup`
    setuptools.setup(**kwargs)


setup(
    name="example-repo",
    version="0.10.5",
    description=(
        "Package for Learning Python"
    ),
    author="Siddartha Reddy",
    author_email="reddy.siddartha53@gmail.com",
    python_requires=">=3.6",
    packages=["src"],
    install_requires=[
        "more-itertools~=8.6",
        "iso8601~=0.1",
        "pendulum~=1.4",
    ],
    extras_require={
        "dev": [
            "readme-md-docstrings~=0.1",
            "setuptools-setup-versions~=1.5",
            "wheel~=0.36",
            "ae-compute-ops~=2.0",
        ],
        "test": [
            "mypy~=0.790",
            "flake8~=3.8",
            "pytest~=5.4",
            "tox~=3.20",
            "pip>=20.3.3",
            "setuptools-setup-versions~=1.5",
            "wheel~=0.36",
        ]
    },
)
