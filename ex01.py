from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

usuarios = {
    "joao": "123",
    "maria": "abc",
}

musicas = {
    "joao": [],
    "maria": []
}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        if usuario in usuarios and usuarios[usuario] == senha:
            session['usuario'] = usuario
            return redirect(url_for('dashboard'))
        else:
            flash('Usuário ou senha inválidos!')
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'usuario' in session:
        return render_template('dashboard.html', usuario=session['usuario'])
    
    return redirect(url_for('login'))

@app.route('/musicas', methods=['GET', 'POST'])
def gerenciar_musicas():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    usuario = session['usuario']
    lista = musicas[usuario]

    if request.method == 'POST':
        nova_musica = request.form.get('musica')
        if nova_musica:
            lista.append(nova_musica)

    busca = request.args.get('busca')
    if busca:
        lista_filtrada = [m for m in lista if busca.lower() in m.lower()]
    else:
        lista_filtrada = lista

    return render_template('musicas.html', musicas=lista_filtrada, busca=busca, usuario=usuario)


@app.route('/remover/<int:index>')
def remover_musica(index):
    if 'usuario' in session:
        usuario = session['usuario']
        if 0 <= index < len(musicas[usuario]):
            del musicas[usuario][index]
    
    return redirect(url_for('gerenciar_musicas'))


@app.route('/editar/<int:index>', methods=['GET', 'POST'])
def editar_musica(index):
    if 'usuario' not in session:
        return redirect(url_for('login'))

    usuario = session['usuario']
    lista = musicas[usuario]

    if request.method == 'POST':
        nova_musica = request.form['nova_musica']
        if 0 <= index < len(lista):
            lista[index] = nova_musica
        return redirect(url_for('gerenciar_musicas'))

    return render_template('editar.html', musica=lista[index], index=index)

if __name__ == '__main__':
    app.run(debug=True)
