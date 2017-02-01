FROM ubuntu

RUN apt-get -qq update

RUN apt-get -qq -y install \
libauthen-ntlm-perl \
libcrypt-ssleay-perl \
libdigest-hmac-perl \
libfile-copy-recursive-perl \
libio-compress-perl \
libio-socket-inet6-perl \
libio-socket-ssl-perl \
libio-tee-perl \
libmodule-scandeps-perl \
libnet-ssleay-perl \
libpar-packer-perl \
libreadonly-perl \
libterm-readkey-perl \
libtest-pod-perl \
libtest-simple-perl \
libunicode-string-perl \
liburi-perl \
libssl-dev \
make \
gcc \
cpanminus \
git \
vim

RUN cpanm -q Mail::IMAPClient
RUN cpanm -q Data::Uniqid
RUN cpanm -q Test::MockObject
RUN cpanm -q JSON::WebToken
RUN cpanm -q Crypt::OpenSSL::RSA
RUN cpanm -q LWP

RUN git clone https://github.com/imapsync/imapsync.git /home/imapsync

RUN ln -s /home/imapsync/imapsync /usr/local/sbin
