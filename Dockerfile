FROM ubuntu:20.04
RUN apt-get update && apt-get -y install \
    python3 python3-dev python3-pip wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

WORKDIR /app
COPY . ./
RUN pip3 install -r requirements.txt
RUN clean compile package
CMD java -jar ./target/SinglePageFullHtml-1.0-SNAPSHOT-jar-with-dependencies.jar https://www.example.com/
