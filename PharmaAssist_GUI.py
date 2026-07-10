# =====================
# PHARMAASSIST GUI V1.0
# Developed by Daksh Gohil
# =====================


# IMPORTS
import tkinter as tk
from tkinter import messagebox
import difflib
import json
# =====================


# MEDICINE DATABASE
medicines ={ "paracetamol":
                      {"uses":"Fever,Headache,Body pain",
                      "side_effects":"Nausea,Rashes",
                       "when_to_take":"After food if stomach is sensitive",
                       "age_group":"children and adults",
                       "warnings":"do not exceed the recommended dose",
                       "food":"Can be taken with or without food",
                       "storage":"Store in a coll, dry place",
                       "dosage":"As prescribed",
                       "pregnancy":"Generally considered safe if prescribed",
                       "breastfeeding":"usually safe",
                       "driving":"Safe",
                       "alcohol":"Avoid excessive alcohol",
                       "prescription":"Not always required",
                       "missed_dose":"Take when remembered unless near the next dose",
                       "overdose":"Seek immediate medical attention",
                       "common_brand":["Dolo 650","Crocin","Calpol"],
                       "generic_name":"Paracetamol",
                       "medicine_type":"Analgesic,Antipyretic"},
                 "ibuprofen":
                      {"uses":"Pain,Sweling,Fever, Inflammation, Toothache,Muscle pain",
                      "side_effects":"Stomach pain,Nausea, Hearnurn Dizziness",
                       "when_to_take":"After food",
                       "age_group":"Children (Age-specific doses )and Adults",
                       "warnings":"Avoid if you have a stomach ulcres, kidney disease, or severe heart diseae. Do not exceed the recommended dose",
                       "food":"Take after food or Milk",
                       "storage":"Store in a cool, dry place below 25'C",
                       "dosage":"As prescribed by a doctor or according to the label",
                       "pregnancy":"Avoid during the last trimester unless prescribed by a doctor",
                       "breastfeeding":"Generally considered safe for short-term use",
                       "driving":"Usually safe , but avoid driving if you feel dizzy",
                       "alcohol":"Avoid alcohol as it increases the risk of stomach bleeding",
                       "prescription":"OTC (Over-the-counter)for some strengths; higher strengths may require a prescription",
                       "missed_dose":"Take when rembered unless it is almost time for the next dose  ",
                       "overdose":"Seek immediate medical attention or contact a poison center",
                       "common_brand":["Brufen","Advil","Ibugesic"],
                       "generic_name":"Ibuprofen",
                       "medicine_type":"NSAID(Non-Steroidal Anti-Inflammatory Drug)"
                       },
                 "cetrizine":
                      {"uses":"Allergic rhintis,Sneezing,Runny nose,Itching, Hives(Urticaria)",
                      "side_effects":"Drowsiness,dry mouth, headache, fatigue",
                       "when_to_take":"Usually in the evening or at bedtime if it causes drowsiness",
                       "age_group":"Children (ade-specific doses) and Adults",
                       "warnings":"May cause drowsiness. Avoid activites requiring alertness if affected",
                       "food":"Can be taken with or without food",
                       "storage":"Store in  a cool, dry place below 25'C",
                       "dosage":"As prescribed by a doctor or according to the label",
                       "pregnancy":"Consult a doctor before use",
                       "breastfeeding":"Consult a doctor before use",
                       "driving":"Avoid driving or operating machinery if you feel sleepy",
                       "alcohol":"Avoid alcohol as it may increase drowsiness",
                       "prescription":"OTC (over-the-cunter)",
                       "missed_dose":"take when remembered unless it is almost time for the next dose",
                       "overdose":"Seek immediate medical attention",
                       "common_brand":["Cetzine", "Alerid" , "Okacet"],
                       "generic_name":"Cetrizine",
                       "medicine_type":"Antihistamine"}
                 }
# =====================
# GLOBAL VARIABLES
current_medicine = ""
try:
   with open("favourites.json", "r") as file:
       favourites = json.load(file)
except FileNotFoundError:
   favourites = []
   

# =====================
# GUI SETUP
root = tk.Tk()
try:
   root.iconbitmap("Assets/pharma.ico")
except:
   pass
root.resizable(True, True)
root.title("PharmaAssist GUI V1.0")
root.geometry("800x600")
root.configure(bg="#F5F7FA")
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)
# =====================


# MEDICINE FUNCTIONS
def show_medicine(name):
   global current_medicine
   current_medicine = name
   details = f"""
============================================================
MEDICINE NAME : {name.upper()}
============================================================


Generic Name: {medicines[name]["generic_name"]}
Medicine Type: {medicines[name]["medicine_type"]}
Common Brand: {",".join(medicines[name] ["common_brand"])}

____________________________________________________________

Uses: {medicines[name]["uses"]}
When to take: {medicines[name]["when_to_take"]}
Food: {medicines[name]["food"]}
Dosage: {medicines[name]["dosage"]}
Age Group: {medicines[name]["age_group"]}

____________________________________________________________

Side Effects: {medicines[name]["side_effects"]}
Warnings: {medicines[name]["warnings"]}
Pregnancy: {medicines[name]["pregnancy"]}
Breastfeeding: {medicines[name]["breastfeeding"]}
Driving: {medicines[name]["driving"]}
Alcohol: {medicines[name]["alcohol"]}

____________________________________________________________

Missed Dose:  {medicines[name]["missed_dose"]}
Overdose: {medicines[name]["overdose"]}
Storage: {medicines[name]["storage"]}
Prescription: {medicines[name]["prescription"]}
"""
   output_text.config(state="normal")
   output_text.insert(tk.END, details)
   output_text.config(state="disabled")
   copy_button.config(state="normal")

# Searches medicines by generic name, brand name or close spelling.
def search_medicine():
    medicine_name = search_entry.get().lower()
    found = False

   # Serch by medicine name
    if medicine_name in medicines:
       output_text.config(state="normal")
       output_text.delete("1.0",tk.END)
       show_medicine(medicine_name)
       found = True

   # Search by Brand name
    if not found:
        for medicine in medicines:
           for brand in medicines[medicine]["common_brand"]:
              if medicine_name == brand.lower():
                 output_text.config(state="normal")
                 output_text.delete("1.0",tk.END)
                 show_medicine(medicine)
                 found = True
                 break

           if found:
              break
    # Typo Correction
    if not found:
       matches = difflib.get_close_matches(medicine_name, medicines.keys(), n=1)
       
       if matches:
          output_text.config(state="normal")
          output_text.delete("1.0", tk.END)
          output_text.insert(tk.END,f"Showing results for: {matches[0].upper()}?\n" f'Based on your search:"{medicine_name}"\n\n')
          show_medicine(matches[0])

       else:
          output_text.config(state="normal")
          output_text.delete("1.0", tk.END)
          output_text.insert(tk.END, "Medicine not found.")
          output_text.config(state="disabled")
          copy_button.config(state="disabled")
          
    search_entry.delete(0, tk.END)
    search_entry.focus()
    
# Clears the search box and output area
def clear_search():
   search_entry.delete(0, tk.END)

   output_text.config(state="normal")
   output_text.delete("1.0", tk.END)
   output_text.config(state="disabled")
   copy_button.config(state="disabled")

   search_entry.focus()
   
# Copies the displayed medicine details to clipboard
def copy_details():
   root.clipboard_clear()
   root.clipboard_append(output_text.get("1.0", tk.END))
   copy_button.config(text="Copied")
   root.after(2000, lambda:
              copy_button.config(text="Copy"))
   
# Removes the Placeholder(Search medicine) when clicked.
def clear_placeholder(event):
   if search_entry.get() == "Search Medicine...":
      search_entry.delete(0, tk.END)

# About PHARMAASSIST      
def about():
    messagebox.showinfo("About PharmaAssist",
                        " Developed by Daksh Gohil\n\n"
                        " Version: GUI v1.0\n\n"
                        " A medicine information application\n"
                        " Built using Python and Tkinter.")
    
# Adds  the currently displayed medicine to favourites
def add_to_favourites():
   global current_medicine

   if current_medicine == "":
      messagebox.showwarning("No medicine","Search for a medicine first.")
      return
   if current_medicine not in favourites:
      favourites.append(current_medicine)
      with open("favourites.json", "w") as file:
         json.dump(favourites, file)
      messagebox.showinfo("Success", f"{current_medicine.title().upper()} added to favourites!")
   else:
      messagebox.showinfo("Already added", f"{current_medicine.title().upper()} is already in favourites!")
      
# Disaplays all the favourite medicines
def view_favourites():
   if not favourites:
      messagebox.showinfo("Favourites", "No favourite medicine yet.")
      return
   fav_text = "Favourite Medicines\n\n"

   for medicine in favourites:
      fav_text += f">{medicine.title().upper()}\n"

   messagebox.showinfo("Favourites", fav_text)

# Removes the currently displayed medicine from favourites
def remove_from_favourites():
   global current_medicine

   if current_medicine == "":
      messagebox.info.showwarning("No Medicine", "Search for a medicine first.")
      return
   if current_medicine in favourites:
      favourites.remove(current_medicine)
      with open("favourites.json", "w") as file:
         json.dump(favourites, file)
      messagebox.showinfo("Removed", f"{current_medicine.title().upper()} removed from favourites!")
   
   else:
      messagebox.showinfo("Not Found", f"{current_medicine.title().upper()} is not in favourites.")
# =====================
   
# MENU BAR
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About PharmaAssist", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)
favourites_menu = tk.Menu (menu_bar, tearoff=0)
favourites_menu.add_command(label="Add current Medicine", command=add_to_favourites)
favourites_menu.add_command(label="View Favourites", command=view_favourites)
favourites_menu.add_command(label="Remove Current Medicine", command=remove_from_favourites)
menu_bar.add_cascade(label="Favourites", menu=favourites_menu)
# =====================

# GUI WIDGETS
title = tk.Label(root, text="PharmaAssist", font=("Segoe UI", 22, "bold"), bg="#F5F7FA", fg="#1565C0")
title.pack(pady=(15, 10))
search_frame = tk.Frame(root)
search_frame.pack(pady=10)
# =====================

# EVENT BINDINGS
search_entry = tk.Entry(search_frame, font=("Segoe UI", 11), width=35 )
search_entry.grid(row=0, column=0, padx=10)
search_entry.insert(0,"Search Medicine...")
search_entry.bind("<FocusIn>", clear_placeholder)
# =====================


# GUI WIDGETS

# SEARCH BUTTON
search_button = tk.Button(search_frame, bg="#1976D2", fg="white", font=("Segoe UI", 10 , "bold"), cursor="hand2", text="Search",command=search_medicine)
search_button.grid(row=0, column=1, padx=10)

# CLEAR BUTTON
clear_button = tk.Button(search_frame, bg="#757575", fg="white", font=("Segoe UI", 10), cursor="hand2", text="Clear",command=clear_search)
clear_button.grid(row=0, column=2, padx=5)

# COPY BUTTON
copy_button = tk.Button(search_frame, bg="#388E3C", fg="white", font=("Segoe UI", 10), cursor="hand2", text="Copy",command=copy_details, state="disabled")
copy_button.grid(row=0, column=3, padx=5)
# =====================

#OUTPUT FRAME
output_frame = tk.Frame(root, bg="#F5F7FA")
output_frame.pack(fill="both", expand=True, padx=40, pady=10)

# OUTPUT 
output_text = tk.Text(output_frame, width =70, height =20, font=("Consolas", 11), bg="white", relief="groove", bd=2, padx=10, pady=10)
output_text.config(state="disabled")
output_text.pack( fill="both", expand=True , side="left")
# =====================

# GUI WIDGETS
# SCROLL BAR
scrollbar = tk.Scrollbar(output_frame)
scrollbar.config(command=output_text.yview)
output_text.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# =====================

# EVENT BINDINGS AND APPLY MENU
root.bind("<Return>", lambda event:search_medicine())
root.config(menu=menu_bar)
# =====================

# START APPLICATION
root.mainloop()
# =====================


# End of PharmaAssist GUI v1.0
