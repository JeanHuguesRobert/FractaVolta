# FractaVolta — Simulateur Streamlit de buffers mobiles

Prototype exploratoire comparant un hub fixe et des buffers/conteneurs mobiles.

## Architecture
- `fractasim/model.py` : moteur de simulation indépendant de l'UI.
- `fractasim/data.py` : données synthétiques.
- `app.py` : interface Streamlit + Plotly.

## Lancer
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Le moteur est séparé de Streamlit pour rester réutilisable par Serra, une API ou des tests.
