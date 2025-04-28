# 🚀 DjangoCICD Project

Welcome to the **DjangoCICD** project!  
This project is a minimal Django application designed to demonstrate **Continuous Integration and Continuous Deployment (CI/CD)** using **Jenkins**, **Docker**, and **AWS EC2**.

---

## 📂 Project Structure

DjangoCICD/ ├── manage.py ├── requirements.txt ├── Dockerfile ├── Jenkinsfile └── myproject/ ├── init.py ├── settings.py ├── urls.py └── wsgi.py

yaml
Copy
Edit

---

## 🛠 Tech Stack

- Python 3.12
- Django 4.x
- Django REST Framework
- Gunicorn
- Docker
- Jenkins
- AWS EC2 (Ubuntu 24.04)

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Amitesh220/DjangoCICD.git
cd DjangoCICD
2. Create and Activate a Virtual Environment
bash
Copy
Edit
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Django Development Server
bash
Copy
Edit
python manage.py runserver 0.0.0.0:8000
Access the app at:
👉 http://your-ec2-public-ip:8000

🐳 Docker Instructions 
You can also run this app inside a Docker container:

Build the Docker Image
bash
Copy
Edit
docker build -t djangocicd-app .
Run the Container
bash
Copy
Edit
docker run -d -p 8000:8000 djangocicd-app
🔧 Jenkins CICD Setup
Jenkins is configured using the Jenkinsfile in this repo.
It will automatically:

Pull the latest code from GitHub

Install Python dependencies

Run Django migrations (if any)

Start the server using Gunicorn

🔥 Live Demo
http://54.172.229.65:8000

📜 License
This project is licensed under the MIT License.

🙌 Acknowledgements
Thanks to the Django and Jenkins communities for amazing documentation and support.
Project hosted on AWS EC2.

✨ Made with passion by Amitesh220
