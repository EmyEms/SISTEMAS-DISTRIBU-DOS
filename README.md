Emilly Eduarda Bitencourt Cardoso - 2210568
---

# CRUD de Login com Flask e MySQL  

API para cadastro e autenticação de usuários usando Flask e MySQL.  

## Requisitos  
- Python 3.x  
- XAMPP (MySQL)  
- Insomnia ou Postman  

## Configuração  

1. Inicie o MySQL no XAMPP.  
2. Acesse `http://localhost/phpmyadmin`.  
3. Crie o banco `crud_python`.  
4. Importe `banco_de_dados.sql`.  

## Instalação  

1. Instale as dependências:  
   ```sh
   pip install -r requirements.txt
   ```
2. Execute o servidor:  
   ```sh
   python app.py
   ```

## Endpoints  

### Criar usuário  
- **POST** `/signup`  
  ```json
  {
    "nome": "Maria",
    "email": "maria@email.com",
    "senha": "123456"
  }
  ```

### Login  
- **POST** `/login`  
  ```json
  {
    "email": "maria@email.com",
    "senha": "123456"
  }
  ```

### Acessar perfil (requer token)  
- **GET** `/perfil`  
  - Header: `Authorization: Bearer SEU_TOKEN`  

## Observações  
- O XAMPP deve estar rodando.  
- O token JWT é necessário para acessar `/perfil`.  
- Se houver erro, verifique as configurações do banco no `app.py`.  
