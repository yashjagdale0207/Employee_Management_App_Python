import mysql.connector as my
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window



# Connect to MySQL
connection = my.connect(
    host='localhost',
    user='root',
    password='rootpass',
    database='abcltd'
)
cursor = connection.cursor()


class EmployeeApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        add_button = Button(text='Add Employee', on_press=self.add_employee)
        layout.add_widget(add_button)

        edit_button = Button(text='Edit Employee', on_press=self.edit_employee)
        layout.add_widget(edit_button)

        delete_button = Button(text='Delete Employee', on_press=self.delete_employee)
        layout.add_widget(delete_button)

        show_all_button = Button(text='Show All Employees', on_press=self.show_all_employees)
        layout.add_widget(show_all_button)

        search_button = Button(text='Search by Name or ID', on_press=self.search_by_name_or_id)
        layout.add_widget(search_button)

        shutdown_button = Button(text='Shutdown App', on_press=self.stop)
        layout.add_widget(shutdown_button)

        return layout

    def show_popup(self, message, close_button_callback=None):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))

        close_button = Button(text="Close", on_press=lambda x: popup.dismiss())
        if close_button_callback:
            close_button.bind(on_press=close_button_callback)

        content.add_widget(close_button)

        popup = Popup(title='Message', content=content, size_hint=(None, None), size=(400, 200))
        popup.open()

    def add_employee(self, instance):
        # Create a Popup for adding employee information
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text="Enter employee information:"))

        name_input = TextInput(hint_text="Name")
        content.add_widget(name_input)

        position_input = TextInput(hint_text="Position")
        content.add_widget(position_input)

        salary_input = TextInput(hint_text="Salary")
        content.add_widget(salary_input)

        address_input = TextInput(hint_text="Address")
        content.add_widget(address_input)

        email_input = TextInput(hint_text="Email")
        content.add_widget(email_input)

        dob_input = TextInput(hint_text="Date of Birth (YYYY-MM-DD)")
        content.add_widget(dob_input)

        save_button = Button(text="Save", on_press=lambda x: self.save_employee(
            name_input.text, position_input.text, salary_input.text, address_input.text, email_input.text, dob_input.text))
        content.add_widget(save_button)

        back_button = Button(text="Back", on_press=lambda x: popup.dismiss())
        content.add_widget(back_button)

        popup = Popup(title="Add Employee", content=content, size_hint=(None, None), size=(400, 400))
        popup.open()

    def save_edited_employee(self, employee_id, name, position, salary, address, email, dob):
        # Retrieve existing data for the employee
        select_query = "SELECT * FROM employees WHERE id = %s"
        select_data = (employee_id,)

        try:
            cursor.execute(select_query, select_data)
            existing_employee = cursor.fetchone()
        except my.Error as err:
            print(f"Error: {err}")
            return

        # Check if the TextInput fields are blank, if yes, use existing values
        name = name if name else existing_employee[1]
        position = position if position else existing_employee[2]
        salary = salary if salary else existing_employee[3]
        address = address if address else existing_employee[4]
        email = email if email else existing_employee[5]
        dob = dob if dob else existing_employee[6]

        # Update data in the 'employees' table
        update_query = "UPDATE employees SET name=%s, position=%s, salary=%s, address=%s, email=%s, date_of_birth=%s WHERE id=%s"
        data = (name, position, salary, address, email, dob, employee_id)

        try:
            cursor.execute(update_query, data)
            connection.commit()
            print("Employee updated successfully.")
        except my.Error as err:
            print(f"Error: {err}")

        # Close the Popup after saving the edited employee
        App.get_running_app().root_window.children[0].dismiss()

    def edit_employee(self, instance):
        # Create a Popup for editing employee information
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text="Enter employee information to edit:"))

        id_input = TextInput(hint_text="Employee ID")
        content.add_widget(id_input)

        name_input = TextInput(hint_text="Name")
        content.add_widget(name_input)

        position_input = TextInput(hint_text="Position")
        content.add_widget(position_input)

        salary_input = TextInput(hint_text="Salary")
        content.add_widget(salary_input)

        address_input = TextInput(hint_text="Address")
        content.add_widget(address_input)

        email_input = TextInput(hint_text="Email")
        content.add_widget(email_input)

        dob_input = TextInput(hint_text="Date of Birth (YYYY-MM-DD)")
        content.add_widget(dob_input)

        save_button = Button(text="Save", on_press=lambda x: self.save_edited_employee(
            id_input.text, name_input.text, position_input.text, salary_input.text, address_input.text,
            email_input.text, dob_input.text))
        content.add_widget(save_button)

        back_button = Button(text="Back", on_press=lambda x: popup.dismiss())
        content.add_widget(back_button)

        popup = Popup(title="Edit Employee", content=content, size_hint=(None, None), size=(400, 400))
        popup.open()

    def save_edited_employee(self, employee_id, name, position, salary, address, email, dob):
        # Update data in the 'employees' table
        update_query = "UPDATE employees SET name=%s, position=%s, salary=%s, address=%s, email=%s, date_of_birth=%s WHERE id=%s"
        data = (name, position, salary, address, email, dob, employee_id)

        try:
            cursor.execute(update_query, data)
            connection.commit()
            print("Employee updated successfully.")
        except my.Error as err:
            print(f"Error: {err}")

        # Close the Popup after saving the edited employee
        App.get_running_app().root_window.children[0].dismiss()



    def delete_employee(self, instance):
        # Create the main Popup for choosing the delete option
        self.main_popup = Popup(title="Delete Employee", size_hint=(None, None), size=(400, 200))

        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text="Delete by (1) ID or (2) Name:"))

        delete_option_input = TextInput(hint_text="Option")
        content.add_widget(delete_option_input)

        enter_button = Button(text="ENTER", on_press=lambda x: self.on_delete_option_enter(delete_option_input.text))
        content.add_widget(enter_button)

        back_button = Button(text="Back", on_press=lambda x: self.main_popup.dismiss())
        content.add_widget(back_button)

        self.main_popup.content = content
        self.main_popup.open()

    def on_delete_option_enter(self, option):
        option = option.strip()

        if option == "1":
            # If deleting by ID, show input for ID in a new Popup
            self.main_popup.dismiss()  # Close the current Popup
            self.show_delete_input_popup("ID", "Employee ID", "id")
        elif option == "2":
            # If deleting by name, show input for name in a new Popup
            self.main_popup.dismiss()  # Close the current Popup
            self.show_delete_input_popup("Name", "Employee Name", "name")
        else:
            self.show_popup("Invalid option. Please choose 1 or 2.")

    def show_delete_input_popup(self, field_type, hint_text, option):
        # Create a new Popup for entering the delete value (ID or Name)
        delete_popup = Popup(title=f"Delete Employee by {field_type}", size_hint=(None, None), size=(400, 200))

        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=f"Enter {field_type} to delete:"))

        delete_input = TextInput(hint_text=hint_text)
        content.add_widget(delete_input)

        delete_button = Button(text="Delete", on_press=lambda x: self.perform_delete(option, delete_input.text))
        content.add_widget(delete_button)

        back_button = Button(text="Back", on_press=lambda x: delete_popup.dismiss())
        content.add_widget(back_button)

        delete_popup.content = content
        delete_popup.open()

    def perform_delete(self, option, value):
        if option == "id":
            delete_query = "DELETE FROM employees WHERE id = %s"
        elif option == "name":
            delete_query = "DELETE FROM employees WHERE name = %s"
        else:
            self.show_popup("Invalid option. Please choose 1 or 2.")
            return

        try:
            cursor.execute(delete_query, (value,))
            connection.commit()
            print("Employee deleted successfully.")
        except my.Error as err:
            print(f"Error: {err}")

        # Close the Popup after performing the delete
        App.get_running_app().root_window.children[0].dismiss()

    def show_employee_table(self, employees):
        # Create a new BoxLayout as the parent
        content_layout = BoxLayout(orientation='vertical')

        # Create a GridLayout for the table
        grid_layout = GridLayout(cols=7, spacing=7, size_hint_y=None, row_default_height=30)

        # Add column headers
        headers = ["ID","Name", "Position", "Salary", "Address", "Email", "Date of Birth"]
        for header in headers:
            grid_layout.add_widget(Label(text=header, bold=True))

        # Add employee data to the table
        for employee in employees:
            for data in employee:
                grid_layout.add_widget(Label(text=str(data)))

        # Add the GridLayout to the new BoxLayout
        content_layout.add_widget(grid_layout)

        # Create the Back button
        back_button = Button(text="Back", size_hint=(None, None), size=(40, 40),
                             on_press=lambda x: popup.dismiss())
        content_layout.add_widget(back_button)

        # Create a ScrollView for both vertical and horizontal scrolling
        scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=True, do_scroll_y=True)
        scroll_view.add_widget(content_layout)  # Use the new BoxLayout as the child

        # Create the Popup
        popup = Popup(title="All Employees", content=scroll_view, size_hint=(None, None), size=(850,400))
        popup.open()

    def show_all_employees(self, instance):
        # Query to select all employees
        select_all_query = "SELECT * FROM employees"

        try:
            cursor.execute(select_all_query)
            employees = cursor.fetchall()

            if not employees:
                content = Label(text="No employees found.")
            else:
                # Call the new function to display employees in a table format
                self.show_employee_table(employees)

        except my.Error as err:
            print(f"Error: {err}")
            content = Label(text="An error occurred while fetching employee data.")
    def search_by_name_or_id(self, instance):
        # Create a Popup for searching by name or ID
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text="Choose search option:"))

        options_label = Label(text="(1) Search by Name\n(2) Search by ID")
        content.add_widget(options_label)

        option_input = TextInput(hint_text="Option")
        content.add_widget(option_input)

        search_button = Button(text="Search", on_press=lambda x: self.perform_search(option_input.text))
        content.add_widget(search_button)

        back_button = Button(text="Back", on_press=lambda x: popup.dismiss())
        content.add_widget(back_button)

        popup = Popup(title="Search Option", content=content, size_hint=(None, None), size=(400, 400))
        popup.open()

    def perform_search(self, option):
        option = option.strip()

        if option == "1":
            # If searching by name, show input for name in a new Popup
            self.show_search_input_popup("Name", "Employee Name", "name")
        elif option == "2":
            # If searching by ID, show input for ID in a new Popup
            self.show_search_input_popup("ID", "Employee ID", "id")
        else:
            self.show_popup("Invalid option. Please choose 1 or 2.")

    def show_search_input_popup(self, field_type, hint_text, option):
        # Create a new Popup for entering the search value (ID or Name)
        search_popup = Popup(title=f"Search Employee by {field_type}", size_hint=(None, None), size=(400, 200))

        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=f"Enter {field_type} to search:"))

        search_input = TextInput(hint_text=hint_text)
        content.add_widget(search_input)

        search_button = Button(text="Search", on_press=lambda x: self.perform_search_action(option, search_input.text))
        content.add_widget(search_button)

        back_button = Button(text="Back", on_press=lambda x: search_popup.dismiss())
        content.add_widget(back_button)

        search_popup.content = content
        search_popup.open()

    def perform_search_action(self, option, value):
        search_query = "SELECT * FROM employees WHERE {} = %s".format(option)

        try:
            cursor.execute(search_query, (value,))
            employees = cursor.fetchall()

            if not employees:
                self.show_popup(f"No employees found with the {option} '{value}'.")
            else:
                employee_info = "\n".join([f"ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}, Salary: {employee[3]}, Address: {employee[4]}, Email: {employee[5]}, Date of Birth: {employee[6]}" for employee in employees])
                self.show_popup(employee_info)

        except my.Error as err:
            print(f"Error: {err}")
            self.show_popup("An error occurred during the search.")

        



app=EmployeeApp()
app.run()
