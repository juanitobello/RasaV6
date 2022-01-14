FROM tensorflow/tensorflow:2.2.0
RUN mkdir -p /rasa_app
WORKDIR /rasa_app
COPY . /rasa_app
RUN python -m pip install -U pip
RUN pip3 install -r requirements.txt
#RUN pip3 install --user rasa-nlu==0.14.0
#RUN pip3 install --user rasa-core==0.13.2
RUN python -m spacy download es
RUN pip3 install --user rasa==2.7.2
RUN pip3 install --user sanic==20.6.0
EXPOSE 5000
