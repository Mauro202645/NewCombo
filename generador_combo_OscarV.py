import random
import os
import datetime
import re

# ============================
# COLORES Y ESTILO
# ============================

VERDE = "\033[92m"
AZUL = "\033[94m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# ============================
# BANNER
# ============================

def banner():
    os.system("clear" if os.name != "nt" else "cls")
    print(VERDE + r"""

████████████████████████████████████
█─▄▄─█─▄▄▄▄█─▄▄▄─██▀▄─██▄─▄▄▀█▄─█─▄█
█─██─█▄▄▄▄─█─███▀██─▀─███─▄─▄██▄▀▄██
▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▀▀▀
    """ + RESET)
    print(VERDE + "             ✨ GENERADOR OscarV ✨\n" + RESET)

# ============================
# BASE DE DATOS
# ============================

NOMBRES = [
    "Gabriel","Geovanny","Grover","Guillermo","Hugo","Ironpilot","Jaime","James",
    "Javier","Jennifer","Jhoan","Jimmy","Johann","Jois","Jorge","Juan","Juancito",
    "Karina","Kim","Limber","Luis","Manuel","Marcio","Marina","Marivel","Marlon",
    "Marta","Monica","Nina","Norma","Orlando","Paialfre","Paul","Richard","Roman",
    "Sandra","Santiago","Sebastian","Sergio","Tony","Tribio","Valentin"
]

APELLIDOS = [
    "Cunachi","Marcillo","Chay","Iza","Tapia","Velis","Caseres","Perez","Gonzalez",
    "Dobbertin","Lacruz","Orre","Mutis","Cardone","Hurtado","Salazar","Sanchez",
    "Retamal","Ang","Pae","Bedoya","Garcia"
]

DOMINIOS = [
    "gmail.com","hotmail.com","yahoo.com","outlook.com","proton.me","icloud.com",
    "gmx.com","yandex.com","latinmail.com","terra.com","movistar.com.pe",
    "claro.com.pe","speedy.com.pe"
]

SUFIJOS_ESPECIALES = ["IPTVCLUB", "IPTV", "TV", "MAMA"]

# ============================
# BASE REAL (PEGA AQUÍ TODA TU LISTA)
# ============================

BASE_REAL = [
    "56990745516pro:110224pro",
    "56996752036playtv:010624play",
    "0000781:12345678",
    "001Latin001:3KRgRX3zP9",
    "Abigail2024:Abigail2024",
    "VIP015451747996424462:61ae7dde609f",
    "08072024LC:08072024LC",
    "estebanrojascarrasco@gmail.com:ydgs67d67d98",
    # 👉 Aquí pegas TODA tu base completa, línea por línea, tal como la tienes
]

# ============================
# FUNCIONES BASE
# ============================

def crear_carpeta():
    ruta = "/sdcard/CombosOscarV"
    if not os.path.exists(ruta):
        os.makedirs(ruta)
    return ruta

def rand_hex():
    return ''.join(random.choice("0123456789abcdef") for _ in range(14))

def rand_str(n=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(chars) for _ in range(n))

def fecha_random():
    d = random.randint(1,28)
    m = random.randint(1,12)
    a = random.randint(2018,2026)
    return f"{d:02d}{m:02d}{a}"

# ============================
# PATRONES AVANZADOS
# ============================

def p_nombre_4dig():
    n = random.choice(NOMBRES)
    return f"{n}{random.randint(1000,9999)}"

def p_nombre_apellido():
    return random.choice(NOMBRES) + random.choice(APELLIDOS)

def p_nombre_apellido_ano():
    return random.choice(NOMBRES) + random.choice(APELLIDOS) + str(random.randint(2020,2026))

def p_inicial_apellido_num():
    n = random.choice(NOMBRES)
    a = random.choice(APELLIDOS)
    return n[0] + a + str(random.randint(10,999))

def p_nombre_apellido_fecha():
    return random.choice(NOMBRES) + fecha_random()

def p_nombre_num():
    return random.choice(NOMBRES) + str(random.randint(10,999))

def p_nombre_punto_inicial():
    n = random.choice(NOMBRES)
    return f"{n}.{n[0]}"

def p_nombre_ano():
    n = random.choice(NOMBRES)
    return f"{n}{random.randint(2020,2026)}"

def p_nombre_sufijo():
    return random.choice(NOMBRES) + random.choice(SUFIJOS_ESPECIALES)

def p_nombre_apellido_num():
    return random.choice(NOMBRES) + random.choice(APELLIDOS) + str(random.randint(10,999))

def p_random_mayus_minus():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(random.choice(chars) for _ in range(random.randint(6,12)))

def p_random_complejo():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(chars) for _ in range(random.randint(10,14)))

# ============================
# GENERADORES DE PASSWORD
# ============================

def pass_hex():
    return rand_hex()

def pass_random():
    return rand_str(12)

def pass_nombre_ano():
    n = random.choice(NOMBRES)
    return f"{n}{random.randint(2020,2026)}"

def pass_nombre_num():
    n = random.choice(NOMBRES)
    return f"{n}{random.randint(10,999)}"

def pass_iniciales_ano():
    n = random.choice(NOMBRES)
    a = random.choice(APELLIDOS)
    return f"{n[0]}{a[0]}{random.randint(2020,2026)}"

def pass_fecha():
    return fecha_random()

def pass_random_corto():
    return rand_str(8)

def pass_random_largo():
    return rand_str(14)

PASSWORD_STYLES = [
    pass_hex, pass_random, pass_nombre_ano, pass_nombre_num,
    pass_iniciales_ano, pass_fecha, pass_random_corto, pass_random_largo
]

# ============================
# SUPER CATEGORÍAS
# ============================

# 1) Nombres reales
REAL_PATTERNS = [
    p_nombre_4dig, p_nombre_apellido, p_nombre_apellido_ano,
    p_inicial_apellido_num, p_nombre_apellido_fecha, p_nombre_num,
    p_nombre_punto_inicial, p_nombre_ano
]

# 2) IPTVCLUB / profesionales
IPTV_PATTERNS = [
    p_nombre_sufijo, p_nombre_apellido_ano, p_nombre_apellido_num
]

# 3) Random fuertes
RANDOM_PATTERNS = [
    p_random_mayus_minus, p_random_complejo
]

# 4) Mixtos (todos)
ALL_PATTERNS = REAL_PATTERNS + IPTV_PATTERNS + RANDOM_PATTERNS

# ============================
# DETECCIÓN DE PATRONES EN BASE REAL
# ============================

def detectar_patron(user):
    # Teléfonos con sufijo (Chile)
    if re.match(r"^569\d{7,8}[a-zA-Z]+$", user):
        return "telefono_sufijo"

    # Teléfonos sin sufijo
    if re.match(r"^569\d{7,8}$", user):
        return "telefono"

    # VIP codes
    if user.startswith("VIP") and re.match(r"^VIP\d+$", user):
        return "vip"

    # Nombre + año
    if re.match(r"^[A-Za-z]+20\d{2}$", user):
        return "nombre_ano"

    # Nombre + números
    if re.match(r"^[A-Za-z]+\d+$", user):
        return "nombre_num"

    # Texto + punto + texto + números
    if re.match(r"^[A-Za-z0-9]+\.[A-Za-z0-9]+\d+$", user):
        return "mixto_punto"

    # Random alfanumérico
    if re.match(r"^[A-Za-z0-9]{8,14}$", user):
        return "random"

    # Hexadecimal
    if re.match(r"^[0-9a-f]{10,16}$", user):
        return "hex"

    # Email
    if "@" in user:
        return "email"

    # Default
    return "otro"

def variar_user(user):
    patron = detectar_patron(user)

    if patron == "telefono_sufijo":
        base = "569" + str(random.randint(1000000, 99999999))
        sufijo = re.findall(r"[a-zA-Z]+$", user)[0]
        return base + sufijo

    if patron == "telefono":
        return "569" + str(random.randint(1000000, 99999999))

    if patron == "vip":
        return "VIP" + str(random.randint(100000000000, 999999999999))

    if patron == "nombre_ano":
        nombre = re.findall(r"[A-Za-z]+", user)[0]
        return nombre + str(random.randint(2020, 2026))

    if patron == "nombre_num":
        nombre = re.findall(r"[A-Za-z]+", user)[0]
        return nombre + str(random.randint(10, 99999))

    if patron == "mixto_punto":
        parte1 = rand_str(4)
        parte2 = rand_str(5)
        return f"{parte1}.{parte2}{random.randint(10,9999)}"

    if patron == "random":
        return rand_str(random.randint(8, 14))

    if patron == "hex":
        return rand_hex()

    if patron == "email":
        nombre = rand_str(6).lower()
        dominio = random.choice(DOMINIOS)
        return f"{nombre}@{dominio}"

    return rand_str(10)

# ============================
# GENERADORES ESPECIALES BASE REAL
# ============================

def generar(patterns, cantidad):
    combos = []
    for _ in range(cantidad):
        user = random.choice(patterns)()
        password = random.choice(PASSWORD_STYLES)()
        combos.append(f"{user}:{password}")
    return combos

def generar_base_real(cantidad):
    combos = []
    for _ in range(cantidad):
        combos.append(random.choice(BASE_REAL))
    return combos

def generar_variaciones_base_real(cantidad):
    combos = []
    for _ in range(cantidad):
        user_real, password_real = random.choice(BASE_REAL).split(":", 1)
        nuevo_user = variar_user(user_real)
        nuevo_pass = random.choice(PASSWORD_STYLES)()
        combos.append(f"{nuevo_user}:{nuevo_pass}")
    return combos

# ============================
# GUARDAR
# ============================

def guardar(combos):
    carpeta = crear_carpeta()
    nombre = f"combos_{datetime.datetime.now().strftime('%d%m%Y_%H%M%S')}.txt"
    ruta = os.path.join(carpeta, nombre)

    with open(ruta, "w", encoding="utf-8") as f:
        f.write("=== COMBOS GENERADOS POR OscarV ===\n")
        for c in combos:
            f.write(c + "\n")

    print(VERDE + f"\n📁 Archivo guardado en: {ruta}\n" + RESET)

# ============================
# MENÚ
# ============================

def menu():
    while True:
        banner()
        print(AMARILLO + "Seleccione una SUPER CATEGORÍA:\n" + RESET)
        print("1️⃣  Nombres reales (muy parecido a tus ejemplos)")
        print("2️⃣  IPTVCLUB / profesionales")
        print("3️⃣  Random fuertes")
        print("4️⃣  Mixtos (todos los patrones)")
        print("5️⃣  Base REAL (users:password reales)")
        print("6️⃣  Variaciones basadas en BASE REAL")
        print("7️⃣  Salir ❌")

        op = input("\n👉 Opción: ").strip()

        if op == "7":
            print(ROJO + "\nSaliendo... 👋\n" + RESET)
            break

        if op not in ["1","2","3","4","5","6"]:
            print(ROJO + "\n❌ Opción inválida\n" + RESET)
            input("ENTER para continuar...")
            continue

        try:
            cantidad = int(input("\n¿Cuántos combos desea generar?: "))
        except:
            print(ROJO + "\n❌ Número inválido\n" + RESET)
            input("ENTER para continuar...")
            continue

        print(VERDE + "\n⚙️ Generando combos...\n" + RESET)

        if op == "1":
            combos = generar(REAL_PATTERNS, cantidad)
        elif op == "2":
            combos = generar(IPTV_PATTERNS, cantidad)
        elif op == "3":
            combos = generar(RANDOM_PATTERNS, cantidad)
        elif op == "4":
            combos = generar(ALL_PATTERNS, cantidad)
        elif op == "5":
            combos = generar_base_real(cantidad)
        elif op == "6":
            combos = generar_variaciones_base_real(cantidad)

        guardar(combos)
        input(AMARILLO + "ENTER para volver al menú..." + RESET)

# ============================
# EJECUTAR
# ============================

if __name__ == "__main__":
    menu()