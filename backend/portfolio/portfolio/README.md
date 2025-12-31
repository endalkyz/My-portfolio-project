# The repository url: 
https://github.com/endalkyz/My-portfolio-project.git
cd My-portfolio-project

To access the repository address from local using Git Bash:
cd c/user/enda/My-portfolio-project/backend/portfolio

# future changes, you can do:
git add .
git commit -m "Describe your change"
git push
----------------
## **How to Run Locally**
Clone the repository:
git clone https://github.com/endalkyz/My-portfolio-project.git

# Create and activate a virtual environment:
python -m venv venv
# Windows
# activate a virtual environment:
venv\Scripts\activate


The clear roadmap which tool comes first, second, third… step-by-step.

✅ THE CORRECT ORDER FOR YOUR PROJECT (Django Portfolio)
From Development → CI/CD → Monitoring → Deployment
1️⃣ Finish Your Project (You already finished this 👍)

Technologies used:

Django

Python

PostgreSQL

HTML, CSS, JS
✔ Your project is ready.

2️⃣ Push the Project to GitHub (You already did this 👍)

GitHub will be the source code repository.

3️⃣ Containerize Your Application using Docker

This is the next required step before using Jenkins, Prometheus, Grafana, or Render.

Why Docker first?

Docker makes your app portable.

Render can run Docker apps.

Jenkins CI/CD works best with Docker builds.

Monitoring tools work better when apps are in containers.

So the next step:
👉 Create Dockerfile
👉 Create docker-compose.yml
👉 Test container locally

4️⃣ Configure CI/CD using Jenkins (Optional but recommended)

Once Docker is ready:

Jenkins pipeline will:

Pull your code from GitHub

Build your Docker image

Run tests

Push the image to Docker Hub (optional)

Deploy it automatically to Render (or another server)

If you do not need automation → you can skip Jenkins.

5️⃣ Monitoring using Prometheus + Grafana (Optional)

Only add monitoring when:

You run a backend API

You expect many users

You want to track application metrics

Monitoring order:

Install Prometheus

Expose Django metrics (via django-prometheus)

Connect Prometheus to Grafana

Build dashboards

For a simple portfolio website, monitoring is optional.

6️⃣ Deploy to Render.com (Easiest for you)

Once Docker or code is ready:

You choose ONE of these two deployment options:

Option A — Deploy normal Django code (simpler)

No Docker needed
No Jenkins needed
Just deploy using render.yaml
✔ Fastest
✔ Best for your portfolio

OR

Option B — Deploy Docker container

If you want: Docker + Jenkins + monitoring
This is more DevOps-professional
✔ Good for learning DevOps

📌 So Here is Your Final Roadmap in Order
✅ FOR SIMPLE DEPLOYMENT (recommended for now):

GitHub → (already done)

Prepare Django for production

Add requirements.txt

Add render.yaml

Deploy to Render.com

Done 🎉

🔥 FOR FULL DEVOPS WORKFLOW (if you want advanced setup):

GitHub

Dockerize Django project

Test Docker container locally

Setup Jenkins pipeline

Configure CI/CD (GitHub → Jenkins → Render)

Setup Prometheus + Grafana

Deploy Docker container to Render

Full monitoring + automation 🎉

# Update docker
docker-compose down
docker-compose build
docker-compose up -d