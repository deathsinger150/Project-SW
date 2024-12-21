from locust import HttpUser, task, between

class ClubPlatformUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def view_dashboard(self):
        self.client.get("/dashboard")

    @task
    def create_club(self):
        self.client.post("/create_club", json={"name": "AI Club"})
