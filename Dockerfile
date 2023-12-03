# Usar a imagem base do Jupyter com SciPy (que inclui Python e ferramentas científicas)
FROM jupyter/scipy-notebook

# Definir o usuário root para instalação de pacotes
USER root

# Instalar dependências essenciais para o ambiente SQL (ajuste conforme necessário)
RUN apt-get update && \
    apt-get install -y libpq-dev && \
    apt-get autoclean -y && \
    apt-get autoremove -y 

# Mudar de volta para o usuário do notebook

RUN docker run -p 8888:8888 beakerx/beakerx

USER $NB_UID

EXPOSE 8888

# Iniciar o JupyterLab
CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''"]
