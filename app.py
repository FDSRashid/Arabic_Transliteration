from camel_tools.utils.charmap import CharMapper

import gradio as gr
ar2bw = CharMapper.builtin_mapper('ar2bw')
bw2ar = CharMapper.builtin_mapper('bw2ar')

title = """#Transliterate using BuckWater Scheme"""
description = """
<p>
<center>
This app converts transliterated arabic text to Arabic using BuckWater Scheme. Use the following image to familiarize yourself with the conversion system.
<img src="https://huggingface.co/spaces/FDSRashid/Camel_tools_Test/resolve/main/Buckwalter-transliteration-for-Arabic-language.jpg" alt="Test" >
</center>
</p>
"""
example = [["*hbt <lY Almktbp."]]

def getArabic(transliteration):
  return bw2ar(transliteration)

with gr.Blocks() as demo:
    gr.Markdown(title)
    gr.HTML(description)
    name = gr.Textbox(label="English Transliteration (Using Buckwater System )")
    output = gr.Textbox(label="Arabic Form of Text")
    greet_btn = gr.Button("Get Arabic")
    greet_btn.click(fn=getArabic, inputs=name, outputs=output)
    examples =  gr.Examples(examples = example, inputs = [name])

demo.launch()