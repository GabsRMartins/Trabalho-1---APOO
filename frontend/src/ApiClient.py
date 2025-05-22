# api_client.py
import requests

class ApiClient:
    def __init__(self):
        self.base_url = "http://localhost:5000"

    def login(self, usuario, senha):
        url = f"{self.base_url}/login"
        payload = {"username": usuario, "password": senha}
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
        
    def getUserName(self,nome):
      url = f"{self.base_url}/usuario/usuarioLogado"
      try:
          response = requests.get(url)
          response.raise_for_status
      except requests.exceptions.HTTPError as e:
            return {"error": f"Erro HTTP: {e.response.status_code}", "details": e.response.text}
      except requests.exceptions.RequestException as e:
             return {"error": "Erro de conexão", "details": str(e)}

    def getEventos(self):
        url = f"{self.base_url}/eventos"
        try:
            response = requests.get(url)
            response.raise_for_status()  # <<< Faltavam os parênteses aqui
            return response.json()  # <<< Retorne os dados corretamente
        except requests.exceptions.HTTPError as e:
            print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão: {e}")
        
        return [] 