
from locust import HttpUser, between, task, tag
from http import HTTPStatus

msgFalhaRespostaObtida = "Corpo da resposta, diferente do esperado"
msgFalhaStatusCode = "Status code diferente de 200"


class CargaApiRvv(HttpUser):
    host = "https://simulador-rvv.brf.cloud"
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

    @task #Esperado era: 88.42%
    def calculate_rvv_forecast_id_5095(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 5095,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 33.33,
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
                    "forecast": 47563.019
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 17248.67
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 307827.214
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
                    f" \n Calcula valor rvv e forecast id 5095 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 88.52:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f" \n FALHA ao obter o rvv do id 5095 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

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
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement do id 5095 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

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
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 11112 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

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
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 11112 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

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
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 11861 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

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
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 11861 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_15614(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 15614,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 0,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.184
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.043
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.084
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 148
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 8030.78
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 13.23
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 65317.822
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 15614",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 15614 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 2.76:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 15614 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_15614(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 15614,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.184
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.043
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.084
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 148
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 8030.78
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 13.23
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 65317.822
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 15614",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 15614 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 15614 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_16268(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 16268,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 0,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.225
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.158
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.148
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 1628.00
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 7128.29
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 1481.40
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 34358.34
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 16268",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 16268 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 22.99:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 16268 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_16268(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 16268,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.184
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.043
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.084
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 148
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 8030.78
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 13.23
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 65317.822
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 16268",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 16268 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 16268 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_16317(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 16317,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 0,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 126
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 0
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 3.00
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 61.027
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 6398.41
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 1209.75
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 24636.134
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 16317",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 16317 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 27.69:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 16317 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_16317(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 16317,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 130
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 2.00
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 13.00
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 49.00
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 10611.27
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 1094.52
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 30411.09
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 16317",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 16317 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 16317 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_20819(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 20819,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 11.11,
            "forecast": 1,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 1087.00
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 15
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 54
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 36.203
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 49174.045
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 8190.91
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 181014.267
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 20819",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 20819 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 15.53:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 20819 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_20819(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 20819,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 1141.00
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 16
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 104
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 53
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 74958.07
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 5225.94
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 238502.79
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 20819",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 20819 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 20819 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_24349(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 24349,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 22.22,
            "forecast": 2.00,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.21
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.269
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.301
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.154
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 1545
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 20376.33
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 4214.67
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 51157.602
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 24349",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 24349 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 55.152:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 24349 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_24349(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 24349,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9.00,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.2
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.3
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 1478
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 23228.71
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 4780.87
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 54814.72
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 24349",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 24349 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 24349 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task #Esperado era: 28.16
    def calculate_rvv_forecast_id_24359(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 24359,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 33.33,
            "forecast": 3.00,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 140
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 4.00
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 7
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 28.827
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 7091.33
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 2096.67
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 17649.194
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 24359",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 24359 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 28.15:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 24359 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_24359(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 24359,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9.00,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 159
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 2
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 13
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 44
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 6983.26
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 803.68
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 21052.72
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 24359",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 24359 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 24359 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_29035(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 29035,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 0,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.166
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.186
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.144
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.133
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 1865
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 11300.12
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 2036.6
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 31949.202
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 29035",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 29035 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 31.0:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 29035 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_29035(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 29035,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.2
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.30
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 1782
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 18737.20
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 2022.12
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 50771.80
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 29035",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 29035 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 29035 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_29416(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 29416,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 11.11,
            "forecast": 1,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.153
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.203
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.185
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.149
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 0
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 396
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 8201.183
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 594.915
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 37598.342
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 29416",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 29416 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 15.19:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 29416 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_29416(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 29416,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.2
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.3
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 13
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 391
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 11630.86
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 931.12
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 54499.73
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 29416",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 29416 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 29416 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_32544(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 32544,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 11.11,
            "forecast": 1,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 100
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 1
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 1
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 39.194
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 5175.56
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 538.805
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 26112.411
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 32544",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 32544 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 9.20:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 32544 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_32544(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 32544,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 116
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 2
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 13
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 43
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 5624.5
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 1312.66
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 30508.32
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 32544",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 32544 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 32544 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_33993(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 33993,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 0,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 80
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 0
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 0
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 59.07
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 4425.275
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 873.665
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 27220.652
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 33993",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 33993 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 19.44:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 33993 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_33993(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 33993,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 82
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 2
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 13
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 61
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 5675.23
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 1258.21
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 34635.75
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 33993",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 33993 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 33993 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_34740(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 34740,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 11.11,
            "forecast": 1,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 86
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 2
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 1
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 42.759
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 5384.75
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 450.625
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 20313.577
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 34740",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 34740 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 20.69:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 34740 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_34740(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 34740,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 110
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 2
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 13
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 40
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 6657.19
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 932.07
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 25086.8
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 34740",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 34740 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 34740 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_35315(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 35315,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 0,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 99
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 0
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 2
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 42.751
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 6499.92
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 573.715
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 20251.181
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 35315",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 35315 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 0.0:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 35315 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task #Atingimento esperado era: 104%
    def calculate_achievement_id_35315(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 35315,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 121
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 0
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 13
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 55
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 8279.87
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 848.96
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 30972.90
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 35315",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 35315 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 35315 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task #Esperado era: 34.80
    def calculate_rvv_forecast_id_40814(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 40814,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 11.11,
            "forecast": 1,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.136
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.155
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.123
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.096
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 1482
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 14531.725
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 862.285
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 61531.068
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 40814",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 40814 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 34.79:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 40814 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task #Atingimento esperado era: 108%
    def calculate_achievement_id_40814(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 40814,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.2
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.3
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 1447
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 15231.49
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 1268.07
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 120567.46
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 40814",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 40814 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 40814 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_42303(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 42303,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 11.11,
            "forecast": 1,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.06
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.187
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.149
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.061
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 188
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 196428.404
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 9430.95
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 596570.15
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 42303",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 42303 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 0.0:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 42303 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task  # Atingimento esperado era: 108%
    def calculate_achievement_id_42303(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 42303,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.2
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.3
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 235
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 283653.44
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 24972.25
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 1305499.82
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 42303",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 42303 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 42303 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_42768(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 42768,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 0,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.181
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.229
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.203
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.081
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 13
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 1060
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 14888.781
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 2415.48
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 37512.745
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 42768",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 42768 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 24.1725:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 42768 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_42768(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 42768,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.2
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.3
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 13
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 1236
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 22191.14
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 2112.78
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 54044.86
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 42768",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 42768 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 42768 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_44013(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 44013,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 11.11,
            "forecast": 1,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.084
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.103
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.195
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 1380
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 18810.15
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 514.725
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 49878.675
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 44013",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 44013 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 24.0:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 44013 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_44013(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 44013,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.2
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.3
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 1117
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 43583.45
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 3500.17
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 105446.46
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 44013",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 44013 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 44013 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_45919(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 45919,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 33.33,
            "forecast": 3,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 98
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 2
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 6
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 58.741
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 8135.692
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 1526.78
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 31368.7
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 45919",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 45919 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 71.01:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 45919 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_45919(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 45919,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 103
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 2
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 13
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 44
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 5868.12
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 1529.07
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 34842.09
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 45919",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 45919 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 45919 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_46609(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 46609,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 0,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 134
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 4
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 3
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 55.085
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 8516.385
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 1139.555
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 27588.368
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 46609",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 46609 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 48.84:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 46609 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_46609(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 46609,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 139
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 2
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 13
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 42
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 9256.99
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 738.11
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 31961.07
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 46609",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 46609 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 46609 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_50088(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 50088,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 11.11,
            "forecast": 1,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.239
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.22
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.212
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.147
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 2372
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 22094.885
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 3497.74
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 67141.417
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 50088",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 50088 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 21.5357:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 50088 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_50088(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 50088,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.20
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.30
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 2589
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 25407.41
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 2699.81
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 82037.34
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 50088",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 50088 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 50088 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_51932(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 51932,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 0,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 80
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 0
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 1
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 46.383
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 4243.375
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 419.82
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 13597.449
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 51932",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 51932 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 10.31:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 51932 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_51932(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 51932,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 98
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 2
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 13
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 45
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 6565.45
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 871.14
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 19923.34
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 51932",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 51932 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 51932 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_52919(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 52919,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 0,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.185
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.234
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.172
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.216
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 851
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 27371.224
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 2806.521
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 77781.541
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 52919",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 52919 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 37.9983:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 52919 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_52919(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 52919,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.2
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.3
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 833
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 36023.54
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 2509.04
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 96463.77
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 52919",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 52919 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 52919 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_59218(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 59218,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 0,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 75
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 0
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 2
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 37.748
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 3089.85
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 481.065
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 8748.001
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 59218",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 59218 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 15.68:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 59218 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_59218(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 59218,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 110
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 7
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 13
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 39
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 5301.34
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 291.68
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 16308.81
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 59218",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 59218 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 59218 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_61305(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 61305,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 22.22,
            "forecast": 2,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 92
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 1
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 1
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 41.558
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 2442.79
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 892.195
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 11395.331
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 61305",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 61305 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 40.04:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 61305 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_61305(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 61305,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "CLIMOV",
                    "forecast": 110
                },
                {
                    "indicator": "CLIMOV NOVOS CLIENTES",
                    "forecast": 12
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 13
                },
                {
                    "indicator": "POSITIVACAO",
                    "forecast": 39
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 3268.41
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 368.68
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 12186.95
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 61305",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 61305 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 61305 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_71332(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 71332,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 11.11,
            "forecast": 1,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.173
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.192
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.208
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.119
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 21
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 8580
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 54172.11
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 8126.35
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 152593.304
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 71332",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 71332 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 0.0:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 71332 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_71332(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 71332,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.20
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.3
                },
                {
                    "indicator": "MIX IDEAL",
                    "forecast": 143
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 10849
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 68563.36
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 10061.92
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 220631.97
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 71332",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 71332 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 71332 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_72032(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 72032,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 33.33,
            "forecast": 3,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.099
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.286
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.178
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.164
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 1529
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 10506.505
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 4372.14
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 39974.719
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 72032",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 72032 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 13.9:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 72032 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_72032(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 72032,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.2
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.3
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 1685
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 16108.98
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 4242.92
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 54933.76
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 72032",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 72032 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 72032 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_rvv_forecast_id_85261(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 85261,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 0,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.255
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.155
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.203
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.068
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 1695
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 11287.845
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 1012.215
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 45569.82
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 85261",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 85261 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 26.8633:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 85261 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task
    def calculate_achievement_id_85261(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 85261,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0.2
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0.25
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0.3
                },
                {
                    "indicator": "TOTAL DE ITENS",
                    "forecast": 1651
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 16009.68
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 1821.16
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 66851.67
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 85261",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 85261 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 85261 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @task #loja ideal
    def calculate_rvv_forecast_id_85799(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 85799,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 11.11,
            "forecast": 1,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0
                },
                {
                    "indicator": "LOJA IDEAL",
                    "forecast": 7.67
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 118918.656
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 14719.333
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 310149.647
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula RVV e forecast id 85799",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula valor rvv e forecast id 85799 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 26.8633:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 85799 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")

    @tag('test1')
    @task #loja ideal
    def calculate_achievement_id_85799(self):

        calculate_rvv_endpoint = f"{self.ENDPOINT_PRIFIX_RVVSIMULATOR}"
        body = {
            "sellerCod": 85799,
            "indicator": "ATINGIMENTO VOLUME FAMILIAS",
            "date": "2023-08-25",
            "achievement": 0,
            "forecast": 9,
            "otherIndicators": [
                {
                    "indicator": "FASEAMENTO SEMANA 1",
                    "forecast": 0
                },
                {
                    "indicator": "FASEAMENTO SEMANA 2",
                    "forecast": 0
                },
                {
                    "indicator": "FASEAMENTO SEMANA 3",
                    "forecast": 0
                },
                {
                    "indicator": "FASEAMENTO SEMANA 4",
                    "forecast": 0
                },
                {
                    "indicator": "LOJA IDEAL",
                    "forecast": 6
                },
                {
                    "indicator": "VOLUME FOCO",
                    "forecast": 168715.44
                },
                {
                    "indicator": "VOLUME INOVACAO",
                    "forecast": 13322.37
                },
                {
                    "indicator": "VOLUME TOTAL",
                    "forecast": 424064.97
                }
            ]
        }
        with self.client.post(url=calculate_rvv_endpoint,
                              name="CargaSimuladorRvv - Calcula achievement id 85799",
                              catch_response=True, json=body) as response:

            rvv_calculate_response = response.json()
            print(f"Body enviado: {body}")

            try:
                print(
                    f"========== \n Calcula achievement id 85799 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "achievement" in rvv_calculate_response and rvv_calculate_response["achievement"] != 120:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)
                print("===================== \n")

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 85799 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)
                print("===================== \n")
