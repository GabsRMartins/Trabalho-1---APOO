# api_client.py
import requests
from Interface.EventoInterface import EventoInterface
from Interface.UsuarioInterface import UsuarioInterface


class ApiClient:
    def __init__(self):
        self.base_url = "http://localhost:5000"
        self.token = None 

    def _get_headers(self):
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers


    def login(self, usuario, senha):
        url = f"{self.base_url}/login"
        payload = {"username": usuario, "password": senha}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            self.token = data.get("access_token")
            return data
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
          response.raise_for_status()
      except requests.exceptions.HTTPError as e:
            return {"error": f"Erro HTTP: {e.response.status_code}", "details": e.response.text}
      except requests.exceptions.RequestException as e:
             return {"error": "Erro de conexão", "details": str(e)}

    def getEventos(self):
     url = f"{self.base_url}/eventos"
     try:
        response = requests.get(url)
        response.raise_for_status()
        eventos_dict = response.json()
        eventos_obj = [
            EventoInterface(
                nome=e["nome"],
                local=e["local"],        
                horario=e["horario"],
                organizadora=e["organizadora"],
                preco=e["preco"],
            ) for e in eventos_dict
        ]
        return eventos_obj  
     except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")
     except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
     return []
    

    def getDadosLogado(self):
        url = f"{self.base_url}/usuario/usuarioLogado"
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()
            usuario_dict = response.json()
            return UsuarioInterface(
                nome=usuario_dict["nome"],
                email=usuario_dict["email"]
            )
        except requests.exceptions.HTTPError as e:
            print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão: {e}")
        return None