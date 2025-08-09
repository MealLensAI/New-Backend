# CORS Configuration Fix for your app.py
# Replace the existing CORS configuration with this:

# Option 1: Most permissive (for testing)
CORS(
    app,
    origins=["https://meallensai.netlify.app", "http://localhost:5173", "*"],
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
    supports_credentials=False  # Set to False when using "*" in origins
)

# Option 2: More specific (recommended for production)
CORS(
    app,
    origins=["https://meallensai.netlify.app", "http://localhost:5173"],
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
    supports_credentials=True
)

# Option 3: Simplest (if above doesn't work)
CORS(app, origins="*", supports_credentials=False)
