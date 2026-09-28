import random
import unicodedata


def normalizar_texto(texto):
    """Elimina tildes, caracteres especiales y convierte a minúsculas."""
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto.lower()


def generar_nombre_usuario(nombre, primer_apellido, segundo_apellido=None):
    """Genera un usuario según un formato aleatorio."""
    n = normalizar_texto(nombre)
    p = normalizar_texto(primer_apellido)
    s = normalizar_texto(segundo_apellido) if segundo_apellido else ""

    # Formatos de ejemplo:
    # 1: Inicial + Primer apellido (ej: jcolque)
    # 2: Inicial + Punto + Primer apellido (ej: j.colque)
    # 3: Nombre completo pegado (ej: josecondorizambrana)
    formatos = [
        f"{n[0]}{p}",
        f"{n[0]}.{p}",
        f"{n}{p}{s}" if s else f"{n}{p}",
    ]

    return random.choice(formatos)


def generar_lista_usuarios(nombres, apellidos, cantidad=1000):
    """Genera una lista aleatoria de usuarios."""
    usuarios = set()

    while len(usuarios) < cantidad:
        nombre = random.choice(nombres)
        primer_ap = random.choice(apellidos)
        segundo_ap = random.choice(apellidos)

        # Evitamos repetición de apellidos
        while segundo_ap == primer_ap:
            segundo_ap = random.choice(apellidos)

        usuario = generar_nombre_usuario(nombre, primer_ap, segundo_ap)
        usuarios.add(usuario)
    return list(usuarios)

# Listas de datos base
nombres_base = [
    "adrian",
    "alejandro",
    "sergio",
    "valeria",
    "vanessa",
]

apellidos_base = [
    "aguilar",
    "alcocer",
    "aramayo",
    "arce",
    "arias",
    "zoto",
]


# Generar 10 usuarios aleatorios
lista_usuarios = generar_lista_usuarios(
    nombres_base, apellidos_base, cantidad=1000
)

for u in lista_usuarios:
    print(u)
