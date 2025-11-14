import os

# Bind to 0.0.0.0 and use PORT from environment or default to 10000
bind = f"0.0.0.0:{os.getenv('PORT', '10000')}"

# Worker configuration
workers = 2
worker_class = "sync"
worker_connections = 1000
timeout = 120
keepalive = 5

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

