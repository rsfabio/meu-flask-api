from flask import Flask, render_template
from flask_migrate import Migrate

from database import db
from usuarios import bp_usuarios
from login import bp_login # importa a blueprint de login

app = Flask(__name__)
#1db.init_app(app)
#1conexao = "sqlite:///meubanco.sqlite"

#2app.config['SECRET_KEY'] = 'minha-chave'
#1app.config['SQLALCHEMY_DATABASE_URI'] = conexao
#1app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
#2app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.sqlite'
#2app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Dados de conexão do Supabase
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.bpliaykiuaqtokvuejwc:meubanco@aws-0-sa-east-1.pooler.supabase.com:6543/postgres'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'minha-chave'

# Depois você inicializa o banco
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(bp_usuarios, url_prefix='/usuarios')
app.register_blueprint(bp_login) # registra a blueprint


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
