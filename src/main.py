from js import document


def show(*ags, **kwargs):
    document.getElementById("pump_1").setAttribute("src", button_on)
    document.getElementById("pump_2").hidden = True


brewery_bg = "./img/brewery_bg.png"
button_off = "./img/button_off.png"
button_on = "./img/button_on.png"
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
