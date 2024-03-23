FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install \
    python3 python3-dev python3-pip wget curl zip unzip
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install
RUN curl -s 'https://get.sdkman.io' | bash
RUN /bin/bash -c "source $HOME/.sdkman/bin/sdkman-init.sh; sdk version; sdk install java 8.0.241-open; sdk install maven 3.6.3"
WORKDIR /app
COPY . ./
RUN pip3 install -r requirements.txt
RUN mvn clean compile package
CMD java -jar ./target/SinglePageFullHtml-1.0-SNAPSHOT-jar-with-dependencies.jar https://www.example.com/
