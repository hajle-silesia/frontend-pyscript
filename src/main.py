from js import document, console, FileReader
from pyodide.http import pyfetch
from pyodide import JsException
import datetime
import asyncio
from pyodide import create_proxy
import json
import base64


# async def foo():
#     while True:
#         await asyncio.sleep(1)
#         console.log("tu")
#         output = datetime.datetime.now()
#         Element("outputDiv2").write(output)


def read_complete(event):
    output = document.getElementById("output")
    output.innerText = event.target.result
    asyncio.ensure_future(upload(event.target.result))


async def upload_file(*args, **kwargs):
    file_list = document.getElementById("upload").files
    for file in file_list:
        reader = FileReader.new()
        onload_event = create_proxy(read_complete)
        reader.onload = onload_event
        reader.readAsText(file)
    return


def activate_tab(*args, **kwargs):
    console.log(f"target.id: {args[0].target.id}")
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


def on_click(evt):
    show()


async def upload(file):
    try:
        response = await pyfetch(url="http://localhost:8083/update",
                                 method="POST",
                                 headers={"Content-Type": "application/json"},
                                 body=base64.b64encode(json.dumps(file, default=str).encode()),
                                 mode="no-cors",
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

button = document.getElementById("upload")
button.addEventListener("change", create_proxy(upload_file))
