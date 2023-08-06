"""Handles creating images from binary image data."""

import os
import pathlib

from masterful_gui.backend.apps.api import constants
from masterful_gui.backend.proto import model_pb2
from django.conf import settings


def save_model_graph_image(run_name: str,
                           model_graph: model_pb2.ModelGraphImage) -> str:
  """Saves the model graph image in backend's media storage and returns URL.
  
  Args:
    run_name: The name of the training run.
    model_graph: The proto of the model graph image holding the data.
  
  Returns:
    The URL of the saved image on success. This URL is for the image as it's
    served by the Django backend server that the frontend can use to render
    the image.
  """
  if not model_graph.graph_was_rendered:
    return ""

  file_name = f"{constants.MODEL_GRAPH_IMAGE_NAME}.png"
  output_subdir = f"{run_name}/{constants.MODEL_IMG_DIR}"
  output_dir = f"{settings.MEDIA_ROOT}/{output_subdir}/"

  pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)

  full_path = f'{output_dir}/{file_name}'
  with open(full_path, 'wb') as f:
    f.write(model_graph.data)

  url = ''
  if settings.DEBUG:
    url = f'http://localhost:7007/media/{output_subdir}/{file_name}'
  else:
    url = f'http://localhost:7007/static/media/{output_subdir}/{file_name}'

  return url
