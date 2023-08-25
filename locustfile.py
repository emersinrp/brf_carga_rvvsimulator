import random
from random import choice

from locust import HttpUser, between, task, tag
from http import HTTPStatus

msgFalhaRespostaObtida = "Corpo da resposta, diferente do esperado"
msgFalhaStatusCode = "Status code diferente de 200"


class CargaApiRvv(HttpUser):
    host = "https://simulador-rvv-qas.brf.cloud"
    wait_time = between(1.0, 3.0)

    ENDPOINT_PRIFIX_RVVSIMULATOR = "/rvvsimulator/calculate"
    OTHERS_INDICATORS = [
        {
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "forecast": 9.00
        },
        {
            "indicator": "CLIMOV",
            "forecast": 142.00
        },
        {
            "indicator": "MCR",
            "forecast": 13.00
        },
        {
            "indicator": "VOLUME INOVACAO",
            "forecast": 1785.69
        },
        {
            "indicator": "VOLUME FOCO",
            "forecast": 8956.14
        },
        {
            "indicator": "VOLUME TOTAL",
            "forecast": 33898.62
        }
    ]

    @task
    def calculate_others_rvv_indicators(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 11112,
            "indicator": "POSITIVACAO",
            "date": "2023-08-01",
            "achievement": 0,
            "forecast": 57.00,
            "otherIndicators": [
                choice(self.OTHERS_INDICATORS)
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula valor RVV Indicators",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor RVV \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 84.10:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)

            except Exception as ex:
                print(
                    f"========== \n FALHA no calculo do valor de RVV \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

    @task
    def calculate_all_rvv_indicators(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 11112,
            "indicator": "POSITIVACAO",
            "date": "2023-08-01",
            "achievement": 0,
            "forecast": 57.00,
            "otherIndicators": [
                {
                    "indicator": "ATINGIMENTO VOLUME FAMILIAS",
                    "forecast": 9.00
                },
                {
                    "indicator": "CLIMOV",
                    "forecast": 142.00
                },
                {
                    "indicator": "MCR",
                    "forecast": 13.00
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 1785.69
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 8956.14
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 33898.62
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula Todos RVVs",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula todos valores RVV \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 84.0:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)

            except Exception as ex:
                print(
                    f"========== \n FALHA no calculo de todos os valores de RVV \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

    @task
    def calculate_forecast_mix_ideal(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 11112,
            "indicator": "MIX IDEAL",
            "date": "2023-08-01",
            "achievement": 100,
            "forecast": "",
            "otherIndicators": [

            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula forecast indicator Mix Ideal",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor forecast Mix Ideal \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 104.32:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o forecast do indicador MIX IDEAL  \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

    @task
    def calculate_achievement_mix_ideal(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 11112,
            "indicator": "MIX IDEAL",
            "date": "2023-08-01",
            "achievement": "",
            "forecast": 13,
            "otherIndicators": [

            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement indicator Mix Ideal",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor achievement Mix Ideal \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 100:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement do indicador MIX IDEAL  \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

    @task
    def calculate_rvv_forecast_id_5095(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 5095,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 3,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.226
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.333
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.302
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.239
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 276.00
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 47563.02
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 17248.67
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 307827.21
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 5095",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 5095 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 88.32:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 5095 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

    @task
    def calculate_achievement_id_5095(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 5095,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 3,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.226
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.333
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.302
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.239
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 276.00
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 47563.02
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 17248.67
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 307827.21
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 5095",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor achievement id 5095 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 0:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement do id 5095 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

    @task
    def calculate_rvv_forecast_id_11112(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 11112,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 11.11,
            "forecast": 1,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 141.00
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 6
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 9
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 58.537
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 276.00
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 7202.86
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 1447.195
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 26127.149
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 11112",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 11112 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 32.2:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 11112 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

    @task
    def calculate_achievement_id_11112(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 11112,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 1,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 141.00
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 6
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 9
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 58.537
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 276.00
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 7202.86
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 1447.195
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 26127.149
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 11112",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 11112 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 0:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 11112 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

    @task
    def calculate_rvv_forecast_id_11861(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 11861,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 0,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": -0.253
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.199
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.319
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.034
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 248
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 38317.93
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 840
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 107973.87
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 11861",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 11861 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 3.6:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 11861 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

    @tag('test1')
    @task
    def calculate_achievement_id_11861(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 11861,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 0,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": -0.253
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.199
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.319
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.034
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 248
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 38317.93
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 840
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 107973.87
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 11861",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 11861 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 0:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 11861 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)




