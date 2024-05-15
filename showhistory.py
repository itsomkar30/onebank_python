import tkinter as tk
import mysql.connector as sql


def history(user):
    # Connect to the MySQL database
    mydb = sql.connect(
        host="localhost",
        user="root",
        passwd="itsomkar30",
        database="bank"
    )
    cursor = mydb.cursor()

    # Execute SQL query to fetch all rows from the table

    transaction = f"{user}_transaction"
    cursor.execute(f"SELECT * FROM {transaction}")

    # Fetch all rows
    rows = cursor.fetchall()

    # Close the connection
    mydb.close()

    # Display the fetched data in a Tkinter window
    root = tk.Tk()
    root.title(f"{user} Transaction History")

    # Create a frame to hold the table
    table_frame = tk.Frame(root, bd=1, relief=tk.SUNKEN)
    table_frame.pack()

    # Add headers
    headers = ['Timedate', 'Account Number', 'Remarks', 'Amount']
    for i, header in enumerate(headers):
        header_label = tk.Label(table_frame, text=header, relief=tk.RIDGE, width=30)
        header_label.grid(row=0, column=i)

    # Add data rows
    for row_index, row_data in enumerate(rows):
        for col_index, cell_value in enumerate(row_data):
            cell_label = tk.Label(table_frame, text=cell_value, relief=tk.RIDGE, width=30)
            cell_label.grid(row=row_index + 1, column=col_index)

    root.mainloop()

# Call the function to display the table

