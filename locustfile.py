
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
                    f"========== \n Calcula valor rvv e forecast id 5095 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 88.52:
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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 15614 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 15614 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 16268 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 16268 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 16317 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 16317 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 20819 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 20819 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

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
                if "rvv" in rvv_calculate_response and rvv_calculate_response["rvv"] != 55.15:
                    raise Exception(msgFalhaRespostaObtida)
                if response.status_code != HTTPStatus.OK:
                    raise Exception(msgFalhaStatusCode)

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 24349 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 24349 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 24359 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 24359 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 24359 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 29035 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 29416 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 29416 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o rvv do id 32544 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)

    @tag('test1')
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

            except Exception as ex:
                print(
                    f"========== \n FALHA ao obter o achievement id 32544 \n {rvv_calculate_response} \n Status code: {response.status_code}")
                print(f"Corpo do erro: {rvv_calculate_response}")
                response.failure(ex.args)