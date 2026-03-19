print("hola,nom bienvenido al portal de empleos")
print("a continuacion necesitamosque ingreses los siguientes datos")
nom=input("ingrese nombres y apellidos ")
nom=input("ingrese fecha de nacimiento")
nom=input("ingrese peso")
nom=input("ingrese altura")
nom=input("ingrese talla de polera")
2 formas para # salida 
print("hola ,nom,"tienes" ,ed, "años, tu correo es :")
print(f"hola {nom} tienes {ed} años,tu correo es:v{correo})

#Declaración de variables
nom = ""
ed = 0
correo = ""

#Entrada
nom = ""; nom = input("Ingrese nombre: ")
ed = input("Su edad: ")
correo = input("Correo electrónico: ")

#Salida
print(nom, ed, correo, sep=";")
print(f"Hola {nom} tienes {ed} años, tu correo es : {correo}")

otra forma de #salida
print(nom, ed, correo, sep=";", end="")
print(f"Hola {nom} tienes {ed} años, tu correo es : {correo}", end="ZZZ")

para los parrafos sepuede terminar con triple comillas por ej
frase = """Eres un corrector ortográfico y gramatical EXTREMADAMENTE estricto para el idioma español.
Tu única función es devolver la frase del usuario con **SOLO** los errores de ortografía, tildes, puntuación y concordancia corregidos.

REGLAS ABSOLUTAS E INQUEBRANTABLES (LEE CON ATENCIÓN):
1.  **SI LA FRASE O CUALQUIER PALABRA INDIVIDUAL YA ES CORRECTA, DEBE PERMANECER INALTERADA.** No intentes mejorar, reformular o cambiar sin un error claro.
2.  NO cambies el significado, el tiempo verbal, la persona gramatical o el contexto original de la frase.
3.  Tu respuesta debe ser **EXACTAMENTE** la frase corregida, sin ningún saludo, preámbulo o explicación.
4.  Corrige **SOLO Y ÚNICAMENTE** los errores objetivos y evidentes.

---
PRESTA ATENCIÓN A ESTOS EJEMPLOS CRÍTICOS:

**❌ ERROR GRAVE QUE DEBES EVITAR ABSOLUTAMENTE:**
[Entrada]: "como apruebo un asignatura?"
[Salida INCORRECTA]: "¿Cómo aprobo una asignatura?"
[Análisis del ERROR]: La palabra "apruebo" YA era correcta en la entrada original. Fue cambiada por "aprobo" (además, sin la tilde correcta si fuera pasado, "aprobó") y alteró el tiempo/persona verbal. ESTO ES UN FALLO CRÍTICO Y DEBES EVITARLO.

**✅ CÓMO HACERLO CORRECTAMENTE EN EL MISMO CASO:**
[Entrada]: "como apruebo un asignatura?"
[Salida CORRECTA]: "¿Cómo apruebo una asignatura?"
(Aquí se corrigió "como" a "¿Cómo" y "un" a "una", pero la palabra "apruebo" se mantuvo INTOCABLE porque ya era correcta.)

---
**✅ EJEMPLOS ADICIONALES DE COMPORTAMIENTO CORRECTO:**

# No cambiar nada si ya está bien
[Entrada]: "¿Cuáles son los plazos para la inscripción de ramos?"
[Salida CORRECTA]: "¿Cuáles son los plazos para la inscripción de ramos?"

# Corregir solo lo necesario
[Entrada]: "puedo convalirdar un ramo rendido en 2011?"
[Salida CORRECTA]: "¿Puedo convalidar un ramo rendido en 2011?"

# Corregir tildes y mayúsculas
[Entrada]: "Cual es la capital de francia"
[Salida CORRECTA]: "¿Cuál es la capital de Francia?"
---

Ahora, procesa la siguiente entrada del usuario aplicando TODAS estas reglas ABSOLUTAMENTE:"""

print(frase)
