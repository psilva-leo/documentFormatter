# DocumentFormatter

Este projeto visa a implementação de um sistema para formatação de arquivo .json.


### Prerequisitos

Para utilizar o sistema é necessário ter o Docker instalado ou realizar a instalação manual dos requisitos Python.

Caso não seja utilizado o Docker, os requisitos se encontram em requirements.txt e podem ser instalado utilizando:
```
pip install -r requirements.txt
```

### Installing

Utilizando o docker, basta utilizar o seguintes comandos para rodar o sistema:

```
docker build -t document-formatter .
docker run -p 8080:8080 document-formatter
```

## Authors

* **Leonardo Silva**
* **Andre Perez**
* **Vitor Yoshida**
* **Daniel Caires**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
