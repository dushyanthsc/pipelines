# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Metric classes in MLMD ontology for KFP SDK."""

from typing import Any, Dict, List

from kfp.dsl import artifact

SCALAR_METRIC_ARTIFACT_SCHEMA=''
COMPLEX_METRICS_ARTIFACT_SCHEMA=''

class ScalarMetrics(artifact.Artifact):
  """Supports logging key-value metrics data e.g "accuracy" = 98.5"""

  TYPE_NAME="SCALAR_METRICS"

  def __init__(self):
    #TODO: call super init with scalar metrics schema

  def log_metric(self, metric: str, value: float) -> None:
    """Log a single metric key-value pair"""
    self.set_float_custom_property(metric, value)

  def load_metrics(self, metrics: Dict[str, float]) -> None:
    """Bulk load the scalar metrics."""
    for metric, value in metrics:
      self.set_float_custom_property(metric, value)

class ComplexMetrics(artifact.Artifact):
  """Base class for complex metric types like ROC-Curve, ConfusionMatrix, etc"""

  TYPE_NAME="COMPLEX_METRICS"

  def __init__(self):
    #TODO: call super init with complex metrics schema



class ROCCurve(ComplexMetrics):
  """Metric class to support logging ROC curve.

  class maintains an internal store to keep track of the logged data points.
  Each update to this internal store will update the custom property of the
  backed MLMD artifact.
  """

  def __init__(self):
    #TODO: call super init with setting metric type.

  def log_roc_reading(self, tpr: float, fpr: float, threshold: float) -> None:
    """Logs a single ROC Curve data point."""
    #TODO: Update internal store and custom property value.

  def load_roc_readings(self, readings: List[List[float]]) -> None:
    """Bulk load ROC Curve"""
    # TODO: Verify passed value conforms to ROC data point update.


class ConfusionMatrix(ComplexMetrics):
  """Metric class to support logging ConfusionMatrix

  Class maintains an internal store to keep track of the logged data points.
  Each update to this internal store will update the custom property of the
  backed MLMD artifact.
  """

  def set_categories(self, categories: List[str]) -> None:
    """Defines the categories for the confusion matrix"""

  def log_cell(self, row_category: str, column_category: str, value: Any) -> None:
    """Logs a single cell value"""

  def log_row(self, row_category: str, cells: List[Any]) -> None:
    """Logs a single row value"""

  def log_column(self, column_category: str, cells: List[Any]) -> None:
    """Logs a single column value"""

  def load_matrix(self, categories: List[str], cells: List[List[Any]]) -> None:
    """Loads a complex confusion matrix"""
