# Copyright (C) 2022 Panther Labs Inc
#
# Panther Enterprise is licensed under the terms of a commercial license available from
# Panther Labs Inc ("Panther Commercial License") by contacting contact@runpanther.com.
# All use, distribution, and/or modification of this software, whether commercial or non-commercial,
# falls under the Panther Commercial License to the extent it is permitted.

# coding=utf-8
# *** WARNING: generated file
import typing
import dataclasses

"""
The detection module provides classes representing Panther detections: Rules, Policies, Scheduled Rules and more
"""

from .. import _utilities

__all__ = [
    "DynamicStringField",
    "DynamicDestinations",
    "AlertGrouping",
    "_BaseFilter",
    "PythonFilter",
    "_BaseUnitTest",
    "JSONUnitTest",
    "Rule",
    "SeverityLow",
    "SeverityInfo",
    "SeverityMedium",
    "SeverityHigh",
    "SeverityCritical",
    "ReportKeyMITRE",
]


SeverityLow = "LOW"
SeverityInfo = "INFO"
SeverityMedium = "MEDIUM"
SeverityHigh = "HIGH"
SeverityCritical = "CRITICAL"
ReportKeyMITRE = "MITRE ATT&CK"


@dataclasses.dataclass(frozen=True)
class DynamicStringField(_utilities.ConfigNode):
    """Make a field dynamic based on the detection input

    Attributes:
        - func -- Dynamic handler (required)
        - fallback -- Fallback value in case the dynamic handler fails (optional, default: "")

    """

    # required
    func: typing.Callable[[typing.Any], str]

    # optional
    fallback: str = ""

    # internal private methods
    def _typename(self) -> str:
        return "DynamicStringField"

    def _output_key(self) -> str:
        return ""

    def _fields(self) -> typing.List[str]:
        return ["func", "fallback"]


@dataclasses.dataclass(frozen=True)
class DynamicDestinations(_utilities.ConfigNode):
    """Make destinations dynamic based on the detection input

    Attributes:
        - func -- Dynamic handler (required)
        - fallback -- Fallback value in case the dynamic handler fails (optional, default: None)

    """

    # required
    func: typing.Callable[[typing.Any], typing.List[str]]

    # optional
    fallback: typing.Optional[typing.List[str]] = None

    # internal private methods
    def _typename(self) -> str:
        return "DynamicDestinations"

    def _output_key(self) -> str:
        return ""

    def _fields(self) -> typing.List[str]:
        return ["func", "fallback"]


@dataclasses.dataclass(frozen=True)
class AlertGrouping(_utilities.ConfigNode):
    """Configuration for how an alert is grouped

    Attributes:
        - group_by -- Function to generate a key for grouping matches (optional, default: None)
        - period_minutes -- How long should matches be grouped into an alert after the first match (optional, default: 15)

    """

    # optional
    group_by: typing.Optional[typing.Callable[[typing.Any], str]] = None

    # optional
    period_minutes: int = 15

    # internal private methods
    def _typename(self) -> str:
        return "AlertGrouping"

    def _output_key(self) -> str:
        return ""

    def _fields(self) -> typing.List[str]:
        return ["group_by", "period_minutes"]


@dataclasses.dataclass(frozen=True)
class _BaseFilter(_utilities.ConfigNode):
    """Base filter"""

    # internal private methods
    def _typename(self) -> str:
        return "_BaseFilter"

    def _output_key(self) -> str:
        return ""

    def _fields(self) -> typing.List[str]:
        return []


@dataclasses.dataclass(frozen=True)
class PythonFilter(_BaseFilter):
    """Custom python filter

    Attributes:
        - func -- Custom python filter (required)
        - params -- Custom python filter (optional, default: None)

    """

    # required
    func: typing.Callable[
        [
            typing.Optional[typing.Any],
            typing.Optional[typing.Dict[str, typing.Union[str, int, float, bool]]],
        ],
        bool,
    ]

    # optional
    params: typing.Optional[
        typing.Dict[str, typing.Union[str, int, float, bool]]
    ] = None

    # internal private methods
    def _typename(self) -> str:
        return "PythonFilter"

    def _output_key(self) -> str:
        return ""

    def _fields(self) -> typing.List[str]:
        return ["func", "params"]


@dataclasses.dataclass(frozen=True)
class _BaseUnitTest(_utilities.ConfigNode):
    """Base unit test"""

    # internal private methods
    def _typename(self) -> str:
        return "_BaseUnitTest"

    def _output_key(self) -> str:
        return ""

    def _fields(self) -> typing.List[str]:
        return []


@dataclasses.dataclass(frozen=True)
class JSONUnitTest(_BaseUnitTest):
    """Unit test with json content

    Attributes:
        - data -- json data (required)
        - expect_match -- should this event trigger the rule? (required)
        - name -- name of the unit test (required)

    """

    # required
    data: str

    # required
    expect_match: bool

    # required
    name: str

    # internal private methods
    def _typename(self) -> str:
        return "JSONUnitTest"

    def _output_key(self) -> str:
        return ""

    def _fields(self) -> typing.List[str]:
        return ["data", "expect_match", "name"]


@dataclasses.dataclass(frozen=True)
class Rule(_utilities.ConfigNode):
    """Define a rule

    Attributes:
        - filters -- Define event filters for the rule (required)
        - log_types -- Log Types to associate with this rule (required)
        - rule_id -- ID for the rule (required)
        - severity -- Severity for the rule (required)
        - alert_context -- Optional JSON to attach to alerts generated by this rule (optional, default: None)
        - alert_grouping -- Configuration for how an alert is grouped (optional, default: None)
        - alert_title -- Title to use in the alert (optional, default: None)
        - description -- Description for the rule (optional, default: "")
        - destinations -- Alert destinations for the rule (optional, default: None)
        - enabled -- Short description for the query (optional, default: True)
        - group -- Number of matches received before an alert is triggered (optional, default: 1)
        - name -- Display name for the rule (optional, default: "")
        - reference -- Reference for the rule (optional, default: "")
        - reports -- Report mappings for the rule (optional, default: None)
        - runbook -- Runbook for the rule (optional, default: "")
        - summary_attrs -- Summary Attributes for the rule (optional, default: None)
        - tags -- Tags for the rule (optional, default: None)
        - threshold -- Number of matches received before an alert is triggered (optional, default: 1)
        - unit_tests -- Define event filters for the rule (optional, default: None)

    """

    # required
    filters: typing.Union[_BaseFilter, typing.List[_BaseFilter]]

    # required
    log_types: typing.Union[str, typing.List[str]]

    # required
    rule_id: str

    # required
    severity: typing.Union[str, DynamicStringField]

    # optional
    alert_context: typing.Optional[
        typing.Callable[[typing.Any], typing.Dict[str, typing.Any]]
    ] = None

    # optional
    alert_grouping: typing.Optional[AlertGrouping] = None

    # optional
    alert_title: typing.Optional[typing.Callable[[typing.Any], str]] = None

    # optional
    description: typing.Optional[typing.Union[str, DynamicStringField]] = ""

    # optional
    destinations: typing.Optional[
        typing.Union[str, typing.List[str], DynamicDestinations]
    ] = None

    # optional
    enabled: bool = True

    # optional
    group: int = 1

    # optional
    name: typing.Optional[str] = ""

    # optional
    reference: typing.Optional[typing.Union[str, DynamicStringField]] = ""

    # optional
    reports: typing.Optional[typing.Dict[str, typing.List[str]]] = None

    # optional
    runbook: typing.Optional[typing.Union[str, DynamicStringField]] = ""

    # optional
    summary_attrs: typing.Optional[typing.List[str]] = None

    # optional
    tags: typing.Optional[typing.Union[str, typing.List[str]]] = None

    # optional
    threshold: int = 1

    # optional
    unit_tests: typing.Optional[
        typing.Union[_BaseUnitTest, typing.List[_BaseUnitTest]]
    ] = None

    # internal private methods
    def _typename(self) -> str:
        return "Rule"

    def _output_key(self) -> str:
        return "config-node:rule"

    def _fields(self) -> typing.List[str]:
        return [
            "filters",
            "log_types",
            "rule_id",
            "severity",
            "alert_context",
            "alert_grouping",
            "alert_title",
            "description",
            "destinations",
            "enabled",
            "group",
            "name",
            "reference",
            "reports",
            "runbook",
            "summary_attrs",
            "tags",
            "threshold",
            "unit_tests",
        ]
