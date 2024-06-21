from ttkthemes import ThemedTk  # Allows usage of themed Tkinter windows
import tkinter as tk  # Standard Tkinter module for GUI elements
from tkinter import ttk, messagebox  # Tkinter's themed widgets and standard message box dialogs
import data  # Import the data module to load YouBike data (assumed to be defined elsewhere)

# Define a class that inherits from ThemedTk
class Window(ThemedTk):
    # Initialize the class
    def __init__(self, theme: str = 'arc', **kwargs):
        super().__init__(theme=theme, **kwargs)  # Initialize the parent class with the specified theme
        self.title('台北市YouBike2.0及時資料')  # Set the window title
        try:
            self.__data = data.load_data()  # Load the YouBike data
        except Exception as e:
            messagebox.showwarning(title='警告', message=str(e))  # Show warning message if data loading fails
        
        self._display_interface()  # Call method to display the interface

    @property
    def data(self) -> list[dict]:
        return self.__data  # Property to access the data

    # Method to display the interface
    def _display_interface(self):
        # Main frame configuration
        mainFrame = ttk.Frame(borderwidth=1, relief='groove')
        ttk.Label(mainFrame, text="台北市YouBike2.0及時資料", font=('arial', 25)).pack(pady=(20, 10))
        
        # Table frame configuration
        tableFrame = ttk.Frame(mainFrame)
        columns = ('sna', 'sarea', 'mday', 'ar', 'total', 'rent_bikes', 'retuen_bikes')
        tree = ttk.Treeview(tableFrame, columns=columns, show='headings')
        
        # Define headings
        tree.heading('sna', text='站點')
        tree.heading('sarea', text='行政區')
        tree.heading('mday', text='時間')
        tree.heading('ar', text='地址')
        tree.heading('total', text='總數')
        tree.heading('rent_bikes', text='可借')
        tree.heading('retuen_bikes', text='可還')

        # Define column widths
        tree.column('sarea', width=70, anchor=tk.CENTER)
        tree.column('mday', width=120, anchor=tk.CENTER)
        tree.column('ar', minwidth=100)
        tree.column('total', width=50, anchor=tk.CENTER)
        tree.column('rent_bikes', width=50, anchor=tk.CENTER)
        tree.column('retuen_bikes', width=50, anchor=tk.CENTER)

        # Bind user events
        tree.bind('<<TreeviewSelect>>', self.item_selected)
        
        # Add data to the treeview
        for site in self.data:
            tree.insert('', tk.END,
                        values=(site['sna'], site['sarea'], site['mday'], site['ar'], site['total'], site['rent_bikes'], site['retuen_bikes']))
        
        tree.grid(row=0, column=0, sticky='nsew')

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(tableFrame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        tableFrame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Pack the main frame
        mainFrame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Method to handle item selection
    def item_selected(self, event):
        tree = event.widget
        print(isinstance(tree, ttk.Treeview))  # Print if the widget is a Treeview instance
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record: list = item['values']
            print(record[0])  # Print the first value of the selected record

# Main function to create and run the window
def main():
    window = Window(theme='breeze')  # Create an instance of the Window class with the 'breeze' theme
    window.mainloop()  # Start the Tkinter main loop

# Entry point check
if __name__ == '__main__':
    main()  # Run the main function if the script is executed directly
