from manim import *


class miembros(Scene):
    def construct(self):
        Textos = [
            "nery kastillo",
            "Waldo Ratti",
            "Claudio Bloise",
            "Eduardo Marcelo Palacios",
            "Carlos Olivares Santis",
            "Manuel Alegría",
            "Lolailo Aviles Arroyo",
        ]
        txGracias = Text("Gracias por su apoyo", slant=ITALIC).scale(1.5)
        txGracias.shift(2.5 * UP)
        self.play(Write(txGracias))
        for texto in Textos:
            patrocinador = Text(texto).scale(1.2)
            self.play(FadeIn(patrocinador, shift=DOWN, Scale=0.66))
            self.play(ReplacementTransform(patrocinador, patrocinador))
            self.play(FadeOut(patrocinador, shift=DOWN * 2, Scale=1.5))
        self.wait(1)
