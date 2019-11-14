# DocumentFormatter

Este projeto visa a implementação de um sistema para formatação de arquivo .json.


### Prerequisitos

Para utilizar o sistema é necessário ter o Docker instalado ou realizar a instalação manual dos requisitos Python.

Caso não seja utilizado o Docker, os requisitos se encontram em requirements.txt e podem ser instalado utilizando:
```
pip install -r requirements.txt
```

### Installing

Utilizando o docker, basta utilizar o seguintes comandos para rodar o sistema em http://localhost:8080

```
docker build -t document-formatter .
docker run -p 8080:8080 document-formatter
```

### Desenvolvimento

Para desenvolver utiliza-se uma instância de debug do Flask (app.py). Ao rodar o comando abaixo, uma instância do Flask 
é inicializada em http://localhost:8000

```
python app.py
```


## Authors

* **Leonardo Silva**
* **Andre Perez**
* **Vitor Yoshida**
* **Daniel Caires**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
