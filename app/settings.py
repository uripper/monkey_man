```python
import os

class Settings:
    def __init__(self):
        self.model_name = os.getenv('MODEL_NAME', 'rockerBOO/stablelm-tuned-alpha-3b-16bit')
        self.port = int(os.getenv('PORT', '8000'))
        self.host = os.getenv('HOST', 'localhost')

    def update_model(self, new_model_name):
        self.model_name = new_model_name

    def update_port(self, new_port):
        self.port = new_port

    def update_host(self, new_host):
        self.host = new_host

settings = Settings()
```