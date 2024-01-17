
## Integration of Python with MySQL Database for Employee Management

### Overview:

I have seamlessly integrated Python with a MySQL database to create a robust Employee Management application. This application employs the Kivy framework for building an intuitive graphical user interface (GUI) that facilitates various employee-related actions.
![Screenshot 2024-01-11 155032](https://github.com/yashjagdale0207/Employee_Management_App_Python/assets/145290827/870da831-7499-4077-94c3-220e239dc130)


### Key Features and Components:

1. **Database Connection:**
   - Incorporated the `mysql.connector` library to establish a secure and efficient connection with the MySQL database.
   - Connected to a specific database named 'abcltd' residing on the local machine.
   - Utilized the credentials 'root' as the username and 'Yash@789' as the password for authentication.

2. **Kivy App Class - `EmployeeApp`:**
   - Defined a comprehensive Kivy application class to encapsulate the entire application logic.
   - Structured the GUI using the BoxLayout to organize key buttons for essential actions.

3. **Graphical User Interface (GUI) Layout:**
   - Implemented a clean and user-friendly interface with buttons for the following actions:
     - Adding an employee
     - Editing employee details
     - Deleting an employee
     - Displaying all employees
     - Searching by name or ID
     - Gracefully shutting down the app

4. **Popup Windows for Enhanced Interactivity:**
   - Employed Kivy's Popup class to create interactive and context-specific pop-up windows for actions such as:
     - Adding a new employee with detailed information input
     - Editing employee details with pre-filled input fields
     - Deleting an employee by providing options for ID or Name
     - Displaying a table of all employees in a scrollable view
     - Searching employees based on name or ID with search result pop-ups

5. **Database Operations:**
   - Developed functions to seamlessly perform essential database operations:
     - Adding a new employee with relevant details
     - Editing existing employee information with optional fields
     - Deleting an employee based on ID or Name
     - Displaying a comprehensive table of all employees
     - Searching for employees by name or ID

6. **Table Display for Employee Information:**
   - Implemented a dynamic table display using Kivy's GridLayout and ScrollView to present employee data in an organized and easily readable format.
   - Ensured proper column headers for clarity.

7. **Error Handling Mechanism:**
   - Incorporated robust error-handling mechanisms for MySQL database operations to gracefully manage and display error messages in case of any issues.

8. **GitHub Integration:**
   - Pushed the code to a GitHub repository, maintaining security by excluding sensitive information such as database credentials through the use of a `.gitignore` file.
   - Encouraged collaboration and contributions by following standard GitHub practices.

### Instructions for Use:


### Instructions for Use:

1. **Setting up the MySQL Database:**
   - Establish a MySQL database named 'abcltd'.
   - Utilize the provided credentials (`root` as the username and `Yash@789` as the password) for establishing a database connection.

2. **Installation and Dependencies:**
   - Install the required libraries using the command: `pip install mysql-connector-python kivy`.

3. **Running the Application:**
   - Execute the Python script to launch the application.
   - The GUI will be presented with intuitive options for effective employee management

4. **Running the Application:**
   - Execute the Python script (`employee_management.py`) to launch the application.
   - The GUI will appear with a set of intuitive buttons, each corresponding to a specific employee management action.

5. **Adding a New Employee:**
   - Click on the "Add Employee" button.
   - A pop-up window will prompt you to input the employee's details such as name, position, salary, address, email, and date of birth.
   - Click the "Save" button to add the new employee to the database.

6. **Editing Employee Details:**
   - Click on the "Edit Employee" button.
   - Enter the employee ID to retrieve existing information.
   - Modify the desired fields (name, position, salary, address, email, date of birth).
   - Click the "Save" button to update the employee details in the database.

7. **Deleting an Employee:**
   - Click on the "Delete Employee" button.
   - Choose the deletion option: either by entering the employee ID or the employee name.
   - Follow the prompts in the pop-up windows to confirm and execute the deletion.

8. **Displaying All Employees:**
   - Click on the "Show All Employees" button.
   - A pop-up window will display a comprehensive table with details of all employees.
   - Scroll through the table to view all entries.

9. **Searching by Name or ID:**
   - Click on the "Search by Name or ID" button.
   - Choose the search option: either by name or ID.
   - Enter the relevant information in the pop-up window.
   - View the search results in a new pop-up window.

10. **Shutdown Application:**
   - Click on the "Shutdown App" button to gracefully exit the application.

11. **Note on Security:**
    - Ensure that sensitive information, such as database credentials, is handled securely.
    - Do not expose confidential details in the source code or public repositories.

12. **Enhancements and Contributions:**
    - This application is open to contributions and enhancements.
    - If you have suggestions or encounter any issues, feel free to contribute or open an issue.

Explore the functionality of the Employee Management application by interacting with the GUI. This guide provides a comprehensive overview of the available actions and how to navigate through the application's features.
