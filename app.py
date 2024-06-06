from app import create_app
import os

print("DATABASE_URL:", os.getenv('DATABASE_URL'))  # Verificar o valor da variável de ambiente

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
