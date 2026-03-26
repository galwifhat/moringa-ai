backend/
│
├── app/
│   ├── __init__.py          # App factory
│   ├── config.py           # Configurations (env vars, API keys)
│   │
│   ├── routes/             # API endpoints (controllers)
│   │   ├── __init__.py
│   │   └── journal_routes.py
│   │
│   ├── services/           # Business logic (OpenRouter, processing)
│   │   ├── __init__.py
│   │   └── openrouter_service.py
│   │
│   ├── models/             # Database models (optional for now)
│   │   ├── __init__.py
│   │   └── journal_model.py
│   │
│   ├── utils/              # Helpers (formatting, validation)
│   │   ├── __init__.py
│   │   └── helpers.py
│
├── .env                    # API keys (DO NOT COMMIT)
├── requirements.txt
├── run.py                  # Entry point
└── README.md

