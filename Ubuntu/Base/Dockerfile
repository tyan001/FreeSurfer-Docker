FROM ubuntu:jammy

# This Dockerfile makes a FreeSurfer 7.4.1 image using Ubuntu 22.04.
# You would need to get the Ubuntu 22.04 image from Dockerhub.
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        bc \
        libgomp1 \
        perl \
        procps \
        tar \
        tcsh \
        wget \
        vim-common \
        libgl1-mesa-glx \
        libxext6 \
        libsm6 \
        libxrender1 \
        libxmu6 \
        python3 \
        python3-pip \
        curl \
        unzip \
        gfortran && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

RUN wget --progress=bar:force:noscroll --no-check-certificate https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/7.4.1/freesurfer-linux-ubuntu22_amd64-7.4.1.tar.gz -O fs.tar.gz && \
    tar --no-same-owner -xzvf fs.tar.gz && \
    mv freesurfer /usr/local && \
    rm fs.tar.gz

ENV PATH=/usr/local/freesurfer/bin:/usr/local/freesurfer/fsfast/bin:/usr/local/freesurfer/tktools:/usr/local/freesurfer/mni/bin:${PATH} \
    OS=Linux \
    FREESURFER_HOME=/usr/local/freesurfer \
    FREESURFER=/usr/local/freesurfer \
    SUBJECTS_DIR=/usr/local/freesurfer/subjects \
    LOCAL_DIR=/usr/local/freesurfer/local \
    FSFAST_HOME=/usr/local/freesurfer/fsfast \
    FMRI_ANALYSIS_DIR=/usr/local/freesurfer/fsfast \
    FUNCTIONALS_DIR=/usr/local/freesurfer/sessions \
    FS_OVERRIDE=0 \
    FIX_VERTEX_AREA= \
    FSF_OUTPUT_FORMAT=nii.gz \
    MINC_BIN_DIR=/usr/local/freesurfer/mni/bin \
    MINC_LIB_DIR=/usr/local/freesurfer/mni/lib \
    MNI_DIR=/usr/local/freesurfer/mni \
    MNI_DATAPATH=/usr/local/freesurfer/mni/data \
    MNI_PERL5LIB=/usr/local/freesurfer/mni/share/perl5 \
    PERL5LIB=/usr/local/freesurfer/mni/share/perl5

# Create non-root user
RUN useradd -m -s /bin/bash freesurfer

# Set ownership of FreeSurfer directory
# RUN chown -R freesurfer:freesurfer /usr/local/freesurfer

# Switch to non-root user
USER freesurfer

# Set working directory
WORKDIR /home/freesurfer
    
CMD ["/bin/bash"]


