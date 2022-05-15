FROM python:3.10

WORKDIR /user/src/app

COPY './requirements.txt' .

RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y libsndfile1-dev
RUN apt-get update && apt-get install -y ffmpeg

EXPOSE 8501

COPY . .

ENTRYPOINT [ "streamlit", "run" ]

CMD ["app.py"]