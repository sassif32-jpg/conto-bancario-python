import pytest
from conto import ContoBancario


@pytest.fixture
def conto_base():
    """Fixture che fornisce un conto di test con saldo iniziale di 100 euro."""
    return ContoBancario("Mario Rossi", 100)


@pytest.fixture
def conto_destinatario():
    """Fixture che fornisce un secondo conto vuoto per i test di bonifico."""
    return ContoBancario("Luigi Verdi", 0)


def test_inizializzazione():
    conto = ContoBancario("Test User", 50)
    assert conto.titolare == "Test User"
    assert conto.saldo == 50.0


# Test parametri per depositi validi
@pytest.mark.parametrize(
    "versamento, saldo_atteso",
    [
        (50, 150.0),
        (20.5, 120.5),
        (0.01, 100.01),
    ],
)
def test_deposita_valido(conto_base, versamento, saldo_atteso):
    conto_base.deposita(versamento)
    assert conto_base.saldo == saldo_atteso


# Test parametri per depositi non validi (eccezione attesa)
@pytest.mark.parametrize("versamento_errato", [0, -10, -0.5])
def test_deposita_non_valido(conto_base, versamento_errato):
    with pytest.raises(ValueError, match="L'importo deve essere positivo"):
        conto_base.deposita(versamento_errato)


def test_preleva_con_commissione(conto_base):
    # Saldo iniziale: 100. Prelievo 50 + 2 di commissione = costo 52. Saldo finale: 48
    conto_base.preleva(50)
    assert conto_base.saldo == 48.0


def test_preleva_fondi_insufficienti(conto_base):
    # Tenta di prelevare 99 euro (costo totale 101, superiore a 100)
    with pytest.raises(ValueError, match="Fondi insufficienti"):
        conto_base.preleva(99)


def test_accredita_interessi(conto_base):
    # 100 euro + 5% = 105.0 euro
    conto_base.accredita_interessi(5)
    assert conto_base.saldo == 105.0


def test_bonifico_successo(conto_base, conto_destinatario):
    # Mittente ha 100, invia 40 (costo prelievo 42). Saldo mittente: 58. Saldo destinatario: 40
    conto_base.bonifico(conto_destinatario, 40)
    assert conto_base.saldo == 58.0
    assert conto_destinatario.saldo == 40.0

def test_fallimento_simulato():
    assert 2 + 2 == 5