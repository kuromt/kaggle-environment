FROM jupyter/datascience-notebook:python-3.7.6

COPY requirement.txt /home/jovyan/
COPY custom.css /home/jovyan/.jupyter/custom/
RUN pip install -r /home/jovyan/requirement.txt

CMD ["start-notebook.sh"]


