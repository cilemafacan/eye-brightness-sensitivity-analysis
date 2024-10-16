import gradio as gr
from PIL import Image, ImageDraw 

COUNT=0
shape = [(0,0), (512,512)]
img = Image.new("RGB", (512, 512)) 
img = ImageDraw.Draw(img)   

def calc_gray(param='Increase'):
    global COUNT, img, shape

    if param == 'Increase':
        if COUNT < 255:
            COUNT += 1
    else:
        if COUNT > 0:
            COUNT -= 1

    rgb = (COUNT, COUNT, COUNT)
    img.rectangle(shape, fill =rgb) 
    image = img._image

    return rgb, image

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            gr.Label("Eye Brigthness Sensitivity Analysis", show_label=False)
            rgb_val = gr.Text(value=("(0, 0, 0)"), label="RGB", text_align="center")
    with gr.Row():
        with gr.Column(scale=1):
            btn1 = gr.Button("Decrease")
        with gr.Column(scale=6):
            image = gr.Image(img._image, show_label=False)
        with gr.Column(scale=1):
            btn2 = gr.Button("Increase")

    btn1.click(fn=calc_gray, inputs=[btn1], outputs=[rgb_val, image])
    btn2.click(fn=calc_gray, inputs=[btn2], outputs=[rgb_val, image])
    
    
demo.launch(server_name="0.0.0.0", server_port=3033, debug=True) 
