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


## Catégories de transport

Le modèle distingue des **tracteurs légers** pour la collecte locale et des
**tracteurs lourds** pour le transport massifié des buffers/conteneurs.

La capacité de tractage (kg) et la charge énergétique (kWh) sont volontairement
séparées : leur relation dépend de la masse réelle du système batterie,
de la remorque et des équipements. Un Kia PV5 peut être utilisé comme exemple
de tracteur léger, sans définir la catégorie.
