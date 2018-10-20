from src.app import create_app

if __name__ == '__main__':
    sio, app = create_app()
    port_number = app.config["APP_PORT"]
    development_mode = app.config.get("DEVELOPMENT", False)

    print('--- Starting Web and Socket Server on port {} ---'.format(port_number))
    sio.run(app, port=port_number, host="0.0.0.0", debug=development_mode)
