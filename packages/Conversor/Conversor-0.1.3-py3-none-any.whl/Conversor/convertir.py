import requests

class CheckErrors:
    def __init__(self, value_or_values, measure_from, measure_to):
        self.value_or_values = value_or_values
        self.measure_from = measure_from
        self.measure_to = measure_to
        self.monedas = ["EUR", "USD", "MXP", "CNY", "GBP", "RUB", "JPY", "INR", "CHF"]
        self.longitud = ["KM", "HM", "DAM", "M", "DM", "CM", "MM"]
        self.liquidos = ["KL", "HL", "DAL", "L", "DL", "CL", "ML"]
        self.tiempo = ["YEAR", "MONTH", "WEEK", "DAY", "HOUR", "MINUTE", "SECOND"]
        self.area = ["HA","KM2","HM2", "DAM2", "M2", "DM2", "CM2", "MM2"]
        self.volumen = ["KM3","HM3", "DAM3", "M3", "DM3", "CM3", "MM3"]
        self.medida = None
        self.check_is_number()

    def check_is_number(self):
        '''Comprueba si un valor o un iterable de valores es convertible a numérico.
        
        Params:
            - value_or_values: valor/iterable.
            
        Devuelve:
            - Inputs en una lista de manera que sean iterables.'''
        if not self.check_input_type() or (self.check_input_type() == 1 and self.value_or_values and len([self.value_or_values])==1):
            self.value_or_values = [float(self.value_or_values)]
        for elem in self.value_or_values: #Si es 1 solo lo hará para ese valor. #Si es Str todos sus elementos deben ser Nums para que el Str completo lo sea.
            float(elem)
        
    def check_input_type(self)->int:
        '''Comprueba el tipo de dato que es el input.
        
        Params:
            - value_or_values: valor/iterable.
            
        Devuelve:
            - 0 si es un str, 1 si es de tipo float y 2 si es de cualquier otro tipo.'''
        if type(self.value_or_values)==str:
            return 0
        elif type(self.value_or_values)==int or type(self.value_or_values)==float:
            return 1
        else:
            return 2

class MedidaLongitud(CheckErrors):
    def __init__(self, value_or_values, measure_from, measure_to):
        super().__init__(value_or_values, measure_from, measure_to)

    def cambio_longitudes(self):
        '''Conversor para cambiar medidas de longitud.
        
        Params:
            - Atributos de entrada a la clase.
            
        Devuelve:
            - Variable value_or_values cambiando los valores de la medida de entrada a la medida de salida.'''
        indice = 0
        for i in self.longitud:
            if self.measure_from == i:
                indice_medida1 = indice
            if self.measure_to == i:
                indice_medida2 = indice
            indice += 1
        
        if indice_medida1 < indice_medida2:
            mode = 0
        else:
            mode = 1
        
        for i in range(len(self.value_or_values)):
            if mode == 0:
                self.value_or_values[i] = self.value_or_values[i] * 10**(indice_medida2 - indice_medida1)
            else:
                self.value_or_values[i] = self.value_or_values[i] / 10**(indice_medida1 - indice_medida2)

class MedidaArea(CheckErrors):
    def __init__(self, value_or_values, measure_from, measure_to):
        super().__init__(value_or_values, measure_from, measure_to)

    def cambio_areas(self):
        '''Conversor para cambiar medidas de áreas.
        
        Params:
            - Atributos de entrada a la clase.
            
        Devuelve:
            - Variable value_or_values cambiando los valores de la medida de entrada a la medida de salida.'''
        indice = 0
        for i in self.area:
            if self.measure_from == i:
                indice_medida1 = indice
            if self.measure_to == i:
                indice_medida2 = indice
            indice += 1
        
        if indice_medida1 < indice_medida2:
            mode = 0
        else:
            mode = 1
        
        for i in range(len(self.value_or_values)):
            if mode == 0:
                self.value_or_values[i] = self.value_or_values[i] * 100**(indice_medida2 - indice_medida1)
            else:
                self.value_or_values[i] = self.value_or_values[i] / 100**(indice_medida1 - indice_medida2)

class MedidaVolumen(CheckErrors):
    def __init__(self, value_or_values, measure_from, measure_to):
        super().__init__(value_or_values, measure_from, measure_to)

    def cambio_volumenes(self):
        '''Conversor para cambiar medidas de volumenes.
        
        Params:
            - Atributos de entrada a la clase.
            
        Devuelve:
            - Variable value_or_values cambiando los valores de la medida de entrada a la medida de salida.'''
        indice = 0
        for i in self.volumen:
            if self.measure_from == i:
                indice_medida1 = indice
            if self.measure_to == i:
                indice_medida2 = indice
            indice += 1
        
        if indice_medida1 < indice_medida2:
            mode = 0
        else:
            mode = 1
        
        for i in range(len(self.value_or_values)):
            if mode == 0:
                self.value_or_values[i] = self.value_or_values[i] * 1000**(indice_medida2 - indice_medida1)
            else:
                self.value_or_values[i] = self.value_or_values[i] / 1000**(indice_medida1 - indice_medida2)

class MedidasLiquidos(CheckErrors):
    def __init__(self, value_or_values, measure_from, measure_to):
        super().__init__(value_or_values, measure_from, measure_to)

    def cambio_liquidos(self):
        '''Conversor para cambiar medidas de liquidos.
        
        Params:
            - Atributos de entrada a la clase.
            
        Devuelve:
            - Variable value_or_values cambiando los valores de la medida de entrada a la medida de salida.'''
        indice = 0
        for i in self.liquidos:
            if self.measure_from == i:
                indice_medida1 = indice
            if self.measure_to == i:
                indice_medida2 = indice
            indice += 1
        
        if indice_medida1 < indice_medida2:
            mode = 0
        else:
            mode = 1
        
        for i in range(len(self.value_or_values)):
            if mode == 0:
                self.value_or_values[i] = self.value_or_values[i] * 10**(indice_medida2 - indice_medida1)
            else:
                self.value_or_values[i] = self.value_or_values[i] / 10**(indice_medida1 - indice_medida2)

class MedidaMonedas(CheckErrors):
    def __init__(self, value_or_values, measure_from, measure_to):
        super().__init__(value_or_values, measure_from, measure_to)

    def cambio_monedas(self):
        '''Conversor para cambiar entre medidas monetarias.
        
        Params:
            - Atributos de entrada a la clase.
            
        Devuelve:
            - Variable value_or_values cambiando los valores de la medida de entrada a la medida de salida.'''
        import requests
        for i in range(len(self.value_or_values)):
            url='https://api.api-ninjas.com/v1/convertcurrency?have='+self.measure_from+'&want='+self.measure_to+'&amount='+str(self.value_or_values[i])
            response=requests.get(url,headers={'X-API-KEY':'xRIFC4JjW7IMhQpsVbYs4Q==IwpSgRDfoQ4zHbV1'})
            #print(response.text)
            valor = ""
            inicio = 0
            elementos = ["e", ".", "+"]
            for caracter in response.text:
                if caracter.isnumeric():
                    inicio = 1
                    valor += caracter
                elif (inicio == 1 and caracter in elementos):
                    valor += caracter
                if caracter == ",":
                    break
            if valor == "":
                raise (Exception)
            try:
                valor = float(valor)
            except ValueError:
                print("La transformación entre monedas no ha sido posible\n")
            self.value_or_values[i] = valor

class MedidaTiempo(CheckErrors):
    def __init__(self, value_or_values, measure_from, measure_to):
        super().__init__(value_or_values, measure_from, measure_to)
    
    def year_month(self, value, mode):
        if (mode == 0):
            value *= 12
        else:
            value /= 12
        return (value)

    def month_week(self, value, mode):
        if (mode == 0):
            value *= 4
        else:
            value /= 4
        return (value)
    
    def week_day(self, value, mode):
        if (mode == 0):
            value *= 7
        else:
            value /= 7
        return (value)
    
    def day_hour(self, value, mode):
        if (mode == 0):
            value *= 24
        else:
            value /= 24
        return (value)
    
    def hour_minute(self, value, mode):
        if (mode == 0):
            value *= 60
        else:
            value /= 60
        return (value)
    
    def minute_second(self, value, mode):
        if (mode == 0):
            value *= 60
        else:
            value /= 60
        return (value)

    def cambio_tiempo(self):
        '''Conversor para cambiar medidas de tiempo.
        
        Params:
            - Atributos de entrada a la clase.
            
        Devuelve:
            - Variable value_or_values cambiando los valores de la medida de entrada a la medida de salida.'''
        indice = 0
        for i in self.tiempo:
            if self.measure_from == i:
                indice_medida1 = indice
            if self.measure_to == i:
                indice_medida2 = indice
            indice += 1
        
        if indice_medida1 < indice_medida2:
            mode = 0
        else:
            mode = 1

        for i in range(len(self.value_or_values)):
            indice_medida1_copy = indice_medida1
            indice_medida2_copy = indice_medida2
            if mode == 0:
                while indice_medida1_copy < indice_medida2_copy:
                    if (indice_medida1_copy == 0):
                        self.value_or_values[i] = self.year_month(self.value_or_values[i], mode)
                    elif (indice_medida1_copy == 1):
                        self.value_or_values[i] = self.month_week(self.value_or_values[i], mode)
                    elif (indice_medida1_copy == 2):
                        self.value_or_values[i] = self.week_day(self.value_or_values[i], mode)
                    elif (indice_medida1_copy == 3):
                        self.value_or_values[i] = self.day_hour(self.value_or_values[i], mode)
                    elif (indice_medida1_copy == 4):
                        self.value_or_values[i] = self.hour_minute(self.value_or_values[i], mode)
                    elif (indice_medida1_copy == 5):
                        self.value_or_values[i] = self.minute_second(self.value_or_values[i], mode)
                    indice_medida1_copy += 1
            else:
                while indice_medida2_copy > indice_medida1_copy:
                    if (indice_medida2_copy == 5):
                        self.value_or_values[i] = self.minute_second(self.value_or_values[i], mode)
                    elif (indice_medida2_copy == 4):
                        self.value_or_values[i] = self.hour_minute(self.value_or_values[i], mode)
                    elif (indice_medida2_copy == 3):
                        self.value_or_values[i] = self.day_hour(self.value_or_values[i], mode)
                    elif (indice_medida2_copy == 2):
                        self.value_or_values[i] = self.week_day(self.value_or_values[i], mode)
                    elif (indice_medida2_copy == 1):
                        self.value_or_values[i] = self.month_week(self.value_or_values[i], mode)
                    elif (indice_medida2_copy == 0):
                        self.value_or_values[i] = self.year_month(self.value_or_values[i], mode)
                    indice_medida2_copy -= 1

class Conversor(MedidaLongitud, MedidasLiquidos, MedidaArea, MedidaVolumen, MedidaMonedas, MedidaTiempo):
    def __init__(self, value_or_values, measure_from, measure_to):
        super().__init__(value_or_values, measure_from, measure_to)
        self.check_measures()
    
    def check_measures(self):
        '''Función que se encarga de ejecutar la función de cambio correcta en base a las medidas de cambio del input.
        
        Params:
            - Atributos de entrada a la clase.
            
        Devuelve:
            - Variable value_or_values con los valores actualizados.'''
        if self.measure_from in self.monedas and self.measure_to in self.monedas:
            self.cambio_monedas()
        elif (self.measure_from in self.longitud and self.measure_to in self.longitud):
            self.cambio_longitudes()
        elif (self.measure_from in self.liquidos and self.measure_to in self.liquidos):
            self.cambio_liquidos()
        elif (self.measure_from in self.tiempo and self.measure_to in self.tiempo):
            self.cambio_tiempo()
        elif (self.measure_from in self.area and self.measure_to in self.area):
            self.cambio_areas()
        elif (self.measure_from in self.volumen and self.measure_to in self.volumen):
            self.cambio_volumenes()
        else:
            raise(Exception("La conversión que intenta realizar no es posible, compruebe que los valores son correctos y que ambas medidas pertenecen al mismo dominio\n"))
        return(self.value_or_values)