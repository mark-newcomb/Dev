FROM alpine:latest
WORKDIR /app

COPY ./target/dist/pybuilder_project-1.0.dev0/dist/pybuilder_project-1.0.dev0.tar.gz .

RUN apk add bash
RUN apk add pipx
RUN apk add python3


# docker build -t <tagname> .
# docker run -it <tag>
# docker push <username/image-name>
