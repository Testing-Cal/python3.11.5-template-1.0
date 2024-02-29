FROM python:3.12.2

COPY . .

RUN pip3 install Flask

ENV context /

ENV port 7076
                                                                         
CMD [ "python3", "./main.py" ]

