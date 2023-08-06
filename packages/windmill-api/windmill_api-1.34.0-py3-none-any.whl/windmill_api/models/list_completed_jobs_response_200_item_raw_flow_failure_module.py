from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.list_completed_jobs_response_200_item_raw_flow_failure_module_input_transform import (
    ListCompletedJobsResponse200ItemRawFlowFailureModuleInputTransform,
)
from ..models.list_completed_jobs_response_200_item_raw_flow_failure_module_value_type_0 import (
    ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType0,
)
from ..models.list_completed_jobs_response_200_item_raw_flow_failure_module_value_type_1 import (
    ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType1,
)
from ..models.list_completed_jobs_response_200_item_raw_flow_failure_module_value_type_2 import (
    ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType2,
)
from ..models.list_completed_jobs_response_200_item_raw_flow_failure_module_value_type_3 import (
    ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType3,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListCompletedJobsResponse200ItemRawFlowFailureModule")


@attr.s(auto_attribs=True)
class ListCompletedJobsResponse200ItemRawFlowFailureModule:
    """ """

    input_transform: ListCompletedJobsResponse200ItemRawFlowFailureModuleInputTransform
    value: Union[
        ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType0,
        ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType1,
        ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType2,
        ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType3,
    ]
    stop_after_if_expr: Union[Unset, str] = UNSET
    skip_if_stopped: Union[Unset, bool] = UNSET
    summary: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        input_transform = self.input_transform.to_dict()

        if isinstance(self.value, ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType0):
            value = self.value.to_dict()

        elif isinstance(self.value, ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType1):
            value = self.value.to_dict()

        elif isinstance(self.value, ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType2):
            value = self.value.to_dict()

        else:
            value = self.value.to_dict()

        stop_after_if_expr = self.stop_after_if_expr
        skip_if_stopped = self.skip_if_stopped
        summary = self.summary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input_transform": input_transform,
                "value": value,
            }
        )
        if stop_after_if_expr is not UNSET:
            field_dict["stop_after_if_expr"] = stop_after_if_expr
        if skip_if_stopped is not UNSET:
            field_dict["skip_if_stopped"] = skip_if_stopped
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        input_transform = ListCompletedJobsResponse200ItemRawFlowFailureModuleInputTransform.from_dict(
            d.pop("input_transform")
        )

        def _parse_value(
            data: object,
        ) -> Union[
            ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType0,
            ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType1,
            ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType2,
            ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType3,
        ]:
            try:
                value_type_0: ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType0
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType0.from_dict(data)

                return value_type_0
            except:  # noqa: E722
                pass
            try:
                value_type_1: ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType1
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType1.from_dict(data)

                return value_type_1
            except:  # noqa: E722
                pass
            try:
                value_type_2: ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType2
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_2 = ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType2.from_dict(data)

                return value_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            value_type_3: ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType3
            value_type_3 = ListCompletedJobsResponse200ItemRawFlowFailureModuleValueType3.from_dict(data)

            return value_type_3

        value = _parse_value(d.pop("value"))

        stop_after_if_expr = d.pop("stop_after_if_expr", UNSET)

        skip_if_stopped = d.pop("skip_if_stopped", UNSET)

        summary = d.pop("summary", UNSET)

        list_completed_jobs_response_200_item_raw_flow_failure_module = cls(
            input_transform=input_transform,
            value=value,
            stop_after_if_expr=stop_after_if_expr,
            skip_if_stopped=skip_if_stopped,
            summary=summary,
        )

        list_completed_jobs_response_200_item_raw_flow_failure_module.additional_properties = d
        return list_completed_jobs_response_200_item_raw_flow_failure_module

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
