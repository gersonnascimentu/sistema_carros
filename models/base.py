# models/base.py

import json
import os

class BaseModel:
    """
    Esta classe é responsável por:
    - Criar e ler arquivos JSON
    - Salvar dados no JSON
    - Carregar dados do JSON

    Outras classes irão HERDAR esta classe
    para poder salvar informações sem escrever código repetido.
    """

    arquivo = ""  # cada classe filha define seu próprio arquivo

    def salvar(self, dados):
        """
        Este método SALVA um registro no arquivo JSON.

        COMO FUNCIONA:
        1. Carrega todos os registros já existentes.
        2. Adiciona o novo dado à lista.
        3. Salva tudo no arquivo novamente.
        """

        # 1 - Lê todos os dados antigos
        lista = self.carregar_todos()

        # 2 - Adiciona os dados novos
        lista.append(dados)

        # 3 - Reescreve o arquivo com a lista atualizada
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)

    def carregar_todos(self):
        """
        Lê todos os registros do arquivo JSON.

        Se o arquivo não existir ainda, devolve uma lista vazia.
        """

        # Se o arquivo ainda não existe, começamos com lista vazia
        if not os.path.exists(self.arquivo):
            return []

        # Caso exista, carregamos tudo
        with open(self.arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
