import os

from dotenv import load_dotenv

load_dotenv()

USUARIO = os.getenv("ORACLE_USER")
SENHA = os.getenv("ORACLE_PASSWORD")

HOST = os.getenv("ORACLE_HOST")
PORTA = os.getenv("ORACLE_PORT")
SERVICO = os.getenv("ORACLE_SERVICE")