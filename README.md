# using-ai-explorer
some ai-generated codes to use for adding pictures to ask ai for answer and other trivial things


# Auto Screenshot AI (Ollama Local)

Use Python to capture a specific area of the screen and automatically query a locally running Ollama multimodal model (e.g., Gemma 4, LLaVA, Llama 3.2-Vision) for image analysis and Q&A.  
**Fully offline, free, and privacy‑protecting.**

## ✨ Features

- Multiple screenshot regions: right half, left half, full screen, custom rectangle
- Configurable prompt, model, delay
- Save AI answers to a file
- Command‑line arguments and JSON config file support
- Manual control for next capture (press Enter)

## 🖥️ Requirements

- Windows / macOS / Linux
- Python 3.8+
- [Ollama](https://ollama.com) installed and running
- At least 4GB RAM (8GB+ recommended, NVIDIA GPU optional but beneficial)

## 📦 Installation & Setup

### 1. Install Ollama and pull the model

```bash
# Install Ollama from https://ollama.com
# Then pull the Gemma 4 31B cloud model (or any vision‑capable model of your choice)
ollama pull gemma4:31b-cloud
```

> **Note**: You can also use other multimodal models like `llava`, `llama3.2-vision`, etc. Just change the model name in `config.json`.

### 2. Clone this repository

```bash
git clone https://github.com/levelsslevel/using-ai-explorer.git
cd using-ai-explorer
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Prepare `config.json`

Create a `config.json` file in the project folder. Example:

```json
{
    "model": "gemma4:31b-cloud",
    "prompt": "Please describe the main content of this screenshot.",
    "region": "right_half",
    "delay": 1.0,
    "output_file": "answers.txt"
}
```

- `region` can be: `right_half`, `left_half`, `full`, `custom`
- `custom_region` (only needed if `region` is `custom`): `[x, y, width, height]`
- `output_file` is optional; omit it to not save answers.

### Run the program

```bash
python screenshot_general_use_ai.py
```

Press `Enter` to take a screenshot. After each answer, press `Enter` again to continue.

### Optional: use a different config file

```bash
python screenshot_general_use_ai.py --config my_config.json
```

## 📁 File descriptions

- `screenshot_general_use_ai.py` – main program
- `config.json` – configuration file (must exist)
- `requirements.txt` – Python dependencies
- `answers.txt` – saved AI answers (if configured)
- `temp_screenshot.png` – temporary screenshot (auto‑generated)

## ❓ FAQ

**Q: `config.json` not found?**  
A: Make sure the file exists in the same directory as the script, and that it contains valid JSON.

**Q: Model responses are slow?**  
A: The first run loads the model into memory, which may take a while. Subsequent runs are faster.

**Q: How to exit the program?**  
A: Press `Ctrl + C`.

## 📄 License

MIT License

## 🙏 Acknowledgements

- [Ollama](https://ollama.com) – making local LLMs easy
- [pyautogui](https://pyautogui.readthedocs.io/) – simple screenshot library
```
