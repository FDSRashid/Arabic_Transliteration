from camel_tools.utils.charmap import CharMapper

import gradio as gr
ar2bw = CharMapper.builtin_mapper('ar2bw')
bw2ar = CharMapper.builtin_mapper('bw2ar')

def getArabic(transliteration = '*hbt <lY Almktbp.'):
  return bw2ar(transliteration)

with gr.Blocks() as demo:
    name = gr.Textbox(label="English Transliteration (Using Buckwater System )")
    output = gr.Textbox(label="Arabic Form of Text")
    greet_btn = gr.Button("Get Arabic")
    greet_btn.click(fn=getArabic, inputs=name, outputs=output)

demo.launch()