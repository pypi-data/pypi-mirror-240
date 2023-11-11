
import gradio as gr
from gradio_blurhashimage import BlurhashImage


demo = gr.Interface(
    lambda x:x,
    gr.Image(),
    BlurhashImage(),
)
demo.launch()
