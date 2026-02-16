# Día 09: Dictionaries and Blind auction

## Objetivos del día
- Learn about dictionaries
- Build a blind auction code

## ¿Qué se implementó?
Code for blind auction. Bidders input their name and bid, then confirm if there are more bidders
It clears console log so there's no cheating
At the end, it shows who won

## Conceptos clave
- Clear console: using import os and pycharm run settings (Emulate terminal in output console)
- Dictionaries: Contains key and value pairs. Format: {key: value, key2: value2}
- Nesting: Combination of different data types inside each other. Used to nest list and dictionaries and many more

## Archivos del proyecto
- `Dictionaries.py`: challenge for learning the use of dictionaries
- `blind-auction.py`: main project
- `art.py` : Ascii logo made for the program

## Cómo ejecutar
```bash
# Activar entorno virtual
source .venv/bin/activate  # macOS/Linux
# o
.venv\Scripts\activate  # Windows

# Ejecutar el programa
python main.py
```

## Problemas encontrados y soluciones
- **Problema 1**: clear console not working
  - *Solución*: access to the run config of the code and enabling "Emulate terminal in output console"

    
## Notas personales
.items(), .value() are useful in the for-in loop for dictionaries
