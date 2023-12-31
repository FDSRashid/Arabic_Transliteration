from camel_tools.utils.charmap import CharMapper
import os
import gradio as gr
from huggingface_hub import login
ar2bw = CharMapper.builtin_mapper('ar2bw')
bw2ar = CharMapper.builtin_mapper('bw2ar')
Secret_token = os.getenv('token')
login(token = Secret_token)
title = """#Transliterate using BuckWater Scheme"""
description = """
This app converts transliterated arabic text to Arabic using BuckWater Scheme. Use the following image to familiarize yourself with the conversion system.
"""
example = [["*hbt <lY Almktbp."]]

def getArabic(transliteration):
  return bw2ar(transliteration)

with gr.Blocks() as demo:
    gr.Markdown(title)
    gr.Markdown(description)
    gr.Image('https://huggingface.co/spaces/FDSRashid/Camel_tools_Test/resolve/main/Buckwalter-transliteration-for-Arabic-language.jpg')
    name = gr.Textbox(label="English Transliteration (Using Buckwater System )")
    output = gr.Textbox(label="Arabic Form of Text")
    greet_btn = gr.Button("Get Arabic")
    greet_btn.click(fn=getArabic, inputs=name, outputs=output)
    examples =  gr.Examples(examples = example, inputs = [name])

demo.launch()