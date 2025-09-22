import customtkinter as ctk
from assistente import AssistenteIA

class AssistenteGUI:
    def __init__(self):
        # Configuração inicial
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.root = ctk.CTk()
        self.root.title("Code Mentor - Assistente de Programação")
        self.root.geometry("700x500")
        self.root.configure(fg_color="#0f111a")  

        self.assistente = AssistenteIA()

        # Frame principal
        self.main_frame = ctk.CTkFrame(self.root, fg_color="#0f111a", corner_radius=0)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=(10, 0))

        # Canvas para mensagens com scroll
        self.canvas = ctk.CTkCanvas(self.main_frame, bg="#0f111a", highlightthickness=0)
        self.scrollbar = ctk.CTkScrollbar(self.main_frame, command=self.canvas.yview)
        self.scrollable_frame = ctk.CTkFrame(self.canvas, fg_color="#0f111a")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Área inferior (input + botão)
        self.bottom_frame = ctk.CTkFrame(self.root, fg_color="#0f111a")
        self.bottom_frame.pack(fill="x", padx=10, pady=10)

        self.input_area = ctk.CTkTextbox(
            self.bottom_frame,
            height=50,
            wrap="word",
            fg_color="#1e1e2f",
            text_color="white",
            corner_radius=15,
            font=("Segoe UI", 13)
        )
        self.input_area.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.input_area.insert("1.0", "Digite sua mensagem...")
        self.input_area.bind("<FocusIn>", self.limpar_placeholder)
        self.input_area.bind("<Return>", self.enviar_enter)
        self.input_area.bind("<Shift-Return>", self.quebra_linha)

        self.enviar_btn = ctk.CTkButton(
            self.bottom_frame,
            text="➤",
            width=50,
            height=50,
            corner_radius=25,
            fg_color="#3b82f6",
            hover_color="#2563eb",
            command=self.enviar,
            font=("Segoe UI", 18, "bold")
        )
        self.enviar_btn.pack(side="right")

    # ==============================
    # Funções do chat
    # ==============================
    def adicionar_mensagem(self, remetente, mensagem, cor, lado="w"):
        """Adiciona bolhas de mensagem"""
        bubble = ctk.CTkFrame(
            self.scrollable_frame,
            fg_color=cor,
            corner_radius=20
        )
        label = ctk.CTkLabel(
            bubble,
            text=mensagem,
            wraplength=480,
            justify="left",
            text_color="white",
            font=("Segoe UI", 13),
            anchor="w"
        )
        label.pack(padx=12, pady=8)
        bubble.pack(anchor=lado, pady=6, padx=10)

        # Scroll automático
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

    def enviar(self):
        mensagem = self.input_area.get("1.0", "end").strip()
        if mensagem and mensagem != "Digite sua mensagem...":
            self.adicionar_mensagem("Você", mensagem, "#3b82f6", lado="e")  # azul user
            self.input_area.delete("1.0", "end")
            resposta = self.assistente.perguntar(mensagem)
            self.adicionar_mensagem("Assistente", resposta, "#16a34a", lado="w")  # verde ia

    def enviar_enter(self, event):
        self.enviar()
        return "break"  # evita quebra de linha automática

    def quebra_linha(self, event):
        self.input_area.insert("insert", "\n")

    def limpar_placeholder(self, event):
        if self.input_area.get("1.0", "end").strip() == "Digite sua mensagem...":
            self.input_area.delete("1.0", "end")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = AssistenteGUI()
    app.run()
