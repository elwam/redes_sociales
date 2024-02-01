from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(10, 20)  # Tiempo aleatorio de espera entre solicitudes
    numeros_documento = [41524193]

    @task
    def consultar_listad_ciudadanos(self):
        self.client.get("https://172.171.225.112:9443/server/c360/ds_informacion_ciudadano/views/ca_vi_listado_personas?$select=tipo_documento,numero_documento,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,id_hogar,edad,cod_localidad,nomlocalidad,cod_upz,nomupz,telefono,indigena,gitano,nap,palenquero,raizal,victima,habitante_calle,lgtbi,migrante,rural,discapacidad,GROUP_CONCAT('-', beneficio)%20as%20beneficios&$filter=codigo_beneficio%20in%20(101,102)&$groupby=tipo_documento,numero_documento,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,id_hogar,edad,cod_localidad,nomlocalidad,cod_upz,nomupz,telefono,indigena,gitano,nap,palenquero,raizal,victima,habitante_calle,lgtbi,migrante,rural,discapacidad&$start_index=0&$count=10&$format=json", verify=False,  timeout=180)
        
        
'''   
    @task
    def consultar_listad_ciudadanos(self):
        self.client.get("https://172.171.225.112:9443/server/c360/ds_informacion_ciudadano/views/ca_vi_listado_personas/$count?$select=tipo_documento,numero_documento&$filter=codigo_beneficio%20in%20(101,102)&$groupby=tipo_documento,numero_documento&$format=json", verify=False,  timeout=30)
        self.client.get("https://172.171.225.112:9443/server/c360/ds_informacion_ciudadano/views/ca_vi_listado_personas/$count?$select=id_hogar&$filter=codigo_beneficio%20in%20(101,102)&$groupby=id_hogar&$format=json", verify=False,  timeout=30)



        params = {
            '$select': "tipo_documento,numero_documento,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,id_hogar,edad,cod_localidad,nomlocalidad,cod_upz,nomupz,telefono,indigena,gitano,nap,palenquero,raizal,victima,habitante_calle,lgtbi,migrante,rural,discapacidad,GROUP_CONCAT('-', beneficio) as beneficios",
            '$filter': 'codigo_beneficio in (101,102)',
            '$groupby': 'tipo_documento,numero_documento,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,id_hogar,edad,cod_localidad,nomlocalidad,cod_upz,nomupz,telefono,indigena,gitano,nap,palenquero,raizal,victima,habitante_calle,lgtbi,migrante,rural,discapacidad',
            '$start_index': '0',
            '$count': '10',
            '$format': 'json'
        }
        self.client.get("/server/c360/ds_informacion_ciudadano/views/ca_vi_listado_personas", params=params, verify=False,  timeout=30)

        params_personas = {
            '$select': 'tipo_documento,numero_documento',
            '$filter': 'codigo_beneficio in (101,102)',
            '$groupby': 'tipo_documento,numero_documento',
            '$format': 'json'
        }
        self.client.get("/server/c360/ds_informacion_ciudadano/views/ca_vi_listado_personas/$count", params=params_personas, verify=False,  timeout=30)

        params_hogares = {
            '$select': 'id_hogar',
            '$filter': 'codigo_beneficio in (101,102)',
            '$groupby': 'id_hogar',
            '$format': 'json'
        }

        self.client.get("/server/c360/ds_informacion_ciudadano/views/ca_vi_listado_personas/$count", params=params_hogares, verify=False,  timeout=30)
'''
'''

    @task
    def consultar_entrega_beneficios(self):
        self.client.get("/server/c360/ds_informacion_ciudadano/views/ca_vi_entrega_beneficios_ciudadano/?$format=json&tipo_documento=1&numero_documento=41524193", verify=False,  timeout=30)
        # Tarea para consultar el servicio adicional
        #for numero_documento in self.numeros_documento:
        #   params2 = {'tipo_documento': '1', 'numero_documento': numero_documento}
        #    self.client.get("/server/c360/ds_informacion_ciudadano/views/ca_vi_entrega_beneficios_ciudadano/?$format=json", params=params2, verify=False,  timeout=30)

'''




'''
    @task
    def validar_reglas_atencion_comedor(self):
        # Tarea para consultar el segundo servicio adicional
        self.client.get("/server/c360/ds_validacion_ciudadano_sdis/views/ca_vi_validacion_reglas_en_atencion_comedor/?$format=json", verify=False)

'''

'''
import requests

class MiClase:
    def __init__(self):
        self.base_url = "https://172.171.225.112:9443/server/c360/ds_informacion_ciudadano/views/"

    def llamar_servicio_1(self):
        url = self.base_url + "ca_vi_listado_personas"
        params = {
            '$select': 'tipo_documento,numero_documento,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,id_hogar,edad,cod_localidad,nomlocalidad,cod_upz,nomupz,telefono,indigena,gitano,nap,palenquero,raizal,victima,habitante_calle,lgtbi,migrante,rural,discapacidad,GROUP_CONCAT('-', beneficio) as beneficios',
            '$filter': 'codigo_beneficio in (101,102)',
            '$groupby': 'tipo_documento,numero_documento,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,id_hogar,edad,cod_localidad,nomlocalidad,cod_upz,nomupz,telefono,indigena,gitano,nap,palenquero,raizal,victima,habitante_calle,lgtbi,migrante,rural,discapacidad',
            '$start_index': '0',
            '$count': '10',
            '$format': 'json'
        }
        response = requests.get(url, params=params, verify=False, timeout=30)
        return response

    def llamar_servicio_2(self):
        url = self.base_url + "ca_vi_listado_personas/$count"
        params = {
            '$select': 'tipo_documento,numero_documento',
            '$filter': 'codigo_beneficio in (101,102)',
            '$groupby': 'tipo_documento,numero_documento',
            '$format': 'json'
        }
        response = requests.get(url, params=params, verify=False, timeout=30)
        return response

    def llamar_servicio_3(self):
        url = self.base_url + "ca_vi_listado_personas/$count"
        params = {
            '$select': 'id_hogar',
            '$filter': 'codigo_beneficio in (101,102)',
            '$groupby': 'id_hogar',
            '$format': 'json'
        }
        response = requests.get(url, params=params, verify=False, timeout=30)
        return response

# Uso de la clase
mi_instancia = MiClase()
respuesta_servicio_1 = mi_instancia.llamar_servicio_1()
respuesta_servicio_2 = mi_instancia.llamar_servicio_2()
respuesta_servicio_3 = mi_instancia.llamar_servicio_3()


'''