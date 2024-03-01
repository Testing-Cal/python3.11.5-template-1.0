FROM python:3.11.5

COPY . .

RUN pip3 install Flask

ENV context /

ENV port 7076
                                                                         
CMD [ "python3", "./main.py" ]

