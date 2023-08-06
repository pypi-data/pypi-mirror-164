import django.http as http
from rest_framework import viewsets

from masterful_gui.backend.apps.api import serializers
from masterful_gui.backend.apps.api import models
from masterful_gui.backend.apps.api import policy_search_task_scanner
from masterful_gui.backend.apps.api import dataset_scanner
from masterful_gui.backend.apps.api import training_run_scanner


class PolicySearchTaskView(viewsets.ReadOnlyModelViewSet):
  serializer_class = serializers.PolicySearchTaskModelSerializer
  queryset = models.PolicySearchTask.objects.all()


class DatasetView(viewsets.ReadOnlyModelViewSet):
  serializer_class = serializers.DatasetModelSerializer
  queryset = models.Dataset.objects.all()


class TrainingRunView(viewsets.ReadOnlyModelViewSet):
  serializer_class = serializers.TrainingRunModelSerializer
  queryset = models.TrainingRun.objects.all().order_by('-completed_ts')


def scan_view(request):
  """This performs scans on all protos supported by visualize."""
  # TODO: improve the experience. Consider reroute or surfacing
  # a template. This is not required it's just for aesthetics.
  try:
    training_run_scanner.scan()
    dataset_scanner.scan()
  except Exception as e:
    print(str(e))
    return http.HttpResponseServerError()

  return http.HttpResponse()
