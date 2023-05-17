import os

import pandas as pd
from manim import *


def cargarData(archivo):
    if not os.path.exists(archivo):
        print(f"No se control {archivo}")
        return None
    data = pd.read_csv(archivo)
    return data

class miembros(Scene):
    def construct(self):
        miembros = cargarData("miembros.csv")
        if miembros is None:
            return

        txGracias = Text("Gracias por su apoyo", slant=ITALIC).scale(1.5)
        txGracias.shift(2.5 * UP)

        self.play(Write(txGracias))

        for nombres in miembros["Miembro"]:
            imagen = ImageMobject(f"fotos_miembros/{nombres}.jpg").scale(0.2)
            self.add(imagen)

            nombreMiembro = Text(nombres).scale(1.4)
            nombreMiembro.move_to([0,-1.5,0])

            border = nombreMiembro.copy()
            border.set_stroke(color=BLUE, width=8)
            self.add(border, nombreMiembro)
            self.play(
                       FadeIn(nombreMiembro, shift=DOWN, Scale=0.66), 
                       FadeIn(imagen, shift=DOWN, Scale=0.66),
                       FadeIn(border, shift=DOWN, Scale=0.66),)
            
            self.play(FadeOut(nombreMiembro, shift=DOWN * 2, Scale=1.5), FadeOut(imagen, shift=DOWN * 2, Scale=1.5))
            return
        self.wait(2)
