from funtions import *

end = 0
score = 0
forceEnd = 0
win = False

## intentos
while end != 1:
    ## end "forzado"
    if forceEnd == 1:
        break

    if win == False:
        score = 0

    ## declaraciones
    end = 0
    clearConsole()
    end2 = 1
    words = ['minuto', 'revista', 'abrigo', 'primero', 'menor', 'carne', 'resultado', 'ajeno',  'nacer', 'facil', 'insecto', 'probar', 'pecho', 'hotel', 'haber', 'acierto', 'quitar', 'cielo', 'pueblo', 'gato', 'era', 'grupo', 'pedir', 'relacion', 'formacion', 'arbol', 'alto', 'hueso', 'gris', 'exito', 'saber', 'comenzar', 'cero', 'malo', 'ley', 'mayor', 'gluteos', 'universal', 'cola', 'yegua', 'blando', 'aumento', 'articulo', 'urbano', 'ordinales', 'mercado', 'tocar', 'halcon', 'pino', 'sobrina', 'primo', 'hija', 'problema', 'amplio', 'oveja', 'cargo', 'junto', 'por', 'prenda',  'el', 'musica', 'hermano', 'vida', 'norte', 'pintura', 'segundo', 'hora',   'proyecto',   'atun',  'japones', 'clima', 'pegar', 'doblar', 'hacer', 'volver', 'vehiculo',  'ruta', 'obra', 'fase', 'sector', 'firme', 'oler', 'cuadro', 'bus', 'oceano', 'aire',  'cerro',  'ultimo', 'transito', 'camino', 'precisar', 'vuelto', 'humano', 'azul', 'publico', 'explicar',  'relativo', 'nuestra', 'ayer', 'decimo', 'gramo', 'paso', 'odiar', 'abuelo', 'y', 'año', 'brazo', 'epoca', 'tranquilo', 'estado', 'pera', 'calzon', 'lombriz', 'colega', 'nuez', 'ligero', 'luz', 'salud', 'delgado', 'permiso', 'evitar', 'bolsa', 'dato', 'cien', 'igual', 'origen', 'fruta', 'ciruela', 'base', 'tren', 'vez', 'debil', 'acuerdo',  'mesa', 'adjetivos', 'parecido', 'hombre', 'noche', 'quinto', 'cuenta', 'hechos', 'sal', 'hijo', 'tomate', 'hogar',  'potencia', 'bajo', 'grado', 'muñeca', 'clase', 'pierna', 'nieta', 'cerdo', 'culo', 'trueno',  'cafe', 'simple', 'cierto', 'puerta', 'arte', 'primer', 'cinturon', 'sur', 'pasto', 'dibujo',  'alimentos', 'avion', 'adjunto', 'aleman', 'posible', 'via', 'ocasion', 'tarde', 'nuevo', 'estar', 'muslo', 'persona', 'alimento', 'pensar', 'golpear', 'club', 'tres', 'final',      'mosca', 'negro', 'fuego', 'bosque', 'oir', 'suelo', 'talon', 'blanco', 'nombre', 'paz',  'viento', 'libro', 'coma', 'razon', 'senador', 'parte', 'fecha', 'cuarto', 'lejano', 'jugar', 'uno', 'lago', 'hoy', 'calor', 'esposa', 'poder', 'ciervo', 'cabo']
    #  'pregunta', 'frontal', 'falso',  'vista',  'buscar', 'diez',  'adulto', 'raiz', 'empeorar', 'jungla', 'gobierno', 'produccion', 'ingles', 'bragas', 'suave', 'tallo', 'enfadarse', 'diarrea', 'rayo', 'oficina', 'corazon', 'area', 'doña', 'hablar', 'sencillo', 'quedarse', 'musculo', 'ayuda', 'central', 'longitud', 'clavo', 'region', 'avance', 'abrir', 'inicio', 'serpiente', 'aceleracion', 'calamar', 'existencia', 'lanzar', 'elogiar', 'busqueda', 'enojo', 'sorpresa', 'avanzar', 'caracol', 'pata', 'nariz', 'tio', 'mi', 'serie', 'animal', 'parlamentario', 'mil', 'compañia', 'afirmar', 'descartar',  'barro', 'subterraneo', 'situacion', 'plantas', 'amigo', 'punto', 'fondo', 'olfato', 'forma', 'morir', 'unico', 'falda', 'extraño', 'bigote', 'buen', 'idioma', 'cabello', 'libertad', 'omnibus', 'aguja', 'particular', 'usar', 'nieve', 'caballero', 'fresco', 'parecer', 'mar', 'trigo', 'pretender', 'piel', 'transcurso', 'informacion', 'voz', 'conseguir', 'politico', 'panel', 'papel', 'interes', 'milenio', 'trafico', 'decreto', 'rural', 'estacion', 'detestar', 'palabra', 'verdura', 'ejemplo', 'tamaño', 'usual', 'separado', 'utilizar', 'sorprenderse', 'comunidad', 'capaz', 'dormir', 'numero', 'coger', 'martes', 'intercambiar', 'reemplazar', 'respuesta', 'experiencia', 'zona', 'lateral', 'bambu', 'interesarse', 'angosto', 'venir', 'señor', 'cansancio', 'medida', 'departamento', 'bicho', 'colores', 'necesario', 'reciente', 'apoyo', 'funcion', 'anciana', 'derecho', 'memoria', 'maloliente', 'de', 'pareja', 'profesion', 'similitud', 'comunicarse', 'coche', 'maquina', 'su', 'salir', 'conocido', 'rata', 'mañana', 'sol', 'sentir', 'solicitud', 'eleccion', 'sustantivos', 'planta', 'apestoso', 'crecer', 'sandia', 'idea', 'mayoria', 'tormenta', 'rojo', 'planeta', 'ministro', 'fuerza', 'recoger', 'uso', 'cercano', 'analisis', 'fuerte', 'expresion', 'atemorizado', 'dictadura', 'oreja', 'oro', 'actividades', 'escuela', 'apetitoso', 'seguir', 'cerebro', 'futuro', 'rana', 'pequeño', 'celeste', 'otro', 'diputado', 'dos', 'dolor', 'serio', 'amiga', 'manga', 'constitucion', 'sujetador', 'boca', 'aspecto', 'real', 'judias', 'placer', 'cuello', 'ir', 'prima', 'prohibicion', 'dejar', 'interrupcion', 'recibir', 'morder', 'atender', 'señora', 'kilo',  'fin', 'intendente', 'tia', 'medir', 'verbos', 'auto', 'cosa', 'reparar', 'lodo', 'comer', 'trabajo', 'siglo', 'alegria', 'hermana', 'guerra', 'tratar', 'pulpo', 'rio', 'medidas', 'electricidad', 'familia', 'clavar', 'espacio', 'significar', 'madre', 'posesivos', 'dios', 'boleto', 'beneficio', 'local', 'imagen', 'inferior', 'encuentro', 'tristeza', 'calidad', 'litro', 'arroz', 'habitacion', 'instituto', 'efecto', 'mejora', 'deterioro',  'acertado', 'cortar', 'puesto', 'mejorar', 'costa', 'superficie', 'pie', 'mediodia', 'regional', 'reunion', 'estudio', 'periodismo', 'perro', 'esposo', 'superior', 'aparecer', 'derecha', 'camiseta', 'viejo', 'norma', 'conejo', 'periodico', 'favor', 'privado', 'comun', 'tarifa', 'cine', 'dinero', 'manual', 'salado', 'vuestro', 'gobernador', 'total', 'orden', 'solo', 'llevar', 'resfriado', 'bomberos', 'empatia', 'existir', 'feliz', 'distinto', 'penultimo', 'vapor', 'cambio', 'marron', 'compacto', 'decidir', 'abdomen', 'encontrar', 'ciencia', 'primera', 'nacion', 'creer', 'cuestion', 'sabado', 'cierre', 'seis', 'ocho', 'miedo', 'actividad', 'inverso', 'pesado', 'horrible', 'cansarse', 'cuervo', 'negar', 'tomar', 'deber', 'mostrar', 'presencia', 'peso', 'agitado', 'sacar', 'traer', 'ordenador', 'espinilla', 'milimetro', 'calcetines', 'crear', 'secreto', 'educacion', 'abstractos', 'capital', 'millon', 'comprar', 'amor', 'ancho', 'solapa', 'desaparecer', 'ser', 'temor', 'autopista', 'babosa', 'mes', 'sensoriales', 'carretera', 'figura', 'cuerpo', 'elemento', 'defensa', 'parada', 'contento', 'hilo', 'formalidad', 'caliente', 'autoridad', 'aburrirse', 'sensaciones', 'joven', 'frio', 'rosa', 'comida', 'religion', 'vivir', 'pais', 'trancar', "fisica", 'escultura', 'terminar', 'unido', 'raro', 'manera', 'uña', 'papas', 'verbo', 'comunicacion', 'mujer', 'actuacion', 'ciento', 'caracteristica', 'secuencia', 'tiempo', 'chino', 'autor', 'causa', 'padre', 'caso', 'escribir', 'solitario', 'analizar', 'siguiente', 'rodilla', 'cansado', 'poblacion', 'municipio', 'durazno', 'bisabuela', 'necesidad', 'bisnieto', 'demanda', 'ver', 'construir',  'enojarse', 'diverso', 'sorprendido', 'pesar', 'obligacion', 'conexion', 'entretenimiento', 'interesado', 'verdad', 'nivel', 'congresista', 'silla', 'sangre', 'caro', 'realidad', 'campo', 'cordon', 'emociones', 'barato', 'diferencia', 'ayudar', 'agua', 'langosta', 'leon', 'rechazar', 'cintura', 'cesped', 'mano', 'numeros', 'posicion', 'democracia', 'izquierda', 'atencion', 'abuela', 'dar', 'solucion', 'escuchar', 'ropa', 'meta', 'lenguaje', 'pantalon', 'sentido', 'kilometro', 'deporte', 'bebe', 'cordones', 'dulce', 'castaño', 'concepto', 'picante', 'admirar', 'decir', 'transporte', 'entre', 'absoluto', 'consecuencia', 'cremallera', 'social', 'semilla', 'destino', 'higado', 'caluroso', 'tu', 'triste', 'largo', 'tema', 'camisa', 'vuestra', 'fabricar', 'policia', 'gas', 'precio', 'chaqueta', 'mundo', 'colegio', 'luna', 'flor', 'retroceso', 'monte', 'carta', 'fuente', 'mover', 'conjunto', 'falta', 'calmo', 'volumen', 'pajaro', 'verde', 'cinco', 'sujetar', 'entender',  'cultura', 'automovil', 'selva', 'tigre', 'patatas', 'escalera', 'altura', 'mundial', 'amar', 'comprender', 'dragon', 'automatico', 'principio', 'dia', 'metalico', 'universo', 'partido', 'acto', 'bolso', 'capacidad', 'marisco', 'individuo', 'violeta', 'tipo', 'informe', 'don', 'labio', 'curso', 'pez', 'otras', 'corte', 'metal', 'valor', 'mentira', 'grueso', 'calendario', 'estilo', 'mariposa', 'niña', 'piso', 'nuestro', 'equipo', 'raton', 'comienza', 'complicar', 'metro', 'duro', 'cuatro', 'hoja', 'lado', 'gran', 'español', 'hielo', 'lugar', 'bueno', 'niño', 'nublado', 'frances', 'romper', 'nieto', 'grande', 'gripe', 'enfado', 'lunes', 'poner', 'cordel']
    noContent = ""
    life = 7
    secretWord = random.choice(words)
    ocultWord = len(secretWord) * "_"

    # dibujo
    clear()
    drawHorca()

    ## juego
    while life != 0:
        # header
        print(f"Score = {score}")
        # print(f"Tienes {life} vidas")
        print(f"Aciertos >> {ocultWord}")
        print(f"No contiene >> {noContent}")

        # win condicion
        if ocultWord.find("_") == -1:
            win = True
            break

        # intento
        intent = str(input("Ingrese su intento: "))

        # comprobacion
        position = secretWord.find(intent)

        if position >= 0:
            print(f"Si esta!!")
            ocultWord = replaceIndexString(ocultWord, position, intent)
        else:
            print("No esta!")
            noContent += intent + ", "
            life -= 1
            if life == 6:
                drawHead()
            elif life == 5:
                drawBody()
            elif life == 4:
                drawLeftHand()
            elif life == 3:
                drawRightHand()
            elif life == 2:
                drawLeftFoot()
            elif life == 1:
                drawRigthFoot()

        wait(1)
        clearConsole()

    if win == True:
        clearConsole()
        print(f"As ganado!!! la palabra era >{secretWord}<")
        print("Score +1")
        score =+ 1
        print(f"Score = {score}")
    else:
        clearConsole()
        print(f"As perdido!!! la palabra era > {secretWord} <")
        print("Puntaje reiniciado!!")
        drawDead()

    ## menu final
    while end2 == 1:
        finalMenu()
        option = str(input("Ingrese una opcion: "))

        if option == "0":
            clearConsole()
            print("Hasta la proxima :D")
            forceEnd = 1
            break
        elif option == "1":
            end = 0
            end2 = 0
        elif option == "2":
            clearConsole()
            print("Los records anteriores: ")
            printScore()
            score += 5
            if score < 4:
                print("Tu score necesita ser igual o mayor a 10 para poder guardarlo (!)")
            else:
                name = str(input("Escribe como quieren que te recuerden: "))
                newScore = (score, name)
                saveScore(newScore)
        else:
            clearConsole()
            print("Error")
            end2 = 1