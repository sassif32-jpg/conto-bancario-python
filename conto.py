class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0):
        self.titolare = titolare
        self.saldo = float(saldo_iniziale)

    def deposita(self, importo):
        """Deposita un importo sul conto corrente."""
        if importo <= 0:
            raise ValueError("L'importo deve essere positivo")
        self.saldo += importo
        return self.saldo

    def preleva(self, importo):
        """Preleva un importo applicando una commissione di 2 euro."""
        if importo <= 0:
            raise ValueError("L'importo deve essere positivo")

        costo_totale = importo + 2  # Importo richiesto + commissione bancaria

        if costo_totale > self.saldo:
            raise ValueError("Fondi insufficienti per coprire prelievo e commissione.")

        self.saldo -= costo_totale
        return self.saldo

    def accredita_interessi(self, tasso_percentuale):
        """Calcola e accredita gli interessi in percentuale (es. 2.5 per il 2.5%)."""
        if tasso_percentuale < 0:
            raise ValueError("Il tasso di interesse non può essere negativo")

        interessi = self.saldo * (tasso_percentuale / 100)
        self.saldo = round(self.saldo + interessi, 2)
        return self.saldo

    def bonifico(self, destinatario, importo):
        """Trasferisce denaro da questo conto ad un altro oggetto ContoBancario."""
        self.preleva(importo)
        destinatario.deposita(importo)