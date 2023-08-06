from typing import Dict, Optional, Union

from pydantic import Field
from typing_extensions import Literal

from myst.models import base_model
from myst.openapi.models.absolute_timing_get import AbsoluteTimingGet
from myst.openapi.models.choice import Choice
from myst.openapi.models.constant import Constant
from myst.openapi.models.cron_timing_get import CronTimingGet
from myst.openapi.models.hyperopt_get import HyperoptGet
from myst.openapi.models.log_uniform import LogUniform
from myst.openapi.models.q_log_uniform import QLogUniform
from myst.openapi.models.q_uniform import QUniform
from myst.openapi.models.relative_timing_get import RelativeTimingGet
from myst.openapi.models.uniform import Uniform


class HPOGet(base_model.BaseModel):
    """HPO schema for get responses."""

    object_: Literal["HPO"] = Field(..., alias="object")
    uuid: str
    create_time: str
    title: str
    project: str
    model: str
    creator: str
    search_space: Dict[str, Optional[Union[Uniform, QUniform, LogUniform, QLogUniform, Choice, Constant]]]
    search_algorithm: HyperoptGet
    fit_start_timing: Union[AbsoluteTimingGet, RelativeTimingGet]
    fit_end_timing: Union[AbsoluteTimingGet, RelativeTimingGet]
    predict_start_timing: Union[AbsoluteTimingGet, RelativeTimingGet]
    predict_end_timing: Union[AbsoluteTimingGet, RelativeTimingGet]
    update_time: Optional[str] = None
    description: Optional[str] = None
    test_start_time: Optional[str] = None
    test_end_time: Optional[str] = None
    fit_reference_timing: Optional[Union[AbsoluteTimingGet, CronTimingGet]] = None
    predict_reference_timing: Optional[CronTimingGet] = None
