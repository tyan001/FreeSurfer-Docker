FROM ubuntu:22.04

ENV FSLDIR=/usr/local/fsl
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=en_GB.UTF-8

RUN apt update  -y && \
    apt upgrade -y && \
    apt install -y    \
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
      libgomp1

RUN wget https://fsl.fmrib.ox.ac.uk/fsldownloads/fslconda/releases/fslinstaller.py && \
    python3 ./fslinstaller.py -d /usr/local/fsl/ && \
    rm fslinstaller.py

ENV PATH=$FSLDIR/bin:$PATH
ENV FSLOUTPUTTYPE=NIFTI_GZ

# Set the working directory
WORKDIR /workspace

# Set the entrypoint to bash
ENTRYPOINT ["/bin/bash"]

