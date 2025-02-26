FROM ubuntu:jammy

# Set environment variables for both FreeSurfer and FSL
ENV DEBIAN_FRONTEND=noninteractive \
    LANG=en_GB.UTF-8 \
    FSLDIR=/usr/local/fsl \
    FSLOUTPUTTYPE=NIFTI_GZ

# Install common dependencies for both FreeSurfer and FSL
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
        gfortran \
        file \
        dc \
        mesa-utils \
        pulseaudio \
        libquadmath0 \
        libgtk2.0-0 \
        firefox \
        libosmesa6 \
        libosmesa6-dev \
        libgl1-mesa-dev \
        libglu1-mesa-dev \
        xvfb \
        sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install FSL
RUN wget https://fsl.fmrib.ox.ac.uk/fsldownloads/fslconda/releases/fslinstaller.py && \
    python3 ./fslinstaller.py -d /usr/local/fsl/ && \
    rm fslinstaller.py

# Install FreeSurfer
RUN wget --progress=bar:force:noscroll --no-check-certificate https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/7.4.1/freesurfer-linux-ubuntu22_amd64-7.4.1.tar.gz -O fs.tar.gz && \
    tar --no-same-owner -xzvf fs.tar.gz && \
    mv freesurfer /usr/local && \
    rm fs.tar.gz

# Set FreeSurfer environment variables
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

# Install FreeSurfer MCR
RUN fs_install_mcr R2019b

# Update PATH to include both FSL and FreeSurfer
ENV PATH=$FSLDIR/bin:$PATH

# Create a non-root user with sudo privileges
RUN useradd -m fsuser && \
    echo "fsuser ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/fsuser && \
    chmod 0440 /etc/sudoers.d/fsuser

# Set appropriate permissions for workspace and FreeSurfer/FSL directories
RUN mkdir -p /workspace && \
    chown -R fsuser:fsuser /workspace && \
    chmod -R 775 /workspace && \
    chown -R fsuser:fsuser /usr/local/freesurfer && \
    chown -R fsuser:fsuser /usr/local/fsl

# Copy FreeSurfer scripts
# COPY --chown=fsuser:fsuser recon_all.py /workspace
# COPY --chown=fsuser:fsuser hippocampus.py /workspace
COPY --chown=fsuser:fsuser mri_processing.py /workspace

# If you want the license file to be copied to the container, uncomment the line below.
# COPY --chown=fsuser:fsuser license.txt /usr/local/freesurfer/.license

# Set working directory
WORKDIR /workspace

# Switch to non-root user
USER fsuser

# Set the entrypoint to bash
CMD ["/bin/bash"]