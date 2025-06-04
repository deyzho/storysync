cat <<EOL > src/core/feedback.py
import json
import os

class FeedbackManager:
    def __init__(self, storage_path="feedback.json"):
        self.storage_path = storage_path
        self.feedback_data = self.load_feedback()

    def load_feedback(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        return []

    def store_feedback(self, user_id, action, feedback):
        entry = {"user_id": user_id, "action": action, "feedback": feedback}
        self.feedback_data.append(entry)
        with open(self.storage_path, 'w') as f:
            json.dump(self.feedback_data, f)
EOL