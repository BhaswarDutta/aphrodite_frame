# 🪞 Aphrodite Frame

Make your images Instagram-ready **without cropping**.

Aphrodite Frame adds clean white borders so your images fit perfectly into **1:1** and **4:5** ratios while preserving composition.

---

## ✨ Features

- Upload images (PNG, JPG, JPEG)
- Live preview
- 1:1 (Square) and 4:5 (Portrait) support
- No cropping — smart resizing + padding
- Download processed image

---

## 🚀 Demo

[Aphrodite Frame](https://aphrodite-frame.streamlit.app/)

---

## 🛠️ Tech Stack

- Streamlit
- Pillow (PIL)
- Python

---

## ▶️ Run Locally

- Make sure `uv` is installed in your system
- For Linux and MacOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- For Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

- Clone the repo

```bash
git clone --depth 1 https://github.com/BhaswarDutta/aphrodite_frame.git
```

- `cd` into the cloned directory

```bash
cd aphrodite_frame
```

- Use `uv` to add necessary dependencies and run the app

```bash
uv sync
uv run streamlit run main.py
```

- Alternatively you can use the standard way of using the `requirements.txt`
- Though I have tested only the above method on my own machine

```bash
uv pip install -r requirements.txt
source .venv/bin/activate # For POSIX shells like Bash and Zsh
source .venv/bin/activate.fish # For Fish shell, something I use
streamlit run main.py
```

---

## 📜 License

_MIT_
