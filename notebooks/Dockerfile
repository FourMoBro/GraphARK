FROM jupyter/datascience-notebook

COPY requirements.txt ./
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt
RUN conda install -c conda-forge ta-lib

ENV JUPYTER_ENABLE_LAB=yes


COPY --chown=${NB_UID}:${NB_GID} . /home/jovyan/work
WORKDIR /home/jovyan/work

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--NotebookApp.token=''", "--NotebookApp.password=''", "--port=8888", "--no-browser", "--notebook-dir=/home/jovyan/work", "--allow-root"]