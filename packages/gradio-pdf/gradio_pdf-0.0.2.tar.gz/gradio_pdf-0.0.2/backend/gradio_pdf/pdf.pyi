from gradio.components.base import Component

from gradio.events import Dependency

class PDF(Component):

    data_model = FileData

    def __init__(self, value: Any = None, *, height: int | None = None, label: str | None = None, info: str | None = None, show_label: bool | None = None, container: bool = True, scale: int | None = None, min_width: int | None = None, interactive: bool | None = None, visible: bool = True, elem_id: str | None = None, elem_classes: list[str] | str | None = None, render: bool = True, load_fn: Callable[..., Any] | None = None, every: float | None = None):
        super().__init__(value, label=label, info=info, show_label=show_label, container=container, scale=scale, min_width=min_width, interactive=interactive, visible=visible, elem_id=elem_id, elem_classes=elem_classes, render=render, load_fn=load_fn, every=every)
        self.height = height

    def preprocess(self, payload: FileData) -> str:
        return payload.path

    def postprocess(self, value: str | None) -> FileData:
        if not value:
            return None
        return FileData(path=value)

    def example_inputs(self):
        return {"foo": "bar"}

    def api_info(self):
        return {"type": {}, "description": "any valid json"}

    def as_example(self, input_data: str | None) -> str | None:
        if input_data is None:
            return None
        return processing_utils.move_resource_to_block_cache(input_data, self)