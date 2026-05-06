import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from pyswip import Prolog

# Professional Aesthetic Configuration
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

class AlShifaDiamondFeedback:
    def __init__(self, root):
        self.root = root
        self.root.title("Al-Shifa AI Pharmacy System")
        self.root.geometry("1000x750")
        self.root.resizable(False, False)

        # Luxury Medical Palette
        self.bg_color = "#0B0E14"
        self.sidebar_color = "#11151C"
        self.card_bg = "#1A1F2B"
        self.accent_mint = "#00F5D4"   # Safe Color
        self.accent_red = "#FF4C4C"    # Danger Color
        self.accent_blue = "#2463EB"   # Clinical Blue
        self.text_secondary = "#94A3B8"
        
        # Prolog connection
        self.prolog = Prolog()
        try:
            self.prolog.consult("drugs.pl")
            self.prolog.consult("rules.pl")
            self.drug_list = self.get_all_drugs()
        except Exception:
            self.drug_list = ["System Data Error"]

        # --- Sidebar ---
        self.sidebar = ctk.CTkFrame(self.root, width=280, corner_radius=0, fg_color=self.sidebar_color)
        self.sidebar.pack(side="left", fill="y")
        
        self.brand_label = ctk.CTkLabel(self.sidebar, text="✚ AL-SHIFA", font=ctk.CTkFont(size=32, weight="bold"), text_color=self.accent_mint)
        self.brand_label.pack(pady=(60, 5))
        
        self.sup_title = ctk.CTkLabel(self.sidebar, text="ACADEMIC SUPERVISOR", font=ctk.CTkFont(size=11, weight="bold"), text_color=self.accent_mint)
        self.sup_title.pack(pady=(20, 0))
        self.sup_name = ctk.CTkLabel(self.sidebar, text="Eng. Rewan Nour", font=ctk.CTkFont(size=16), text_color="white")
        self.sup_name.pack(pady=(0, 40))

        # --- Main Dashboard ---
        self.main_area = ctk.CTkFrame(self.root, corner_radius=0, fg_color=self.bg_color)
        self.main_area.pack(side="right", fill="both", expand=True)

        self.header_title = ctk.CTkLabel(self.main_area, text="Interaction Diagnostic Center", font=ctk.CTkFont(size=28, weight="bold"), text_color="white")
        self.header_title.pack(pady=(60, 40), padx=50, anchor="w")

        # Interaction Card
        self.card = ctk.CTkFrame(self.main_area, fg_color=self.card_bg, corner_radius=25)
        self.card.pack(pady=10, padx=50, fill="x")

        self.combo1 = ctk.CTkOptionMenu(self.card, values=self.drug_list, width=280, height=45, corner_radius=12, fg_color=self.bg_color, button_color=self.accent_blue)
        self.combo1.grid(row=0, column=0, padx=30, pady=40)

        self.combo2 = ctk.CTkOptionMenu(self.card, values=self.drug_list, width=280, height=45, corner_radius=12, fg_color=self.bg_color, button_color=self.accent_blue)
        self.combo2.grid(row=0, column=1, padx=30, pady=40)

        # Action Buttons
        self.btn_frame = ctk.CTkFrame(self.main_area, fg_color="transparent")
        self.btn_frame.pack(pady=30, padx=50, fill="x")

        self.btn_check = ctk.CTkButton(self.btn_frame, text="GENERATE ANALYSIS", command=self.check_interaction, fg_color=self.accent_mint, text_color=self.bg_color, font=ctk.CTkFont(weight="bold"), height=55, corner_radius=15)
        self.btn_check.pack(side="left", expand=True, padx=(0, 15), fill="x")

        self.btn_advice = ctk.CTkButton(self.btn_frame, text="CLINICAL ADVICE", command=self.get_recommendation, fg_color="transparent", border_width=2, border_color=self.accent_blue, font=ctk.CTkFont(weight="bold"), height=55, corner_radius=15)
        self.btn_advice.pack(side="left", expand=True, padx=(15, 0), fill="x")

        # --- Diagnostic Terminal (The Feedback Zone) ---
        self.status_indicator = ctk.CTkLabel(self.main_area, text="SYSTEM READY", font=ctk.CTkFont(size=12, weight="bold"), text_color=self.text_secondary)
        self.status_indicator.pack(pady=(10, 0), padx=55, anchor="w")

        self.result_box = ctk.CTkTextbox(self.main_area, corner_radius=20, fg_color="#0D1117", border_width=2, border_color="#1E293B", font=("Consolas", 15), text_color="#E2E8F0", padx=30, pady=30)
        self.result_box.pack(pady=(5, 30), padx=50, fill="both", expand=True)
        self.result_box.configure(state="disabled")

        # Sidebar Footer
        members = f"PROJECT TEAM\n{'-'*20}\nHamsa Mustafa\nRewan Mamdouh\nMariem Hassan\nYasmen Abdelaziz"
        self.footer = ctk.CTkLabel(self.sidebar, text=members, font=ctk.CTkFont(size=11), text_color=self.text_secondary, justify="left")
        self.footer.pack(side="bottom", pady=50, padx=40)

    def get_all_drugs(self):
        try:
            return sorted(list(set([res['Drug'] for res in self.prolog.query("drug_class(Drug, _)") ])))
        except: return ["Error"]

    def update_result(self, message, is_safe=True):
        self.result_box.configure(state="normal")
        self.result_box.delete("1.0", tk.END)
        self.result_box.insert("1.0", message)
        
        if is_safe:
            self.result_box.configure(border_color=self.accent_mint)
            self.status_indicator.configure(text="● ANALYSIS COMPLETE: SAFE", text_color=self.accent_mint)
        else:
            self.result_box.configure(border_color=self.accent_red)
            self.status_indicator.configure(text="● ANALYSIS COMPLETE: DANGER DETECTED", text_color=self.accent_red)
        
        self.result_box.configure(state="disabled")

    def check_interaction(self):
        d1, d2 = self.combo1.get(), self.combo2.get()
        query = f"(interaction({d1}, {d2}, Sev, Desc) ; interaction({d2}, {d1}, Sev, SevDesc))"
        results = list(self.prolog.query(query))
        
        if results:
            res = results[0]
            desc = res.get('Desc') or res.get('SevDesc')
            msg = f"--- DIAGNOSTIC REPORT ---\n\nSTATUS: INTERACTION DETECTED\nSEVERITY: {res['Sev'].upper()}\n\nDETAILS:\n{desc}"
            self.update_result(msg, is_safe=False)
        else:
            msg = "--- DIAGNOSTIC REPORT ---\n\nSTATUS: NO INTERACTION FOUND\n\nClinical data suggests this combination is stable."
            self.update_result(msg, is_safe=True)

    def get_recommendation(self):
        d1, d2 = self.combo1.get(), self.combo2.get()
        query = f"(interaction({d1}, {d2}, Sev, _) ; interaction({d2}, {d1}, Sev, _))"
        results = list(self.prolog.query(query))
        
        if results:
            sev = results[0]['Sev']
            advice = "CRITICAL: Contraindicated. Consult physician." if sev == 'severe' else "ADVISORY: Monitor for side effects."
            self.update_result(f"--- CLINICAL ADVICE ---\n\n{advice}", is_safe=False)
        else:
            self.update_result("--- CLINICAL ADVICE ---\n\nNo specific precautions needed.", is_safe=True)

if __name__ == "__main__":
    app_root = ctk.CTk()
    AlShifaDiamondFeedback(app_root)
    app_root.mainloop()