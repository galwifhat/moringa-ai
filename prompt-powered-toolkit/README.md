frontend/
├── public/
├── src/
│   ├── api/                     # All API call logic lives here
│   │   ├── axiosClient.js       # Axios instance with base URL + interceptors
│   │   ├── journalApi.js        # Journal-specific API calls
│   │   └── aiApi.js             # AI/OpenRouter-specific API calls
│   │
│   ├── components/              # Reusable, dumb UI components
│   │   ├── ui/                  # Primitives: Button, Input, Modal
│   │   └── journal/             # Domain-specific: JournalCard, EntryForm
│   │
│   ├── pages/                   # Route-level components
│   │   ├── HomePage.jsx
│   │   ├── JournalPage.jsx
│   │   └── SettingsPage.jsx
│   │
│   ├── hooks/                   # Custom React hooks
│   │   ├── useJournal.js        # Data fetching + state for journal
│   │   └── useAIStream.js       # Handles SSE streaming from OpenRouter
│   │
│   ├── context/                 # Global state (Auth, Theme)
│   │   └── AuthContext.jsx
│   │
│   ├── utils/                   # Pure helper functions
│   │   └── formatDate.js
│   │
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
│
├── .env                         # VITE_API_BASE_URL etc.
├── vite.config.js
└── tailwind.config.js


### AI Prompt Plan

#### Phase 1 - Discovery Prompts:

Prompt 1:
"What is an API wrapper? What problems does it solve in AI applications?"

Prompt 2:
"What are the prerequisites for building an AI wrapper for OpenRouter?"

Prompt 3:
"Show me 5 real-world applications that use API wrappers for AI services"

### Phase 2- Setup Prompts:

Prompt 1 (Setup):
"Give me step-by-step instructions to set up a project with:
Backend: Python Flask with OpenRouter API
Frontend: React + Vite + TailwindCSS
Include all installation commands and a requirements.txt file"

Prompt 2 (Structure):
"What's the minimal project structure for a Flask + React app? Show me folder organization."
Prompt 3 (Common Mistakes):
"What common configuration mistakes should I avoid when setting up Flask with CORS for React?"
