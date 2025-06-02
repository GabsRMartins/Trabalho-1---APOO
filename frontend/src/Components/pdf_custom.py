
from fpdf import FPDF

class CustomPDF(FPDF):
        def __init__(self, bg_path):
            super().__init__()
            self.bg_path = bg_path

        def header(self):
            # Adiciona imagem de fundo com transparência
            if self.bg_path:
                self.set_auto_page_break(auto=False)
                self.image(self.bg_path, x=0, y=0, w=210, h=297)

        def rounded_rect(self, x, y, w, h, r, style=''):
            """Desenha retângulo com cantos arredondados."""
            k = self.k
            hp = self.h
            op = {'F': 'f', 'FD': 'B', 'DF': 'B'}.get(style, 'S')
            MyArc = 4/3 * (2**0.5 - 1)
            self._out(f'{x * k:.2f} {(hp - y) * k:.2f} m')
            x0 = x + r
            y0 = y + r
            x1 = x + w - r
            y1 = y + h - r
            self._out(f'{x1 * k:.2f} {(hp - y) * k:.2f} l')
            self._out(f'{(x + w) * k:.2f} {(hp - y) * k:.2f} {((x + w) * k):.2f} {(hp - y0) * k:.2f} {((x + w) * k):.2f} {(hp - y0) * k:.2f} c')
            self._out(f'{((x + w) * k):.2f} {(hp - y1) * k:.2f} l')
            self._out(f'{((x + w) * k):.2f} {(hp - (y + h)) * k:.2f} {x1 * k:.2f} {(hp - (y + h)) * k:.2f} {x1 * k:.2f} {(hp - (y + h)) * k:.2f} c')
            self._out(f'{x0 * k:.2f} {(hp - (y + h)) * k:.2f} l')
            self._out(f'{x * k:.2f} {(hp - (y + h)) * k:.2f} {x * k:.2f} {(hp - y1) * k:.2f} {x * k:.2f} {(hp - y1) * k:.2f} c')
            self._out(f'{x * k:.2f} {(hp - y0) * k:.2f} l')
            self._out(f'{x * k:.2f} {(hp - y) * k:.2f} {x0 * k:.2f} {(hp - y) * k:.2f} {x0 * k:.2f} {(hp - y) * k:.2f} c')
            self._out(op)

        def add_event_card(self, nome, horario, local, preco):
            y = self.get_y()
            box_height = 25

            # Fundo branco com borda cinza clara
            self.set_fill_color(255, 255, 255)
            self.set_draw_color(200, 200, 200)
            self.rounded_rect(10, y, 190, box_height, 4, style='DF')

            # Nome do evento
            self.set_xy(14, y + 2)
            self.set_font("Arial", "B", 13)
            self.set_text_color(51, 51, 51)
            self.cell(0, 6, nome, ln=True)

            # Informações
            self.set_xy(14, y + 10)
            self.set_font("Arial", "", 11)
            self.set_text_color(80, 80, 80)
            texto_info = f"Horário: {horario} | Local: {local} | Preço: R$ {preco:.2f}"
            self.cell(0, 5, texto_info, ln=True)

            self.ln(10)