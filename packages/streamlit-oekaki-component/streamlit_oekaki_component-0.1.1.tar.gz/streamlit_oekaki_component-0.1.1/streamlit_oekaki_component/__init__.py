from __future__ import annotations
import base64
from pathlib import Path
import numpy as np
import streamlit.components.v1 as components
from PIL import Image
import io
from dataclasses import dataclass

# Declare a Streamlit component
_frontend_dir = (Path(__file__).parent / "frontend").absolute()
_declare_component = components.declare_component("oekaki", path=str(_frontend_dir))


@dataclass
class OekakiResponse:
    is_submitted: bool
    image_data_np: np.ndarray | None


def _data_url_to_image(data_url: str) -> Image:
    _, encoded = data_url.split(";base64,")
    return Image.open(io.BytesIO(base64.b64decode(encoded)))


def oekaki(
    stroke_width: int = 20,
    stroke_color: str = "#000000",
    background_color: str = "",
    width: int = 300,
    height: int = 300,
    button_height: int = 30,
    submit_button_label: str = "Submit",
    submit_background_color: str = "#FAFAFA",
    clear_button_label: str = "Clear",
    clear_background_color: str = "#FAFAFA",
    key=None,
) -> OekakiResponse:
    component_value = _declare_component(
        strokeWidth=stroke_width,
        strokeColor=stroke_color,
        backgroundColor=background_color,
        canvasWidth=width,
        canvasHeight=height,
        buttonHeight=button_height,
        submitButtonLabel=submit_button_label,
        submitBackgroundColor=submit_background_color,
        clearButtonLabel=clear_button_label,
        clearBackgroundColor=clear_background_color,
        key=key,
        default=None,
    )

    is_submitted = (
        component_value.get("is_submitted", False) if component_value else False
    )
    image_data_np = (
        np.asarray(_data_url_to_image(component_value["image_data"]))
        if component_value and component_value.get("image_data")
        else None
    )

    return OekakiResponse(is_submitted=is_submitted, image_data_np=image_data_np)
