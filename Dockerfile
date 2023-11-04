FROM ubuntu

RUN apt-get update -y && apt-get install -y \
    python3 \
    python3-pip

RUN pip3 install pandas numpy matplotlip seaborn scikit-learn scipy

WORKDIR /home/doc-bd-a1

EXPOSE 8080

CMD [ "bash" ]






 