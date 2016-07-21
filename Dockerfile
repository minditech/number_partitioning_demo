FROM ubuntu:16.04
RUN apt-get update && \
    apt-get install -y python
COPY printer.py /bin/printer.py
RUN chmod 755 /bin/printer.py
ENTRYPOINT ["/bin/printer.py"]
