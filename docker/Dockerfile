FROM kalilinux/kali-rolling
ARG DEBIAN_FRONTEND=noninteractive
# Cập nhật và cài đặt các gói cơ bản
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    ltrace \
    libc6-i386 \
    gcc-multilib \
    g++-multilib \
    build-essential \
    file \
    patch \
    curl \
    wget \
    bash \
    git \
    openssh-client \
    procps \
    netbase \
    dirmngr \
    gnupg \
    libssl-dev \
    gdb \
    gdbserver \
    strace \
    vim \
    upx \
    poppler-utils \
    netcat-traditional \
    bsdmainutils \
    sshpass \
    zsh \
    nasm \
    nano \
    openssh-server \
    python3 \
    python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Cài đặt pip và các công cụ bổ sung
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir unicorn pwntools ropper pyasn1 Pillow bitarray pycrypto

# Cài đặt các công cụ phân tích
RUN mkdir -p /opt/tools && \
    git clone --depth 1 https://github.com/longld/peda.git /opt/tools/peda && \
    git clone --depth 1 https://github.com/hugsy/gef.git /opt/tools/gef && \
    git clone --depth 1 https://github.com/gdbinit/Gdbinit /opt/tools/Gdbinit && \
    git clone --depth 1 https://github.com/pwndbg/pwndbg /opt/tools/pwndbg && \
    git clone --depth 1 https://github.com/slimm609/checksec.sh /opt/tools/checksec.sh && \
    ln -rsf /opt/tools/checksec.sh/checksec /usr/local/bin/checksec && \
    git clone --depth 1 https://github.com/wapiflapi/villoc.git /opt/tools/villoc && \
    ln -rsf /opt/tools/villoc/villoc.py /usr/local/bin/villoc

# Tạo người dùng và cài đặt cấu hình
RUN useradd -m -s /bin/bash seed && \
    echo "root:dees" | chpasswd && \
    echo "seed:dees" | chpasswd && \
    usermod -aG sudo seed

# Tạo thư mục làm việc và cấu hình gdb
USER seed
WORKDIR /home/seed

RUN git clone https://github.com/longld/peda.git ~/peda && \
    echo "source ~/peda/peda.py" >> ~/.gdbinit

# The command executed by the container after startup
CMD [ "/bin/bash"]
