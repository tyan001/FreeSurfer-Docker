FROM ubuntu:jammy

ENV FSLDIR=/usr/local/fsl
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=en_GB.UTF-8

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y    \
    r-base          \
    r-base-dev      \
    python3         \
    python3-pip     \
    wget            \
    file            \
    dc              \
    mesa-utils      \
    pulseaudio      \
    libquadmath0    \
    libgtk2.0-0     \
    firefox         \
    libosmesa6      \
    libosmesa6-dev  \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    xvfb            \
    libgomp1     && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://fsl.fmrib.ox.ac.uk/fsldownloads/fslconda/releases/fslinstaller.py && \
    python3 ./fslinstaller.py -d /usr/local/fsl/ && \
    rm fslinstaller.py

ENV PATH=$FSLDIR/bin:$PATH
ENV FSLOUTPUTTYPE=NIFTI_GZ


# Set working directory
WORKDIR /workspace

# Set the entrypoint to bash
ENTRYPOINT ["/bin/bash"]

