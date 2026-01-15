## B2B SAAS - FRONTEND

### Stage 0 - Project Structure Setup

- first we create the frontend folder and using `npm` library initialise and add some libraries.

```bash
npm create@latest frontend
npm i @clerk/clerk-react react-router-dom
```

---

### Stage 1 - Write our `main.jsx` file

- import the publishable key from Clerk and using the aliases `{ ClerkProvider}` and `{BrowserProvider}` we wrap the function `App()` inside their respective tags

---

### Stage 2 - `App.jsx` file

- this file acts as main routing entry point for the frontend application. It defines which pages exist, their URLs, and which routes require authentication.

This file connects:

-  React Router (navigation)

- Clerk (authentication state)

- Page-level components (Home, Auth, Dashboard, etc.)


- It is the backbone that ties together routing, authentication, and page structure in a clean and maintainable way.