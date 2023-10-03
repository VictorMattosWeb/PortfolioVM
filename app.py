from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from config import email, senha 

app = Flask(__name__)
app.secret_key = 'vhmattos'


''' Config email '''
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha
}

''' Placing mail_settings within our app settings '''
app.config.update(mail_settings)
mail = Mail(app)

class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome,
        self.email = email,
        self.mensagem = mensagem


''' Main route '''
@app.route('/')
def index():
    return render_template('index.html')

''' Route send '''
@app.route('/send', methods=['GET', 'SET'])
def send():
    #Instantiating my form
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )
        #Placing message data in the form
        msg = Message(
            subject = f'{formContato.nome} te enviou uma mensagem no portfólio',
            sender = app.config.get("MAIL_USERNAME"),
            recipients= ['victorcontato109@gmail.com', app.config.get("MAIL_USERNAME")],
            body = f''' 

            {formContato.nome} com o e-mail {formContato.email}, te enviou a seguinte mensagem:

            {formContato.mensagem}

            '''
        )

        #Send message
        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)