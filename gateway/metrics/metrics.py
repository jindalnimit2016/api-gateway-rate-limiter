class MetricsCollector:
    def __init__(self):
        self.allowed = 0
        self.blocked = 0

    def record_allowed(self):
        self.allowed += 1

    def record_blocked(self):
        self.blocked += 1
