from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            
            subject, from_email, to = 'Site dev Samuel', 'samueldev2196@gmail.com', email
            text_content = f'{email}'
            html_content = enviar_email_to_cuca(email, raw_password)

            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})



def enviar_email_to_cuca(username, raw_password):
    conteudo = f'''
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>App Cuca</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Poppins" rel="stylesheet">
        </head>
        <title>E-mail cuca</title>
        <body>
            <div class="container" style="background-color: #023E73; height: 330px; border-radius: 26px;">
                <center>
                    <div>
                        <img height="120" src="/static/img/logo.png" alt="">
                    </div>
                    <div style="margin-top: 20px; color: white;">
                        <h2>Bem vindo ao seu controle de estoque!</h2>
                    </div>
                    <h3 style="color: white;">
                        Seu usuário é: {username}
                    </h3>
                    <h3 style="color: white;">
                        Sua senha é: {raw_password}
                    </h3>
                </center>
            </div>
        </body>
    </html>'''

    return conteudo
