# Ticket Allocation System

## Installation

Follow these steps to set up the Ticket Management System project on your local machine.

### Prerequisites

- [Python](https://www.python.org/) (version 3.6 or higher)
- [pip](https://pip.pypa.io/en/stable/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)
- [PostgreSQL](https://www.postgresql.org/) (installed and running)

### Steps

1. **Clone the Repository:**

   ```bash
   git clone [https://github.com/shilpacvenugopal/ticket_allocation.git]
   cd ticket_allocation
   ```

2. **Create a Virtual Environment:**

   ```bash
   virtualenv venv
   ```

3. **Activate the Virtual Environment:**

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure Database:**

   - Change the database settings in `settings.py` file according to your PostgreSQL configuration.

6. **Run Migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Create Superuser (Admin User):**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create an admin user.

8. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   The project will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

9. **Task 1: CRUD Operations**

   - **Retrieve All Tickets:**
     - Method: GET
     - URL:
       ```bash
       http://127.0.0.1:8000/tickets/ticket/
       ```

   - **Create a Ticket:**
     - Method: POST
     - Request Body: ticket_number, description, resolution_end_date
     - URL:
       ```bash
       http://127.0.0.1:8000/tickets/ticket/
       ```

   - **Update a Ticket:**
     - Method: PUT
     - Request Body: ticket_number, description, resolution_end_date
     - URL:
       ```bash
       http://127.0.0.1:8000/tickets/ticket/<id>/
       ```

   - **Delete a Ticket:**
     - Method: DELETE
     - URL:
       ```bash
       http://127.0.0.1:8000/tickets/ticket/<id>/
       ```

10. **Task 2: Ticket Allocation to Employee**

    Ticket allocation to an employee will take place using the following URL:
    - Method: POST
    - Request Body: ticket_number, description, resolution_end_date
    - URL:
      ```bash
      http://127.0.0.1:8000/tickets/ticket/
      ```

11. **Access the Dashboard Interface:**

    - Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with the admin credentials created in step 7.
    - Visit [http://127.0.0.1:8000/tickets/dashboard/](http://127.0.0.1:8000/tickets/dashboard/)
    - Visit [http://127.0.0.1:8000/tickets/dashboard/?date=<date>](http://127.0.0.1:8000/tickets/dashboard/?date=<date>) to get the dashboard view of a particular date.


## Technology Stack

- **Backend:** Python – Django
- **Frontend:** Django Templates
- **Database:** PostgreSQL

Make sure to replace `<id>` in the URLs with the actual ticket ID when performing CRUD operations. Make sure to replace `<date>` in the URLs with the date eg:2024-03-07 when performing url of the dashboard operations. Also, ensure to provide valid data in the request bodies where necessary.
