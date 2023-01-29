import asyncio
import base64
import json

from js import document, window, console, FileReader
from pyodide import JsException
from pyodide import create_proxy
from pyodide.http import pyfetch


def read_complete(event):
    asyncio.ensure_future(upload(event.target.result))


async def upload_file(*args, **kwargs):
    file_list = document.getElementById("upload").files
    console.log(f"HREF: {window.location.href}")
    console.log(f"hostname : {window.location.hostname}")
    console.log(f"pathname : {window.location.pathname}")
    console.log(f"protocol : {window.location.protocol}")

    for file in file_list:
        reader = FileReader.new()
        onload_event = create_proxy(read_complete)
        reader.onload = onload_event
        reader.readAsText(file)
    document.getElementById('upload').value = ""
    return


async def activate_tab(*args, **kwargs):
    if "brewery_tab" in args[0].target.id:
        document.getElementById("recipe").hidden = True
        document.getElementById("brewery").hidden = False
    elif "recipe_tab" in args[0].target.id:
        document.getElementById("recipe").hidden = False
        document.getElementById("brewery").hidden = True


def show(*args, **kwargs):
    console.log(f"len args: {len(args)}")
    console.log(f"type: {args[0].type}")
    console.log(f"target: {args[0].target}")
    console.log(f"target.id: {args[0].target.id}")
    console.log(f"target.src: {args[0].target.src}")
    console.log(f"type(target.id): {type(args[0].target.id)}")

    document.getElementById("pump_1").setAttribute("src", button_on)
    document.getElementById("pump_2").hidden = True


async def upload(file):
    try:
        console.log(f"PUSHING HERE: {window.location.href}api/update")
        response = await pyfetch(url=f"{window.location.href}api/update",
                                 method="POST",
                                 # headers={'content-type': "application/json"},
                                 body=base64.b64encode(json.dumps(file, default=str).encode()),
                                 # mode="no-cors",
                                 )
        if response.ok:
            console.log("SENT TO FILE-CONTENT-MONITOR")
            # data = await response.json()
            # return data.get("token")
    except JsException:
        return None


brewery_bg = "./img/brewery_bg.png"
button_off = "./img/button_off.png"
button_on = "./img/button_on.png"


def main():
    document.getElementById("brewery_bg").setAttribute("src", brewery_bg)
    document.getElementById("pump_1").setAttribute("src", button_off)
    document.getElementById("pump_2").setAttribute("src", button_off)
    document.getElementById("pump_3").setAttribute("src", button_off)
    document.getElementById("bk_drain").setAttribute("src", button_off)
    document.getElementById("bk_wort").setAttribute("src", button_off)
    document.getElementById("bk_whirlpool").setAttribute("src", button_off)
    document.getElementById("pump_1_cfc").setAttribute("src", button_off)
    document.getElementById("pump_1_wort_out").setAttribute("src", button_off)
    document.getElementById("pump_1_drain").setAttribute("src", button_off)
    document.getElementById("cfc_drain").setAttribute("src", button_off)
    document.getElementById("water_in_cfc").setAttribute("src", button_off)
    document.getElementById("pump_2_pump_1").setAttribute("src", button_off)
    document.getElementById("pump_2_rims").setAttribute("src", button_off)
    document.getElementById("mlt_recirculation").setAttribute("src", button_off)
    document.getElementById("water_in_pump_3").setAttribute("src", button_off)
    document.getElementById("pump_3_hlt").setAttribute("src", button_off)
    document.getElementById("pump_3_rims").setAttribute("src", button_off)
    document.getElementById("hlt_drain").setAttribute("src", button_off)
    document.getElementById("bk_cip").setAttribute("src", button_off)
    document.getElementById("mlt_cip").setAttribute("src", button_off)
    document.getElementById("mlt_sightglass").setAttribute("src", button_off)
    document.getElementById("mlt_sightglass_cam").setAttribute("src", button_off)
    document.getElementById("mlt_sightglass_size").setAttribute("src", button_off)

    document.getElementById("recipe").hidden = True


main()

document.getElementById("label_recipe_upload").addEventListener("change", create_proxy(upload_file))
document.getElementById("recipe_tab_overlay").addEventListener("click", create_proxy(activate_tab))
document.getElementById("recipe_tab_text").addEventListener("click", create_proxy(activate_tab))
document.getElementById("brewery_tab_overlay").addEventListener("click", create_proxy(activate_tab))
document.getElementById("brewery_tab_text").addEventListener("click", create_proxy(activate_tab))
document.getElementById("pump_2").addEventListener("click", create_proxy(show))
