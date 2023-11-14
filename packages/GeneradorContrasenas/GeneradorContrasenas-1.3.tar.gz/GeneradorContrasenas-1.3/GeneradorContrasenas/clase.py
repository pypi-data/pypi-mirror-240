import random

class LongitudInvalidaException(Exception): 
    pass

class GenerarContrasena(): 
    def __init__(self, longitud, incluir_mayusculas, incluir_numeros, incluir_especiales, cadena_personalizar = ''): 
        self.longitud = longitud
        self.incluir_mayusculas = incluir_mayusculas
        self.incluir_numeros = incluir_numeros
        self.incluir_especiales = incluir_especiales
        self.cadena_personalizar = cadena_personalizar

        self.minusculas = "abcdefghijklmnopqrstuvwxyz" # no hay ñ
        self.mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # no hay Ñ
        self.digitos = "0123456789"
        self.especiales = "!#$%&()+-/<=>?@[\]_{|}"

    @property
    def minusculas(self): 
        return self.__minusculas
    
    @minusculas.setter
    def minusculas(self, minusculas): 
        self.__minusculas = minusculas

    @property
    def mayusculas(self): 
        return self.__mayusculas
    
    @mayusculas.setter
    def mayusculas(self, mayusculas): 
        self.__mayusculas = mayusculas

    @property
    def digitos(self): 
        return self.__digitos
    
    @digitos.setter
    def digitos(self, digitos): 
        self.__digitos = digitos

    @property
    def especiales(self): 
        return self.__especiales
    
    @especiales.setter
    def especiales(self, especiales): 
        self.__especiales = especiales

    def personalizar(self):
        if self.cadena_personalizar == '':
            self.contrasena_pers = ''
        else:
            self.contrasena_pers = self.cadena_personalizar
        return self.contrasena_pers

    def crear_contrasena(self): 
        self.contrasena = ""
        caracteres = self.__minusculas

        if self.incluir_mayusculas == "SI": 
            caracteres += self.__mayusculas
            self.contrasena += random.choice(self.__mayusculas)

        if self.incluir_numeros == "SI": 
            caracteres += self.__digitos
            self.contrasena += random.choice(self.__digitos)

        if self.incluir_especiales == "SI": 
            caracteres += self.__especiales
            self.contrasena += random.choice(self.__especiales)

        longitud_restante = self.longitud - len(self.contrasena)
        
        self.contrasena_pers = self.personalizar()

        if longitud_restante < len(self.contrasena_pers):
            raise LongitudInvalidaException("La longitud especificada no es viable para el número de condiciones.")
        elif len(self.contrasena_pers) != 0: 
            self.contrasena += "".join(self.contrasena_pers)
            longitud_restante = self.longitud - len(self.contrasena)
            if longitud_restante > 0:
                self.contrasena += "".join(random.choice(caracteres) for i in range(longitud_restante))
        else:   
            self.contrasena += "".join(random.choice(caracteres) for i in range(longitud_restante))
            contrasena_lista = list(self.contrasena)
            random.shuffle(contrasena_lista)
            self.contrasena = "".join(contrasena_lista)
        return self.contrasena
    
    def mostrar(self): 
        return "La contraseña generada es: " + self.contrasena
    

class GenerarContrasenasMultiples(GenerarContrasena): 
    def __init__(self, longitud, incluir_mayusculas, incluir_numeros, incluir_especiales, num_contrasenas, cadena_personalizar=''):
        super().__init__(longitud, incluir_mayusculas, incluir_numeros, incluir_especiales, cadena_personalizar)
        self.num_contrasenas = num_contrasenas

    def GenerarMultiples(self): 
        cont = 0
        self.contras = []
        while cont < self.num_contrasenas: 
            contra = super().crear_contrasena()
            self.contras.append(contra)
            cont += 1
        return self.contras


    def mostrar(self): 
        return "Las contraseñas generadas son: " + ', '.join(self.contras)

class EjecutarGeneradorContrasena():

    def EjecutarGenerador(self):
        try:
            try: 
                long = int(input("Numero de digitos que tendrá la contraseña:"))
                
            except ValueError as e: 
                print("No se ha introducido un número de digitos para la contraseña. ")
            
            else: 
                may = input('Quieres mayúsculas (SI/NO)? ')
                num = input('Quieres números (SI/NO)? ')
                esp = input('Quieres carácteres especiales (SI/NO)? ')
                if ((may == "SI") | (may == "NO")) & ((num == "SI") | (num == "NO")) & ((esp == "SI") | (esp == "NO")): 
                    quiere_pers = input('Quieres personalizar tu contraseña (SI/NO)? ')
                    if quiere_pers == 'SI':
                        que_quieres = input('Qué quieres añadir? ')
                        if len(que_quieres) > long: 
                            raise LongitudInvalidaException("La longitud especificada no es viable para el número de condiciones.")
                        else: 
                            resp = input("¿Quieres generar multiples contraseñas (SI/NO)? ")
                            if resp == "SI": 
                                try: 
                                    resp_si = int(input("¿Cuantas? "))
                                    generador = GenerarContrasenasMultiples(long, may, num, esp, resp_si, que_quieres)
                                    generador.GenerarMultiples()
                                    print(generador.mostrar())
                                except ValueError as e: 
                                    print("No se ha introducido un número de contraseñas valido. ")
                            elif resp == "NO": 
                                generador = GenerarContrasena(long, may, num, esp, que_quieres)
                                generador.crear_contrasena()
                                print(generador.mostrar())

                            else:
                                print("No se ha introducido una respuesta valida")
                    elif quiere_pers == 'NO':
                        resp = input("¿Quieres generar multiples contraseñas (SI/NO)? ")
                        if resp == "SI": 
                            try: 
                                resp_si = int(input("¿Cuantas? "))
                                generador = GenerarContrasenasMultiples(long, may, num, esp, resp_si)
                                generador.GenerarMultiples()
                                print(generador.mostrar())
                            except ValueError as e: 
                                print("No se ha introducido un número de contraseñas valido. ")
                        elif resp == "NO": 
                            generador = GenerarContrasena(long, may, num, esp)
                            generador.crear_contrasena()
                            print(generador.mostrar())

                        else:
                            print("No se ha introducido una respuesta valida (SI/NO)")
                    else:
                        print("No se ha introducido una respuesta valida (SI/NO)")
                else: 
                    print("No se ha introducido una respuesta valida (SI/NO)")

        except LongitudInvalidaException as e:
            print(e)
