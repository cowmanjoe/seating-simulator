import random
from dataclasses import dataclass
from typing import Type, Tuple, List, Any

from rules import Rule


@dataclass
class RuleParameter:
    name: str

    def create_parameter(self) -> Any:
        pass


@dataclass
class RandomFloatRuleParameter(RuleParameter):
    lower_bound: float
    upper_bound: float

    def create_parameter(self) -> float:
        return random.uniform(self.lower_bound, self.upper_bound)


@dataclass
class RandomIntRuleParameter(RuleParameter):
    lower_bound: int
    upper_bound: int

    def create_parameter(self) -> int:
        return random.randint(self.lower_bound, self.upper_bound)


@dataclass
class ConstantRuleParameter(RuleParameter):
    value: Any

    def create_parameter(self) -> Any:
        return self.value


class RuleConfiguration:
    rule_type: Type[Rule]
    rule_parameters: List[RuleParameter]

    def __init__(self, rule_type: Type[Rule], rule_parameters: List[RandomFloatRuleParameter]):
        self.rule_type = rule_type
        self.rule_parameters = rule_parameters

    def create_rule(self):
        rule_params = {}
        for rule_param in self.rule_parameters:
            rule_params[rule_param.name] = rule_param.create_parameter()

        rule = self.rule_type(**rule_params)
        return rule

