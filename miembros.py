import os

import pandas as pd
from manim import *


def cargarData(archivo):
    # archivoData = FuncionesArchivos.UnirPath(ruta, archivo)
    if not os.path.exists(archivo):
        logger.warning(f"No se control {archivo}")
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

        avengers_and_thanos = ImageMobject("fondo.jpg").scale(0.1)
        self.add(avengers_and_thanos)
        self.play(FadeIn(avengers_and_thanos))

        self.play(Write(txGracias))

        for nombres in miembros["Miembro"]:
            patrocinador = Text(nombres).scale(1.2)
            self.play(FadeIn(patrocinador, shift=DOWN, Scale=0.66))
            self.play(ReplacementTransform(patrocinador, patrocinador))
            self.play(FadeOut(patrocinador, shift=DOWN * 2, Scale=1.5))
        self.wait(1)
