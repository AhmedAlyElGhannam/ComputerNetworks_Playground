# use ubuntu focal as base image
FROM ubuntu:focal

# set user as root
USER root

# update and upgrade packages
RUN apt update 
RUN apt upgrade -y

# install ping for debugging network
RUN apt install inetutils-ping -y

# install dnsutils to know the ip of other containers
RUN yes "1" | apt install dnsutils -y

# set default shell (login as root && launch an INTERACTIVE SHELL)
SHELL ["/bin/bash", "--login", "-i", "-c"]

# install python2 to run the labs
RUN apt install python3 -y

# install pip
RUN apt install python3-pip -y

# change current working directory to /
WORKDIR /

# copy tcp && udp server python scripts
COPY . .

# prevent container from exiting by keeping it running in the background
CMD exec "$@"