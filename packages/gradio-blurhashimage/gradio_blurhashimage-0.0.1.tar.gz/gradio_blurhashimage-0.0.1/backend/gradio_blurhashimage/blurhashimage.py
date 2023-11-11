"""gr.Image() component."""

from __future__ import annotations

import warnings
from pathlib import Path
from typing import Any, Literal, cast

import numpy as np
from gradio_client.documentation import document, set_documentation_group
from PIL import Image as _Image  # using _ to minimize namespace pollution

import blurhash
import gradio.image_utils as image_utils
from gradio import processing_utils, utils
from gradio.components.base import Component
from gradio.data_classes import FileData, GradioModel
from gradio.events import Events
from typing import Optional

set_documentation_group("component")
_Image.init()  # fixes https://github.com/gradio-app/gradio/issues/2843

class BlurhashFileData(GradioModel):
    image: FileData = None
    blurhash: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None

@document()
class BlurhashImage(Component):
    """
    Creates an image component that can be used to display images (as an output). A blurhash image is displayed until the image is fully loaded.
    Preprocessing: passes the uploaded image as a {numpy.array}, {PIL.Image} or {str} filepath depending on `type`.
    Postprocessing: expects a {numpy.array}, {PIL.Image} or {str} or {pathlib.Path} filepath to an image and displays the image.
    Examples-format: a {str} local filepath or URL to an image.
    Demos: image_mod, image_mod_default_image
    Guides: image-classification-in-pytorch, image-classification-in-tensorflow, image-classification-with-vision-transformers, create-your-own-friends-with-a-gan
    """

    EVENTS = [
        Events.clear,
        Events.change,
        Events.stream,
        Events.select,
        Events.upload,
    ]

    data_model = BlurhashFileData

    def __init__(
        self,
        value: str | _Image.Image | np.ndarray | None = None,
        *,
        height: int | None = None,
        width: int | None = None,
        image_mode: Literal[
            "1", "L", "P", "RGB", "RGBA", "CMYK", "YCbCr", "LAB", "HSV", "I", "F"
        ] = "RGB",
        type: Literal["numpy", "pil", "filepath"] = "numpy",
        label: str | None = None,
        every: float | None = None,
        show_label: bool | None = None,
        show_download_button: bool = True,
        container: bool = True,
        scale: int | None = None,
        min_width: int = 160,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
        show_share_button: bool | None = None,
    ):
        """
        Parameters:
            value: A PIL BlurhashImage, numpy array, path or URL for the default value that BlurhashImage component is going to take. If callable, the function will be called whenever the app loads to set the initial value of the component.
            height: Height of the displayed image in pixels.
            width: Width of the displayed image in pixels.
            image_mode: "RGB" if color, or "L" if black and white. See https://pillow.readthedocs.io/en/stable/handbook/concepts.html for other supported image modes and their meaning.
            type: The format the image is converted to before being passed into the prediction function. "numpy" converts the image to a numpy array with shape (height, width, 3) and values from 0 to 255, "pil" converts the image to a PIL image object, "filepath" passes a str path to a temporary file containing the image.
            label: The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.
            every: If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.
            show_label: if True, will display label.
            show_download_button: If True, will display button to download image.
            container: If True, will place the component in a container - providing some extra padding around the border.
            scale: relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.
            min_width: minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.
            visible: If False, component will be hidden.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
            render: If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.
            show_share_button: If True, will show a share icon in the corner of the component that allows user to share outputs to Hugging Face Spaces Discussions. If False, icon does not appear. If set to None (default behavior), then the icon appears if this Gradio app is launched on Spaces, but not otherwise.
        """
        valid_types = ["numpy", "pil", "filepath"]
        if type not in valid_types:
            raise ValueError(
                f"Invalid value for parameter `type`: {type}. Please choose from one of: {valid_types}"
            )
        self.type = type
        self.height = height
        self.width = width
        self.image_mode = image_mode

        self.show_download_button = show_download_button
        self.show_share_button = (
            (utils.get_space() is not None)
            if show_share_button is None
            else show_share_button
        )
        super().__init__(
            label=label,
            every=every,
            show_label=show_label,
            container=container,
            scale=scale,
            min_width=min_width,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            render=render,
            value=value,
        )

    def preprocess(
        self, payload: BlurhashFileData | None
    ) -> np.ndarray | _Image.Image | str | None:
        if payload is None:
            return payload
        im = _Image.open(payload.image.path)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            im = im.convert(self.image_mode)
        return image_utils.format_image(
            im, cast(Literal["numpy", "pil", "filepath"], self.type), self.GRADIO_CACHE
        )

    def postprocess(
        self, value: np.ndarray | _Image.Image | str | Path | None
    ) -> BlurhashFileData | None:
        if value is None:
            return None
        path = image_utils.save_image(value, self.GRADIO_CACHE)
        image = _Image.open(path)

        return BlurhashFileData(
            image=FileData(path=path),
            blurhash=blurhash.encode(image, x_components=5, y_components=5),
            width=image.width,
            height=image.height,
        )

    def as_example(self, input_data: str | Path | None) -> str | None:
        if input_data is None:
            return None
        return processing_utils.move_resource_to_block_cache(input_data, self)

    def example_inputs(self) -> Any:
        return "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png"