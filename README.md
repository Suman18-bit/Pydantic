<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&height=200&section=header&text=FastAPI%20%2B%20Pydantic&fontSize=46&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=REST%20APIs%20%26%20Data%20Validation&descSize=18&descAlignY=58&color=gradient&customColorList=0D1117,A855F7)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=A855F7&center=true&vCenter=true&width=560&lines=Build+REST+APIs+with+FastAPI;Validate+data+with+Pydantic;Patient+and+student+records%2C+end+to+end)](https://github.com/Suman18-bit)

---

![Python](https://img.shields.io/badge/Python-0D1117?style=for-the-badge&logo=python&logoColor=A855F7)
![FastAPI](https://img.shields.io/badge/FastAPI-0D1117?style=for-the-badge&logo=fastapi&logoColor=A855F7)
![Pydantic](https://img.shields.io/badge/Pydantic-0D1117?style=for-the-badge&logo=pydantic&logoColor=A855F7)
![Uvicorn](https://img.shields.io/badge/Uvicorn-0D1117?style=for-the-badge&logo=uvicorn&logoColor=A855F7)

</div>


## ✨ Overview

A hands-on project for exploring how **FastAPI** and **Pydantic** work together. It pairs a FastAPI application with Pydantic models and sample JSON data for **patient** and **student** records.

- ⚡ **FastAPI app** with automatically generated, interactive API docs
- ✅ **Pydantic models** for patient and student data
- 🗂️ **JSON sample data**, so there's no database to set up
- 🐍 **Reproducible setup**: Python version pinned in `.python-version`, dependencies in `pyproject.toml`

## 🧩 How It Works

```mermaid
flowchart LR
    A([Client]) -->|HTTP request| B["FastAPI app<br/>main.py"]
    B -->|validates with| C["Pydantic models"]
    B <-->|reads / writes| D[("JSON data")]
    B -->|JSON response| A

    classDef purple fill:#1e1033,stroke:#A855F7,color:#F5F3FF,stroke-width:2px;
    class A,B,C,D purple;
```

## 📁 Project Structure

```
FastAPI/
├── FastAPI/
│   └── main.py               # FastAPI application
├── Pydantic/
│   ├── Patients.py           # Patient model
│   ├── Student.py            # Student model
│   ├── pydt.py               # Pydantic examples
│   ├── patients_data.json    # Sample patient data
│   └── students_data.json    # Sample student data
├── Data.json                 # Sample data
├── patients_data.json        # Sample patient data
├── new.md                    # Notes
├── New.mmd.txt               # Mermaid diagram source
├── pyproject.toml            # Project metadata & dependencies
├── .python-version           # Pinned Python version
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python (the version is pinned in `.python-version`)
- `pip`, or [uv](https://docs.astral.sh/uv/)

### Installation

```bash
# Clone the repository
git clone https://github.com/Suman18-bit/<repo-name>.git
cd <repo-name>

# Create a virtual environment
python -m venv .venv
```

Activate it:

```bash
# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install fastapi "uvicorn[standard]" "pydantic[email]"
```

<details>
<summary><b>Prefer uv?</b></summary>

```bash
uv sync
```

</details>

### Run the API

```bash
cd FastAPI
uvicorn main:app --reload
```

Once the server is up, open the interactive docs:

| Docs | URL |
|------|-----|
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |

### Try the Pydantic examples

Each script in `Pydantic/` can be run on its own:

```bash
python Pydantic/Patients.py
python Pydantic/Student.py
```

## 👨‍💻 Author

**Suman Seth**

[![GitHub](https://img.shields.io/badge/GitHub-Suman18--bit-A855F7?style=for-the-badge&logo=github&logoColor=white&labelColor=0D1117)](https://github.com/Suman18-bit)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Suman%20Seth-A855F7?style=for-the-badge&labelColor=0D1117)](https://linkedin.com/in/suman-seth-b05417324)

---

<div align="center">

⭐ If you found this useful, consider starring the repo!

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:A855F7,100:0D1117&height=120&section=footer)

</div>
