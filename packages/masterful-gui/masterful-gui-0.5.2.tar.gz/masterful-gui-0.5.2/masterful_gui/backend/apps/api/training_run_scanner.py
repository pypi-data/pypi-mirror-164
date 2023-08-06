"""Scanner for serialized TrainingRun protos."""

import os
import pathlib
import datetime
import pytz
import pkg_resources

import google.protobuf.json_format as json_format

from masterful_gui.backend.apps.api import models
from masterful_gui.backend.proto import timestamp_pb2, training_pb2
from masterful_gui.backend.apps.api import constants
from masterful_gui.backend.apps.api import image_utils


def scan():
  """Scans the configured directory for serlized policy protos.
  
  This function deserializes policy protos on disk, converts them
  to Django's owm policy model, and persists them to the database (app model).
  If the database already had a record for that policy, it updates
  that records with the values extracted from the serialized policy. If it
  wasn't, this will persist it to the database.
  """
  _load_sample_binary_classification_run()
  _load_sample_classification_run()

  pathlib.Path(constants.TRAINING_RUN_SCAN_DIR).mkdir(parents=True,
                                                      exist_ok=True)

  if len(os.listdir(constants.TRAINING_RUN_SCAN_DIR)) == 0:
    #TODO(ray): Consider printing something to show in backend logs.
    return

  serialized_runs = []
  for file in os.listdir(constants.TRAINING_RUN_SCAN_DIR):
    if file.split('.')[-1] != constants.TRAINING_RUN_EXT:
      continue
    serialized_runs.append(file)

  if len(serialized_runs) == 0:
    return

  for serialized_run in serialized_runs:
    run = training_pb2.TrainingRun()
    file_name = f'{constants.TRAINING_RUN_SCAN_DIR}/{serialized_run}'
    with open(file_name, "rb") as f:
      run.ParseFromString(f.read())

    run_dict = json_format.MessageToDict(run,
                                         use_integers_for_enums=False,
                                         including_default_value_fields=True,
                                         preserving_proto_field_name=True)

    run_exists = len(models.TrainingRun.objects.filter(pk=run.name)) > 0
    if run_exists:
      existing_run = models.TrainingRun.objects.get(pk=run.name)
      existing_run.model_info = run_dict.get("model_info", {})
      existing_run.policy_search_results = run_dict.get("policy_search_results",
                                                        {})
      existing_run.approach_name = run.approach_name
      existing_run.masterful_version = run.masterful_version
      existing_run.completed_ts = _get_datetime(run.completed_ts)
      existing_run.task = run.task
      if run.model_info.graph_image.graph_was_rendered:
        graph_path = image_utils.save_model_graph_image(
            run.name, run.model_info.graph_image)
        existing_run.model_graph_image = graph_path
      existing_run.optimization_params = run_dict.get("optimization_params", {})
      existing_run.ssl_params = run_dict.get("ssl_params", {})
      existing_run.datasets = run_dict.get("datasets", {})
      existing_run.save()

    else:
      graph_path = ''
      if run.model_info.graph_image.graph_was_rendered:
        graph_path = image_utils.save_model_graph_image(
            run.name, run.model_info.graph_image)

      new_run = models.TrainingRun.objects.create(
          name=run.name,
          completed_ts=_get_datetime(run.completed_ts),
          model_info=run_dict.get("model_info", {}),
          policy_search_results=run_dict.get("policy_search_results", {}),
          approach_name=run.approach_name,
          masterful_version=run.masterful_version,
          model_graph_image=graph_path,
          optimization_params=run_dict.get("optimization_params", {}),
          ssl_params=run_dict.get("ssl_params", {}),
          datasets=run_dict.get("datasets", {}),
          task=run.task)
      new_run.save()


def _load_sample_classification_run():
  """Loads the data for a sample classification into the model."""
  loaded_already = len(
      models.TrainingRun.objects.filter(
          pk=constants.CLASSIFICATION_SAMPLE_RUN_NAME)) > 0

  if loaded_already:
    return

  sample_proto = training_pb2.TrainingRun()
  data = pkg_resources.resource_string(
      "masterful_gui", f'data/{constants.CLASSIFICATION_SAMPLE_RUN_FILE_NAME}')
  sample_proto.ParseFromString(data)

  proto_dict = json_format.MessageToDict(sample_proto,
                                         use_integers_for_enums=False,
                                         including_default_value_fields=True,
                                         preserving_proto_field_name=True)
  graph_path = ''
  if sample_proto.model_info.graph_image.graph_was_rendered:
    graph_path = image_utils.save_model_graph_image(
        sample_proto.name, sample_proto.model_info.graph_image)

  model_entry = models.TrainingRun.objects.create(
      name=sample_proto.name,
      completed_ts=_get_datetime(sample_proto.completed_ts),
      model_info=proto_dict.get("model_info", {}),
      policy_search_results=proto_dict.get("policy_search_results", {}),
      approach_name=sample_proto.approach_name,
      masterful_version=sample_proto.masterful_version,
      model_graph_image=graph_path,
      optimization_params=proto_dict.get("optimization_params", {}),
      ssl_params=proto_dict.get("ssl_params", {}),
      task=sample_proto.task,
      datasets=proto_dict.get("datasets", {}))

  model_entry.save()


def _load_sample_binary_classification_run():
  """Loads the data for a sample binary classification into the model."""
  loaded_already = len(
      models.TrainingRun.objects.filter(
          pk=constants.BINARY_SAMPLE_RUN_NAME)) > 0

  if loaded_already:
    return

  sample_proto = training_pb2.TrainingRun()
  data = pkg_resources.resource_string(
      "masterful_gui", f'data/{constants.BINARY_SAMPLE_RUN_FILE_NAME}')
  sample_proto.ParseFromString(data)

  proto_dict = json_format.MessageToDict(sample_proto,
                                         use_integers_for_enums=False,
                                         including_default_value_fields=True,
                                         preserving_proto_field_name=True)
  graph_path = ''
  if sample_proto.model_info.graph_image.graph_was_rendered:
    graph_path = image_utils.save_model_graph_image(
        sample_proto.name, sample_proto.model_info.graph_image)

  model_entry = models.TrainingRun.objects.create(
      name=sample_proto.name,
      completed_ts=_get_datetime(sample_proto.completed_ts),
      model_info=proto_dict.get("model_info", {}),
      policy_search_results=proto_dict.get("policy_search_results", {}),
      approach_name=sample_proto.approach_name,
      masterful_version=sample_proto.masterful_version,
      model_graph_image=graph_path,
      optimization_params=proto_dict.get("optimization_params", {}),
      ssl_params=proto_dict.get("ssl_params", {}),
      task=sample_proto.task,
      datasets=proto_dict.get("datasets", {}))

  model_entry.save()


def _get_datetime(timestamp: timestamp_pb2.Timestamp) -> datetime.datetime:
  ts = float(timestamp.seconds + timestamp.nanos / 1e9)
  return datetime.datetime.fromtimestamp(ts, tz=pytz.timezone('UTC'))