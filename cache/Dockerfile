FROM ubuntu

RUN \  
apt-get update \
&& apt-get install -y build-essential \
&& apt-get install -y wget \
&& wget http://download.redis.io/redis-stable.tar.gz \
&& tar xvzf redis-stable.tar.gz
RUN ls
RUN cd redis-stable
RUN ls
RUN make
