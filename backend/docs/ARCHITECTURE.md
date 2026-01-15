## B2B SAAS - BACKEND


### Stage 0 - Project Structure Setup

- first we create the backend folder and using `uv` library initialise and add some libraries.

```bash
uv init .
uv add fastapi uvicorn sqlalchemy python-dotenv pyjwt clerk svix
```

### Stage 1 - Setup up the envariables inside the `.env` file

- here we will be using clerk for all auth related stuff hence we sign up, create a new application inside the cleck account, and get all the relevant envariables add them to `.env` file.

---

### Stage 2 - Writing the code

##### Step 1

- first write our `config.py` where we configue our env variables.
- after this we write the `database.py` file where we create the database session and engine to lock our database, add some session and bind the engine.
- we then write a function `get_db` which basically yields the database to us. [also check if the database is already created we access it or if not we create one]. we use the `db.close()` method to close safely our database and makes sure everything is saved properly.

##### Step 2

- next we write our `clerk.py` file. here we setup some clerk related stuff in the backend since we're using clerk for all our authentication-related stuff in the frontend.
- Note: we only want authenticated users to be able to access our backend features

##### Step 3 

- setting up some clerk-related stuff to make the authentication to work [did: roles&permissions, billings, and memberships]

---

### Stage 4 - Auth Config

- write to the `auth.py` file: firstly we import all libraries from fastapi and clerk_backend_api.
- essentially, from the frontend -> we want to include the user's clerk account details which include the jwt token (user's identity) which is sent to the backend. basically the frontend sends a request (including the jwt token from clerk) to the backend. 
- the backend authenticates this token, gets the user's details from clerk and check the user's permissions. [if the details are valid]. the ability to do??
- create a `AuthUser` class which basically initialises some organisation's permissions which should be checked during the authentication stage. we also create a function `has_permission` to check if user has a specific permission inside the org list
- add the properties we created on the clerk website 
- write a function to convert FastAPI Request to httpx.Request
- have written four functions which are responsible for dependencies injection

---

### Stage 5 - Database Models

- here we write the file `models/tasks.py` where the class `TaskStatus` basically defines the task status enums and then another class `Task` which inherits from `Base` which essentially defines the table schema for our tasks
- then we move on to `schemas/task.py` to write the data validation for creating, updating, and getting tasks so that we have correct types in our fastAPI application.
- inside the `app/api/tasks.py` file this is where we define our endpoints (routes) for the API for different operations related to our tasks 
    - here specify the router prefix `/api/tasks` 
    - function `list_tasks()` which will depeend on the `require_view()` function which essentially checks if the user is authenticated before returning a response (view the tasks)

