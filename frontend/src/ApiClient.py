# api_client.py
import requests

class ApiClient:
    def __init__(self):
        self.base_url = "http://localhost:5000"

    def login(self, usuario, senha):
        url = f"{self.base_url}/login"
        payload = {"usuario": usuario, "senha": senha}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Lança exceção para códigos 4xx e 5xx
            return response.json()       # Retorna o JSON da resposta
        except requests.exceptions.HTTPError as e:
            return {"error": f"Erro HTTP: {e.response.status_code}", "details": e.response.text}
        except requests.exceptions.RequestException as e:
            return {"error": "Erro de conexão", "details": str(e)}

    def cadastrar_usuario(self, nome, email, senha, usuario):
        url = f"{self.base_url}/cadastrar"
        payload = {
            "username": nome,
            "email": email,
            "tipo": usuario,
            "password": senha
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            return {"error": f"Erro HTTP: {e.response.status_code}", "details": e.response.text}
        except requests.exceptions.RequestException as e:
            return {"error": "Erro de conexão", "details": str(e)}
