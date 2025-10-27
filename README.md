### ☐ CareAI Assistant

### ☐ Tech Stack
- **Frontend**: Next.js 16, React.js, TailwindCSS, Framer Motion, TypeScript
- **Backend**: Python 3.11+, FastAPI, LangChain, RAG, Hugging Face (LLMs)
- **Database**: Pinecone Vector
- **Tools/Version**: Git, MCP

### ☐ Project Workflow

### ☐ Vector DB

### ☐ Project Structure
``` Java
CareAI/
├── app/                             
│   ├── components/                
│   │   └── ...tsx
│   ├── styles/                     
│   │   └── ...css
│   ├── utils/                      
│   │   └── ...ts
│   ├── layout.tsx                   
│   └── page.tsx            
├── public/
├── data/                            
│   └── ...pdf                   
├── server/
│   ├── model/
│   │   └── ...ipynb                 
│   ├── src/
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── ...py
│   │   ├── utils/
│   │   │   └── ...py
│   │   ├── __init__.py
│   │   ├── db_handler.py
│   │   ├── embedding_handler.py
│   │   ├── gpt_handler.py
│   │   ├── prompt_handler.py
│   │   └── text_handler.py
│   ├── main.py
│   ├── requirements.txt
│   ├── setup.py
│   └── template.sh           
├── .gitignore
├── package.json
├── eslint.config.mjs
├── next.config.js
├── tailwind.config.js
└── README.md
```


### ☐ Installation
#### 1. Clone the repository
```bash
git clone https://github.com/harshkunz/careAI.git
cd Job-Finder
```

#### 2. Frontend setup (Next.js 16)
```bash
cd app
npm install       # Install Dependencies
npm run dev       # Run Server
```
Run at http://localhost:3000

#### 3. Backend setup (FastAPI)
```bash
cd ../server
python -m venv venv         # Create virtual environment
source venv/bin/activate     # Linux/macOS
# OR
venv\Scripts\activate        # Windows

pip install -r requirements.txt  # Install Dependencies
uvicorn main:app --reload        # Run Server
```
Run at http://localhost:8000

#### 4. Environment Variables
.env file in server:
```bash
HF_API_KEY = "your_huggingface_api_key"
PINECONE_API_KEY ="your_pinecone_api_key"
```

### ☐ Contributing
Open to contributions!
- Fork the repository  
- Create a new branch (`git checkout -b feature-name`)  
- Commit your changes (`git commit -m 'Add feature'`)  
- Push to the branch (`git push origin feature-name`)  
- Create a Pull Request
