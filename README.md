# 🐍 Python & Pytest Starter Template

Un modello pronto all'uso per strutturare un progetto Python con ambiente virtuale, gestione delle dipendenze, test automatici tramite `pytest` e pipeline di CI/CD con **GitHub Actions**.

---

## 🛠️ Requisiti Prerequisiti

* **Python 3.10+** installato nel sistema.
* **Git** configurato locale.
* **VS Code** (consigliato con l'estensione *Python* di Microsoft).

---

## 🚀 Cheatsheet Guida Rapida Passo-Passo

### 1. Struttura Cartelle e File
Creazione dei file sorgente, di test e della configurazione iniziale:

```powershell
# Crea la cartella di progetto ed entra
mkdir mio_progetto
cd mio_progetto

# Crea i file del modulo e dei test
New-Item -Path modulo.py, test_modulo.py -ItemType File