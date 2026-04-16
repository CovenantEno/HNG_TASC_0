# HNG_Task_0

## Description
This is a Django-based API that classifies a given name using an external API and returns structured data.

## Features
- Accepts a name as a query parameter
- Calls external API (Genderize)
- Returns:
  - Gender
  - Probability
  - Count
- JSON response format

## Project Structure
HNG_Task1/
├── api/
├── HNG_Task1/
├── manage.py

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/your-repo.git

2. Navigate into the project:
cd HNG_Task1

3. Create virtual environment:
python -m venv env

4. Activate environment:
env\Scripts\activate

5. Install dependencies:
pip install django requests

## Run Server
python manage.py runserver

## 🔗 API Endpoint
http://127.0.0.1:8000/api/classify?name=John

## Tech Stack
- Python
- Django
