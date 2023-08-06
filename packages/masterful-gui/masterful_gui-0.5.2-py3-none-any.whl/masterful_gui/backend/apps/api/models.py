from django.db import models


class TrainingRun(models.Model):
  """Represents a full training run by Masterful.
  
  This model mirros the TrainingRun proto. All details are in proto definition.
  """
  # The name of the run.
  name = models.CharField(primary_key=True, max_length=250)

  # Datetime of when the training run was completed. We call it 'ts' to match
  # the proto name for ease of conversions, even though it's a datetime
  # field and not a timestamp.
  completed_ts = models.DateTimeField()

  # Information about the model. This is a Model proto json representation.
  model_info = models.JSONField(default=dict)

  # Results of searching for optimal policy and training with it. This is a
  # PolicySearchTask proto json representation.
  policy_search_results = models.JSONField(default=dict)

  # Name of the approach which performed the run.
  approach_name = models.CharField(max_length=120)

  # Version of the masterful pip package which produced the run.
  masterful_version = models.CharField(default="", max_length=100)

  # The CV task the run was used for.
  task = models.CharField(default="", max_length=100)

  # The absolute path of the model graph image on disk.
  model_graph_image = models.CharField(default="", max_length=100)

  # Optimization params used in training.
  optimization_params = models.JSONField(default=dict)

  # SSL params used in training.
  ssl_params = models.JSONField(default=dict)

  # Datasets used in this training run. Can also include evaluation (test) set
  # when CLI is used for the run.
  datasets = models.JSONField(default=dict)


############
# DEPRECATED
############
class PolicySearchTask(models.Model):
  """The main PolicySearchTask model.
  
  The model mirrors the PolicySearchTask proto. Scalar fields are assigned
  similaer fields in the model, everything else is assigned JSON fields.
  """
  # The name of the policy. This is the primary key of the model.
  policy_name = models.CharField(primary_key=True, max_length=250)

  # The name of the approach.
  approach_name = models.CharField(max_length=120)

  # Node search tasks performed in the policy search task.
  node_search_tasks = models.JSONField(default=dict)

  # Metrics specific to the customer model without any Masterful improvements.
  presearch_model_val_metrics = models.JSONField(default=dict)

  # The version of the policy engine that produced this policy.
  engine_version = models.CharField(default="", max_length=100)

  # Whether fit results were captured.
  fit_was_captured = models.BooleanField(default=False)

  # Results of training the model with Masterful's learned policy.
  learned_policy_val_metrics = models.JSONField(default=dict)

  # The type of the ML task the policy is used for.
  task_type = models.CharField(default="COMPUTER_VISION_TASK_UNKNOWN",
                               max_length=250)


class Dataset(models.Model):
  """A model that represents a dataset.
  
  The model mirros the Dataset proto. For full documentation, see proto
  definition.
  """
  # The id of the dataset. This is the primary key of the model.
  dataset_id = models.CharField(primary_key=True, max_length=250)

  # The title of the dataset.
  title = models.CharField(max_length=250)

  # Train split. This is a Split proto.
  train_dataset = models.JSONField(default=dict)

  # Val split. This is a Split proto.
  val_dataset = models.JSONField(default=dict)

  # Test split. This is a Split proto.
  test_dataset = models.JSONField(default=dict)

  # Full dataset. This is a Split proto.
  full_dataset = models.JSONField(default=dict)

  # Cardinality of the whole dataset.
  cardinality = models.IntegerField(default=0)

  # Maps each label to its count in the full dataset.
  label_count = models.JSONField(default=dict)

  # Maps labels numeric format to their text format.
  labels_map = models.JSONField(default=dict)

  # Computer visiion task. This is a ComputerVisionTask proto.
  task = models.JSONField(default=dict)

  # Number of classes in the dataset.
  num_classes = models.IntegerField(default=0)

  # Duration it took to complete the dataset analysis, in minutes.
  analysis_duration_mins = models.FloatField(default=0.)