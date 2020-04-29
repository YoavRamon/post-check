FROM python

WORKDIR /post
COPY requirements.txt /post
RUN pip install -r requirements.txt
COPY . /post

ENV PKG="RH080789165GB"
CMD ["/bin/bash"]

# RUN "python3 post-check.py -pn ${pkg}"

