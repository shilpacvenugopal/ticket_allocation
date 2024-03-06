# Ticket Allocation System

## Installation

Follow these steps to set up the Ticket Management System project on your local machine.

### Prerequisites

- [Python](https://www.python.org/) (version 3.6 or higher)
- [pip](https://pip.pypa.io/en/stable/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)

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

5. **Run Migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create Superuser (Admin User):**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create an admin user.

7. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   The project will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

 8. **Task 1**
    Basic CURD Operations
  - Method: (GET)
  - url:
    ```bash
     http://127.0.0.1:8000/tickets/ticket/
    ```

  - Method: (POST)
  - Request Body : ticket_number, description, resolution_end_date
  - url:
    ```bash
     http://127.0.0.1:8000/tickets/ticket/
    ```

  - Method: (PUT)
  - Request Body : ticket_number, description, resolution_end_date
  - url:
    ```bash
     http://127.0.0.1:8000/tickets/ticket/<id>/
    ```
  - Method: (DELETE)
  - url:
    ```bash
     http://127.0.0.1:8000/tickets/ticket/<id>/
    ```

9. **Access the Dashboard Interface:**

   Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with the admin credentials created in step 6.
   Visit [http://127.0.0.1:8000/tickets/dashboard/](http://127.0.0.1:8000/tickets/dashboard/) and log in with the admin credentials created in step 6.

## Technology Stack

- **Backend:** Python – Django
- **Frontend:** Django Templates
- **Database:** PostgreSQL

