import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from pyswip import Prolog

# Professional Aesthetic Configuration
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

class AlShifaDiamondEdition:
    def __init__(self, root):
        self.root = root
        self.root.title("Al-Shifa AI Pharmacy System")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)

        # Luxury Medical Palette
        self.bg_color = "#0B0E14"       # Obsidian Black
        self.sidebar_color = "#11151C"  # Dark Charcoal
        self.card_bg = "#1A1F2B"       # Navy Slate
        self.accent_color = "#00F5D4"   # Electric Mint
        self.button_hover = "#00D1B2"
        self.text_secondary = "#94A3B8"
        
        # Prolog connection
        self.prolog = Prolog()
        try:
            self.prolog.consult("drugs.pl")
            self.prolog.consult("rules.pl")
            self.drug_list = self.get_all_drugs()
        except Exception:
            self.drug_list = ["System Data Error"]

        # --- Sidebar (Navigation & Credits) ---
        self.sidebar = ctk.CTkFrame(self.root, width=280, corner_radius=0, fg_color=self.sidebar_color, border_width=0)
        self.sidebar.pack(side="left", fill="y")
        
        # Brand Identity
        self.brand_label = ctk.CTkLabel(self.sidebar, text="✚ AL-SHIFA", 
                                        font=ctk.CTkFont(family="Inter", size=32, weight="bold"),
                                        text_color=self.accent_color)
        self.brand_label.pack(pady=(60, 5))
        self.sub_brand = ctk.CTkLabel(self.sidebar, text="EXPERT INTELLIGENCE", font=ctk.CTkFont(size=10, weight="bold"), text_color=self.text_secondary)
        self.sub_brand.pack(pady=(0, 50))
        
        # Supervisor Label (Clean Typography instead of Box)
        self.sup_title = ctk.CTkLabel(self.sidebar, text="ACADEMIC SUPERVISOR", font=ctk.CTkFont(size=11, weight="bold"), text_color=self.accent_color)
        self.sup_title.pack(pady=(20, 0))
        self.sup_name = ctk.CTkLabel(self.sidebar, text="Eng. Rewan Nour", font=ctk.CTkFont(size=16), text_color="white")
        self.sup_name.pack(pady=(0, 40))

        # --- Main Dashboard ---
        self.main_area = ctk.CTkFrame(self.root, corner_radius=0, fg_color=self.bg_color)
        self.main_area.pack(side="right", fill="both", expand=True)

        self.header_title = ctk.CTkLabel(self.main_area, text="Interaction Diagnostic Center", 
                                         font=ctk.CTkFont(family="Inter", size=28, weight="bold"), text_color="white")
        self.header_title.pack(pady=(60, 40), padx=50, anchor="w")

        # Interaction Selection Card
        self.card = ctk.CTkFrame(self.main_area, fg_color=self.card_bg, corner_radius=25)
        self.card.pack(pady=10, padx=50, fill="x")

        # Drug 1 Dropdown
        self.d1_label = ctk.CTkLabel(self.card, text="PATIENT MEDICATION", font=ctk.CTkFont(size=12, weight="bold"), text_color=self.text_secondary)
        self.d1_label.grid(row=0, column=0, padx=35, pady=(30, 5), sticky="w")
        self.combo1 = ctk.CTkOptionMenu(self.card, values=self.drug_list, width=280, height=45, corner_radius=12,
                                        fg_color=self.bg_color, button_color="#2463EB", dropdown_fg_color=self.card_bg)
        self.combo1.grid(row=1, column=0, padx=30, pady=(0, 40))

        # Drug 2 Dropdown
        self.d2_label = ctk.CTkLabel(self.card, text="NEW PRESCRIPTION", font=ctk.CTkFont(size=12, weight="bold"), text_color=self.text_secondary)
        self.d2_label.grid(row=0, column=1, padx=35, pady=(30, 5), sticky="w")
        self.combo2 = ctk.CTkOptionMenu(self.card, values=self.drug_list, width=280, height=45, corner_radius=12,
                                        fg_color=self.bg_color, button_color="#2463EB", dropdown_fg_color=self.card_bg)
        self.combo2.grid(row=1, column=1, padx=30, pady=(0, 40))

        # Action Buttons
        self.btn_frame = ctk.CTkFrame(self.main_area, fg_color="transparent")
        self.btn_frame.pack(pady=30, padx=50, fill="x")

        self.btn_check = ctk.CTkButton(self.btn_frame, text="GENERATE ANALYSIS", command=self.check_interaction,
                                       fg_color=self.accent_color, hover_color=self.button_hover, text_color=self.bg_color,
                                       font=ctk.CTkFont(size=14, weight="bold"), height=55, corner_radius=15)
        self.btn_check.pack(side="left", expand=True, padx=(0, 15), fill="x")

        self.btn_advice = ctk.CTkButton(self.btn_frame, text="CLINICAL ADVICE", command=self.get_recommendation,
                                        fg_color="transparent", border_width=2, border_color="#2463EB",
                                        hover_color="#1E293B", font=ctk.CTkFont(size=14, weight="bold"),
                                        height=55, corner_radius=15)
        self.btn_advice.pack(side="left", expand=True, padx=(15, 0), fill="x")

        # Analysis Terminal
        self.result_box = ctk.CTkTextbox(self.main_area, corner_radius=20, fg_color="#0D1117",
                                         border_width=1, border_color="#1E293B", font=("Consolas", 15), 
                                         text_color="#E2E8F0", padx=30, pady=30)
        self.result_box.pack(pady=(10, 30), padx=50, fill="both", expand=True)
        self.result_box.configure(state="disabled")

        # Sidebar Footer
        members = f"PROJECT TEAM\n{'-'*20}\nHamsa Mustafa\nRewan Mamdouh\nMariem Hassan\nYasmen Abdelaziz"
        self.footer = ctk.CTkLabel(self.sidebar, text=members, font=ctk.CTkFont(size=11), 
                                   text_color=self.text_secondary, justify="left")
        self.footer.pack(side="bottom", pady=50, padx=40)

    def get_all_drugs(self):
        try:
            return sorted(list(set([res['Drug'] for res in self.prolog.query("drug_class(Drug, _)") ])))
        except Exception:
            return ["No Data Found"]

    def check_interaction(self):
        d1, d2 = self.combo1.get(), self.combo2.get()
        query = f"(interaction({d1}, {d2}, Sev, Desc) ; interaction({d2}, {d1}, Sev, SevDesc))"
        results = list(self.prolog.query(query))
        
        self.result_box.configure(state="normal")
        self.result_box.delete("1.0", tk.END)
        if results:
            res = results[0]
            desc = res.get('Desc') or res.get('SevDesc')
            self.result_box.insert("1.0", f"--- DIAGNOSTIC REPORT ---\n\nSTATUS: INTERACTION DETECTED\nSEVERITY: {res['Sev'].upper()}\n\nDETAILS:\n{desc}")
        else:
            self.result_box.insert("1.0", "--- DIAGNOSTIC REPORT ---\n\nSTATUS: NO INTERACTION FOUND\n\nClinical data suggests this combination is stable.")
        self.result_box.configure(state="disabled")

    def get_recommendation(self):
        d1, d2 = self.combo1.get(), self.combo2.get()
        query = f"(interaction({d1}, {d2}, Sev, _) ; interaction({d2}, {d1}, Sev, _))"
        results = list(self.prolog.query(query))
        
        self.result_box.configure(state="normal")
        self.result_box.delete("1.0", tk.END)
        if results:
            sev = results[0]['Sev']
            advice = "CRITICAL: Contraindicated. Consult physician for alternative therapy." if sev == 'severe' else "ADVISORY: Monitor patient for increased side effects."
            self.result_box.insert("1.0", f"--- CLINICAL ADVICE ---\n\n{advice}")
        else:
            self.result_box.insert("1.0", "--- CLINICAL ADVICE ---\n\nNo specific precautions needed for this combination.")
        self.result_box.configure(state="disabled")

if __name__ == "__main__":
    app_root = ctk.CTk()
    app = AlShifaDiamondEdition(app_root)
    app_root.mainloop()