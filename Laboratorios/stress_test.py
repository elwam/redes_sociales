from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(10, 20)  # Tiempo aleatorio de espera entre solicitudes
    numeros_documento = [41524193]

    @task
    def consultar_informacion_ciudadano(self):
        self.client.get("/server/c360/ds_informacion_ciudadano/views/ca_vi_informacion_ciudadano/?$format=json&tipo_documento=1&fuente=1&numero_documento=41524193", verify=False,  timeout=30)
      #  for numero_documento in self.numeros_documento:
      #      params = {'tipo_documento': '1', 'fuente':'1', 'numero_documento': numero_documento}
      #      self.client.get("/server/c360/ds_informacion_ciudadano/views/ca_vi_informacion_ciudadano/?$format=json", params=params, verify=False,  timeout=30)

    @task
    def consultar_entrega_beneficios(self):
        self.client.get("/server/c360/ds_informacion_ciudadano/views/ca_vi_entrega_beneficios_ciudadano/?$format=json&tipo_documento=1&numero_documento=41524193", verify=False,  timeout=30)
        # Tarea para consultar el servicio adicional
        #for numero_documento in self.numeros_documento:
        #   params2 = {'tipo_documento': '1', 'numero_documento': numero_documento}
        #    self.client.get("/server/c360/ds_informacion_ciudadano/views/ca_vi_entrega_beneficios_ciudadano/?$format=json", params=params2, verify=False,  timeout=30)



'''
    @task
    def validar_reglas_atencion_comedor(self):
        # Tarea para consultar el segundo servicio adicional
        self.client.get("/server/c360/ds_validacion_ciudadano_sdis/views/ca_vi_validacion_reglas_en_atencion_comedor/?$format=json", verify=False)

'''