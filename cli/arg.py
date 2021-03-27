import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Say a simple greeting")

    # required arguments
    parser.add_argument("nombre", type=str)
    parser.add_argument("edad", type=int)

    # optional arguments
    parser.add_argument("--pais", type=str, default="San Panchisco", help="Donde vive esta persona?")

    args = parser.parse_args()
    nombre = args.nombre
    edad = args.edad
    ciudad = args.pais
    print(f"Me llamo {nombre} y tengo {edad} y vivo en {ciudad}")
