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

RUN conda create -y -n beakerx 'python>=3'
RUN source activate beakerx
RUN conda config --env --add pinned_packages 'openjdk>8.0.121'
RUN conda install -y -c conda-forge ipywidgets beakerx
USER $NB_UID

EXPOSE 8888

# Iniciar o JupyterLab
CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''"]
