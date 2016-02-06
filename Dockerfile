FROM        python:3
MAINTAINER  Paul R. Tagliamonte <paultag@debian.org>

RUN apt-get update && apt-get install -y \
    git \
    node-uglify \
    coffeescript

RUN mkdir -p /opt/pault.ag/
ADD . /opt/pault.ag/mandelbrot/

RUN cd /opt/pault.ag/mandelbrot; python3 /usr/local/bin/pip install -r requirements.txt

RUN make -C /opt/pault.ag/mandelbrot/

RUN mkdir -p /mandelbrot/
WORKDIR /mandelbrot/

CMD ["python3", "manage.py"]
