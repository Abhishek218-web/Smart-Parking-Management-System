
import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt


class ParkingManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Parking Management System")
        self.root.geometry("1050x700")
        self.root.configure(bg="#f1f5f9")

        self.total_slots = 10
        self.parking = [None] * self.total_slots

        # Sidebar
        self.sidebar = tk.Frame(root, bg="#172554", width=210)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(
            self.sidebar, text="PARKSMART",
            bg="#172554", fg="white",
            font=("Arial", 20, "bold")
        ).pack(pady=(28, 5))

        tk.Label(
            self.sidebar, text="Parking Management",
            bg="#172554", fg="#bfdbfe",
            font=("Arial", 10)
        ).pack(pady=(0, 25))

        self.add_menu_button("Dashboard", self.refresh_dashboard)
        self.add_menu_button("Park Vehicle", self.park_vehicle)
        self.add_menu_button("Remove Vehicle", self.remove_vehicle)
        self.add_menu_button("Search Vehicle", self.search_vehicle)
        self.add_menu_button("Update Vehicle", self.update_vehicle)
        self.add_menu_button("Parking Statistics", self.show_statistics)

        tk.Label(
            self.sidebar, text="PYTHON MINI PROJECT",
            bg="#172554", fg="#cbd5e1",
            font=("Arial", 8)
        ).pack(side="bottom", pady=20)

        # Main dashboard
        self.main = tk.Frame(root, bg="#f1f5f9")
        self.main.pack(side="left", fill="both", expand=True)

        header = tk.Frame(self.main, bg="white", height=70)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header, text="Parking Dashboard",
            bg="white", fg="#1e293b",
            font=("Arial", 19, "bold")
        ).pack(side="left", padx=25, pady=18)

        tk.Label(
            header, text="● System Ready",
            bg="white", fg="#16a34a",
            font=("Arial", 10, "bold")
        ).pack(side="right", padx=25)

        self.content = tk.Frame(self.main, bg="#f1f5f9")
        self.content.pack(fill="both", expand=True, padx=22, pady=20)

        tk.Label(
            self.content, text="Overview",
            bg="#f1f5f9", fg="#1e293b",
            font=("Arial", 17, "bold")
        ).pack(anchor="w")

        tk.Label(
            self.content,
            text="Manage parking slots and vehicle information.",
            bg="#f1f5f9", fg="#64748b",
            font=("Arial", 10)
        ).pack(anchor="w", pady=(4, 16))

        # Summary cards
        self.summary = tk.Frame(self.content, bg="#f1f5f9")
        self.summary.pack(fill="x", pady=(0, 18))

        self.total_label = self.create_summary_card(
            self.summary, "TOTAL SLOTS", "#2563eb"
        )
        self.occupied_label = self.create_summary_card(
            self.summary, "OCCUPIED", "#dc2626"
        )
        self.available_label = self.create_summary_card(
            self.summary, "AVAILABLE", "#16a34a"
        )

        # Parking slots section
        self.slot_panel = tk.Frame(self.content, bg="white")
        self.slot_panel.pack(fill="x", pady=(0, 18))

        tk.Label(
            self.slot_panel, text="Parking Slot Status",
            bg="white", fg="#1e293b",
            font=("Arial", 14, "bold")
        ).pack(anchor="w", padx=16, pady=(14, 4))

        tk.Label(
            self.slot_panel,
            text="Green: Available     Red: Occupied",
            bg="white", fg="#64748b",
            font=("Arial", 9)
        ).pack(anchor="w", padx=16, pady=(0, 8))

        self.slots_frame = tk.Frame(self.slot_panel, bg="white")
        self.slots_frame.pack(fill="x", padx=10, pady=(0, 12))

        # Parked vehicles section
        self.vehicle_panel = tk.Frame(self.content, bg="white")
        self.vehicle_panel.pack(fill="both", expand=True)

        tk.Label(
            self.vehicle_panel, text="Parked Vehicles",
            bg="white", fg="#1e293b",
            font=("Arial", 14, "bold")
        ).pack(anchor="w", padx=16, pady=(14, 8))

        self.vehicle_list = tk.Listbox(
            self.vehicle_panel, height=6,
            font=("Arial", 10), bd=0,
            highlightthickness=1,
            highlightbackground="#e2e8f0",
            selectbackground="#bfdbfe"
        )
        self.vehicle_list.pack(
            fill="both", expand=True, padx=16, pady=(0, 14)
        )

        self.refresh_dashboard()

    def add_menu_button(self, text, command):
        tk.Button(
            self.sidebar, text=text, command=command,
            anchor="w", padx=18, pady=12,
            bg="#172554", fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat", bd=0,
            font=("Arial", 11), cursor="hand2"
        ).pack(fill="x", padx=10, pady=3)

    def create_summary_card(self, parent, title, color):
        card = tk.Frame(parent, bg="white", height=95)
        card.pack(
            side="left", fill="both", expand=True, padx=5
        )
        card.pack_propagate(False)

        tk.Frame(card, bg=color, height=4).pack(fill="x")

        tk.Label(
            card, text=title,
            bg="white", fg="#64748b",
            font=("Arial", 9, "bold")
        ).pack(anchor="w", padx=13, pady=(10, 1))

        number = tk.Label(
            card, text="0",
            bg="white", fg=color,
            font=("Arial", 23, "bold")
        )
        number.pack(anchor="w", padx=13)
        return number

    def refresh_dashboard(self):
        occupied = 0

        for vehicle in self.parking:
            if vehicle is not None:
                occupied += 1

        available = self.total_slots - occupied

        self.total_label.config(text=str(self.total_slots))
        self.occupied_label.config(text=str(occupied))
        self.available_label.config(text=str(available))

        # Update parking slot cards
        for widget in self.slots_frame.winfo_children():
            widget.destroy()

        for i in range(self.total_slots):
            vehicle = self.parking[i]

            if vehicle is None:
                color = "#16a34a"
                status = "AVAILABLE"
                vehicle_text = "Empty"
            else:
                color = "#dc2626"
                status = "OCCUPIED"
                vehicle_text = vehicle

            card = tk.Frame(
                self.slots_frame, bg="#f8fafc",
                highlightbackground="#e2e8f0",
                highlightthickness=1
            )
            card.grid(
                row=i // 5, column=i % 5,
                padx=5, pady=5, sticky="nsew"
            )

            for column in range(5):
                self.slots_frame.grid_columnconfigure(
                    column, weight=1
                )

            tk.Label(
                card, text="SLOT " + str(i + 1),
                bg="#f8fafc", fg="#1e293b",
                font=("Arial", 10, "bold")
            ).pack(pady=(9, 3))

            tk.Label(
                card, text=status,
                bg="#f8fafc", fg=color,
                font=("Arial", 9, "bold")
            ).pack(pady=2)

            tk.Label(
                card, text=vehicle_text,
                bg="#f8fafc", fg="#64748b",
                font=("Arial", 9)
            ).pack(pady=(2, 9))

        # Update vehicle list
        self.vehicle_list.delete(0, tk.END)

        for i in range(self.total_slots):
            if self.parking[i] is not None:
                self.vehicle_list.insert(
                    tk.END,
                    "Slot " + str(i + 1) + "  |  " + self.parking[i]
                )

    def park_vehicle(self):
        vehicle = simpledialog.askstring(
            "Park Vehicle", "Enter vehicle number:",
            parent=self.root
        )

        if vehicle is None:
            return

        vehicle = vehicle.strip().upper()

        if vehicle == "":
            messagebox.showwarning(
                "Invalid Input", "Enter a vehicle number."
            )
            return

        if vehicle in self.parking:
            messagebox.showwarning(
                "Duplicate", "This vehicle is already parked."
            )
            return

        for i in range(self.total_slots):
            if self.parking[i] is None:
                self.parking[i] = vehicle
                self.refresh_dashboard()

                messagebox.showinfo(
                    "Success",
                    "Vehicle parked in Slot " + str(i + 1) + "."
                )
                return

        messagebox.showwarning(
            "Parking Full", "All parking slots are occupied."
        )

    def remove_vehicle(self):
        vehicle = simpledialog.askstring(
            "Remove Vehicle", "Enter vehicle number to remove:",
            parent=self.root
        )

        if vehicle is None:
            return

        vehicle = vehicle.strip().upper()

        if vehicle in self.parking:
            position = self.parking.index(vehicle)
            self.parking[position] = None
            self.refresh_dashboard()

            messagebox.showinfo(
                "Success",
                "Vehicle removed. Slot " + str(position + 1) + " is free."
            )
        else:
            messagebox.showerror(
                "Not Found", "Vehicle was not found."
            )

    def search_vehicle(self):
        vehicle = simpledialog.askstring(
            "Search Vehicle", "Enter vehicle number to search:",
            parent=self.root
        )

        if vehicle is None:
            return

        vehicle = vehicle.strip().upper()

        if vehicle in self.parking:
            position = self.parking.index(vehicle)

            messagebox.showinfo(
                "Vehicle Found",
                "Vehicle: " + vehicle +
                "\nParking Slot: " + str(position + 1)
            )
        else:
            messagebox.showerror(
                "Not Found", "Vehicle was not found."
            )

    def update_vehicle(self):
        old_vehicle = simpledialog.askstring(
            "Update Vehicle", "Enter current vehicle number:",
            parent=self.root
        )

        if old_vehicle is None:
            return

        old_vehicle = old_vehicle.strip().upper()

        if old_vehicle not in self.parking:
            messagebox.showerror(
                "Not Found", "Current vehicle was not found."
            )
            return

        new_vehicle = simpledialog.askstring(
            "Update Vehicle", "Enter new vehicle number:",
            parent=self.root
        )

        if new_vehicle is None:
            return

        new_vehicle = new_vehicle.strip().upper()

        if new_vehicle == "":
            messagebox.showwarning(
                "Invalid Input", "Enter a vehicle number."
            )
            return

        if new_vehicle in self.parking:
            messagebox.showwarning(
                "Duplicate", "That vehicle is already parked."
            )
            return

        position = self.parking.index(old_vehicle)
        self.parking[position] = new_vehicle
        self.refresh_dashboard()

        messagebox.showinfo(
            "Success", "Vehicle information updated."
        )

    def show_statistics(self):
        occupied = 0

        for vehicle in self.parking:
            if vehicle is not None:
                occupied += 1

        available = self.total_slots - occupied

        # Matplotlib bar chart
        plt.figure(figsize=(7, 5))

        bars = plt.bar(
            ["Occupied", "Available"],
            [occupied, available],
            color=["#dc2626", "#16a34a"]
        )

        plt.title("Parking Slot Statistics")
        plt.xlabel("Slot Status")
        plt.ylabel("Number of Slots")
        plt.ylim(0, self.total_slots + 2)
        plt.bar_label(bars)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = ParkingManagement(root)
    root.mainloop()
