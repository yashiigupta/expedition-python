# Expedition Backend

## Features
- **User & Seller Authentication:** Secure signup and signin using JWT.
- **Ticket Management:** Create, update, and delete available tickets.
- **Purchase Tickets:** Users can buy tickets, reducing available quantities.
- **User Profile Management:** Update and delete user profiles.
- **Secure Password Handling:** Passwords hashed using bcrypt.

## API Endpoints

### Authentication

#### Signup for user
- **Endpoint:** `POST /auth/signup/user`
- **Description:** Register a new user.
- **Request Body:**
  ```json
  {
    "first_name": "John",
    "last_name": "Doe", 
    "email": "john@example.com",
    "password": "password123"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Signup successful"
  }
  ```

#### Signup for seller
- **Endpoint:** `POST /auth/signup/seller`
- **Description:** Register a new seller.
- **Request Body:**
  ```json
  {
    "first_name": "Jane",
    "last_name": "Smith", 
    "email": "jane@example.com",
    "password": "password123",
    "phone": 8546433424,
    "works_at": "bookMyHotel",
    "position": "ticket seller",
    "line1": "12/53, Sun Apartments",
    "line2": "Civil Lines",
    "district": "Sonipat",
    "state": "Haryana",
    "pincode": 131041
  }
  ```
- **Response:**
  ```json
  {
    "message": "Signup successful"
  }
  ```

#### Signin for user
- **Endpoint:** `POST /auth/signin/user`
- **Description:** Authenticate a user and receive a JWT.
- **Request Body:**
  ```json
  {
    "email": "john@example.com",
    "password": "password123"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Signin successful",
    "token": "your-jwt-token"
  }
  ```

#### Signin for seller
- **Endpoint:** `POST /auth/signin/seller`
- **Description:** Authenticate a seller and receive a JWT.
- **Request Body:**
  ```json
  {
    "email": "jane@example.com",
    "password": "password123"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Signin successful",
    "token": "your-jwt-token"
  }
  ```

### Available Tickets

#### Create Ticket
- **Endpoint:** `POST /available-tickets`
- **Description:** Create a new available ticket (Seller only).
- **Headers:**
  ```
  Authorization: Bearer your-jwt-token
  ```
- **Request Body:**
  ```json
  {
    "title": "Rock Concert",
    "type": "Music",
    "place": "Stadium",
    "show_name": "Rock Fest 2024",
    "description": "Annual rock festival",
    "seller": "seller-id",
    "time": "19:00",
    "date": "2024-05-20",
    "available": true,
    "noOfTickets": 100
  }
  ```
- **Response:**
  ```json
  {
    "message": "Ticket created successfully",
    "ticket": { /* ticket details */ }
  }
  ```

#### Update Ticket
- **Endpoint:** `PUT /available-tickets/:id`
- **Description:** Update details of an existing ticket (Seller only).
- **Headers:**
  ```
  Authorization: Bearer your-jwt-token
  ```
- **Request Body:**
  ```json
  {
    "noOfTickets": 99,
    "available": true
  }
  ```
- **Response:**
  ```json
  {
    "message": "Ticket updated successfully",
    "ticket": { /* updated ticket details */ }
  }
  ```

#### Delete Ticket
- **Endpoint:** `DELETE /availableTickets/:id`
- **Description:** Delete a ticket (Seller only).
- **Headers:**
  ```
  Authorization: Bearer your-jwt-token
  ```
- **Response:**
  ```json
  {
    "message": "Ticket deleted successfully."
  }
  ```

#### Get All Tickets
- **Endpoint:** `GET /availableTickets`
- **Description:** Retrieve all tickets.
- **Response:**
  ```json
  {
    "tickets": [ /* array of tickets */ ]
  }
  ```

#### Get Available Tickets
- **Endpoint:** `GET /availableTickets/available`
- **Description:** Retrieve all available tickets.
- **Response:**
  ```json
  {
    "tickets": [ /* array of available tickets */ ]
  }
  ```

#### Get Ticket by ID
- **Endpoint:** `GET /availableTickets/:id`
- **Description:** Retrieve a ticket by its ID.
- **Response:**
  ```json
  {
    "ticket": { /* ticket details */ }
  }
  ```


#### Search Tickets
- **Endpoint:** `GET /api/search`
- **Description:** Search for tickets based on query parameters.
- **Query Parameters:** `?type=Music&place=Stadium`
- **Response:**
  ```json
  {
    "tickets": [ /* array of matching tickets */ ]
  }
  ```

### Tickets Sold

#### Buy Ticket
- **Endpoint:** `POST /tickets/buy/:id`
- **Description:** Purchase a ticket (User only).
- **Headers:**
  ```
  Authorization: Bearer your-jwt-token
  ```
- **Response:**
  ```json
  {
    "message": "Ticket purchased successfully.",
    "ticketId": "generated-ticket-id"
  }
  ```

#### Get Sold Tickets
- **Endpoint:** `GET /ticket-sold/sold`
- **Description:** Retrieve all sold tickets (User only).
- **Headers:**
  ```
  Authorization: Bearer your-jwt-token
  ```
- **Response:**
  ```json
  {
    "soldTickets": [ /* array of sold tickets */ ]
  }
  ```

### User Profile

#### Update Profile
- **Endpoint:** `PUT /profile`
- **Description:** Update user profile information.
- **Headers:**
  ```
  Authorization: Bearer your-jwt-token
  ```
- **Request Body:**
  ```json
  {
    "first_name": "Jane",
    "last_name": "Doe"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Profile updated successfully."
  }
  ```

#### Delete User
- **Endpoint:** `DELETE /user`
- **Description:** Delete user account.
- **Headers:**
  ```
  Authorization: Bearer your-jwt-token
  ```
- **Response:**
  ```json
  {
    "message": "User account deleted successfully."
  }
  ```

#### Get Profile
- **Endpoint:** `GET /profile`
- **Description:** Retrieve user profile information.
- **Headers:**
  ```
  Authorization: Bearer your-jwt-token
  ```
- **Response:**
  ```json
  {
    "user": { /* user profile details */ }
  }
  ```

### Seller Profile

#### Get Profile
- **Endpoint:** `GET /seller/profile`
- **Description:** Retrieve seller profile information.
- **Headers:**
  ```
  Authorization: Bearer your-jwt-token
  ```
- **Response:**
  ```json
  {
    "seller": { /* seller profile details */ }
  }
  ```
