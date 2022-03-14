
# Este projeto foi feito com:
Python 3.10.2 <br>
Django 4.0.2
Django-Rest-Framework 3.13.1

## Descrição do projeto
 Back-end do site costs feito com Django-Rest-Framework, verifique o front-end também <a href="https://github.com/Simeone-Holanda/costs-front-end">Aqui</a>. 

## Como rodar o projeto?

- Clone esse repositório. <br>
- Crie um virtualenv com Python.<br>
- Ative o virtualenv(O caminho pode variar dependendo do sistema operacional).<br>
- Instale as dependências.<br>
- Rode as migrações.<br>

## Siga os comandos abaixo para que tudo ocorra normalmente

    git clone https://github.com/Simeone-Holanda/costs-back-end 

    cd costs-back-end

    python -m venv venv

    source venv/bin/activate No Linux

    source venv/Scripts/activate - No Windows(com o git bash)

    pip install -r requirements.txt 

    python manage.py migrate 

    python manage.py runserver 
    
    acesse a rota: http://127.0.0.1:8000/categories/
    
    faça um post para as categorias que você deseja ter no projeto, aqui uma sugestão das usadas no vídeo infra, desenvolvimento, design, planejamento.
    
 

<br>
Feito com muito esforço por Simeone Holanda, espero que gostem. 
