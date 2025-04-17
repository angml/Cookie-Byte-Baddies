# 🍪 CookieByte — Cafe Management System

Welcome to **CookieByte**, a full-stack cafe management platform designed for tracking inventory, sales, employee management, costs, and more using a microservices architecture with Docker, MySQL, Flask, and Streamlit.

Our team members and Github Usernames: 
1. Angelia Loo (angml)
2. Mahika Sharma (mahikasharma)
3. Amy Baez (amyb25)
4. Riyana Roy (riyanaro / Riyana)
5. Emily Inga (emilycs26)

## Tech Stack

- **Frontend:** Streamlit (Python)
- **Backend:** Flask (REST APIs)
- **Database:** MySQL (via Docker)
- **Containerization:** Docker & Docker Compose

---

## Getting Started

To run this project on your local machine, follow the steps below:

### 1. Clone the Repository

git clone https://github.com/your-username/cookiebyte-baddies.git
cd cookiebyte-baddies

### 2. Add Secrets and Environment Files

SECRET_KEY=someCrazyS3cR3T!Key.!

DB_USER=root

DB_HOST=db

DB_PORT=3306

DB_NAME=CookieByte

MYSQL_ROOT_PASSWORD=<put a good password here>

### 3. Start the Containers

Use Docker Compose to build and run all services:

docker-compose up app -d

docker-compose up api -d

docker-compose up db -d 

This will spin up:

web-app: Streamlit UI at http://localhost:8501

web-api: Flask backend at http://localhost:4000

mysql_db: MySQL server at port 3306

### 4. Load the Database

Once the MySQL container is up, load the schema and sample data:

-- Run these inside the MySQL client or DataGrip

source CookieByte-database.sql;

source CookieByte-data.sql;


