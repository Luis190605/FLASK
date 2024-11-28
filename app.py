from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración del correo
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'luisantoniocastillotrujillo@gmail.com'  # Nuevo correo personal
app.config['MAIL_PASSWORD'] = 'pscy zmmj xptj taeq'  # Contraseña de aplicación generada
app.config['MAIL_DEFAULT_SENDER'] = 'luisantoniocastillotrujillo@gmail.com'
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Enviar correo
        msg = Message(subject="Nuevo mensaje de contacto",
                      sender=email,
                      recipients=["luisantoniocastillotrujillo@gmail.com"])  # Cambiado al nuevo correo
        msg.body = f"Nombre: {name}\nCorreo: {email}\nMensaje:\n{message}"
        mail.send(msg)
        
        return render_template('contact.html', submitted=True, name=name)
    
    return render_template('contact.html', submitted=False)

if __name__ == '__main__':
    app.run(debug=True)


