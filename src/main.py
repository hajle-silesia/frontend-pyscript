from js import document

def show(*ags, **kwargs):
    document.querySelector("img.pump_2").hidden = True


brewery_bg = "./img/brewery_bg.png"
button_off = "./img/button_off.png"
button_on = "./img/button_on.png"
document.querySelector("img.brewery_bg").setAttribute("src", brewery_bg)
document.querySelector("img.pump_1").setAttribute("src", button_off)
document.querySelector("img.pump_1").hidden = True
document.querySelector("img.pump_2").setAttribute("src", button_off)
document.querySelector("img.pump_3").setAttribute("src", button_off)
document.querySelector("img.bk_drain").setAttribute("src", button_off)
document.querySelector("img.bk_wort").setAttribute("src", button_off)
document.querySelector("img.bk_whirlpool").setAttribute("src", button_off)
document.querySelector("img.pump_1_cfc").setAttribute("src", button_off)
document.querySelector("img.pump_1_wort_out").setAttribute("src", button_off)
document.querySelector("img.pump_1_drain").setAttribute("src", button_off)
document.querySelector("img.cfc_drain").setAttribute("src", button_off)
document.querySelector("img.water_in_cfc").setAttribute("src", button_off)
document.querySelector("img.pump_2_pump_1").setAttribute("src", button_off)
document.querySelector("img.pump_2_rims").setAttribute("src", button_off)
document.querySelector("img.mlt_recirculation").setAttribute("src", button_off)
document.querySelector("img.water_in_pump_3").setAttribute("src", button_off)
document.querySelector("img.pump_3_hlt").setAttribute("src", button_off)
document.querySelector("img.pump_3_rims").setAttribute("src", button_off)
document.querySelector("img.hlt_drain").setAttribute("src", button_off)
document.querySelector("img.bk_cip").setAttribute("src", button_off)
document.querySelector("img.mlt_cip").setAttribute("src", button_off)
document.querySelector("img.mlt_sightglass").setAttribute("src", button_off)
document.querySelector("img.mlt_sightglass_cam").setAttribute("src", button_off)
document.querySelector("img.mlt_sightglass_size").setAttribute("src", button_off)
