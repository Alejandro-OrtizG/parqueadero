from controllers.controlador import iniciar_app

def main():
    try:
        print("Iniciando Sistema de Parqueadero")
        iniciar_app()
    except (KeyboardInterrupt, EOFError):
        print("\nGracias por usar el parqueadero")
        print("Adiós")


if __name__ == "__main__":
    main()