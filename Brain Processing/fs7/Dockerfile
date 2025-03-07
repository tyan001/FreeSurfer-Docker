FROM ubuntu:jammy

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    LANG=en_GB.UTF-8 \
    FSLDIR=/usr/local/fsl \
    FSLOUTPUTTYPE=NIFTI_GZ \
    FREESURFER_HOME=/usr/local/freesurfer \
    SUBJECTS_DIR=/usr/local/freesurfer/subjects \
    PATH=/usr/local/freesurfer/bin:/usr/local/freesurfer/fsfast/bin:/usr/local/fsl/bin:${PATH} \
    OS=Linux \
    FSF_OUTPUT_FORMAT=nii.gz

# Install minimal dependencies for both FSL and FreeSurfer
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        bc \
        libgomp1 \
        perl \
        tcsh \
        wget \
        python3 \
        python3-pip \
        libgl1-mesa-glx \
        libxext6 \
        libsm6 \
        libxrender1 \
        libxmu6 \
        file \
        dc \
        unzip \
        tar \
        procps \
        ca-certificates \
        curl \
        nvidia-cuda-toolkit && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install FSL with minimal components and clean up
RUN wget -q https://fsl.fmrib.ox.ac.uk/fsldownloads/fslconda/releases/fslinstaller.py && \
    python3 ./fslinstaller.py -d ${FSLDIR} -o && \
    rm fslinstaller.py && \
    # Remove unnecessary FSL components
    rm -rf ${FSLDIR}/doc \
           ${FSLDIR}/data/atlases \
           ${FSLDIR}/data/first \
           ${FSLDIR}/data/standard/tissuepriors \
           ${FSLDIR}/fslpython/envs/fslpython/pkgs/*.tar.bz2 \
           ${FSLDIR}/src \
           ${FSLDIR}/extras \
           ${FSLDIR}/bin/fslview* \
           ${FSLDIR}/bin/Fsl*

# Install FreeSurfer and clean up
RUN wget -q --no-check-certificate https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/7.4.1/freesurfer-linux-ubuntu22_amd64-7.4.1.tar.gz -O fs.tar.gz && \
    tar --no-same-owner -xzf fs.tar.gz && \
    mv freesurfer ${FREESURFER_HOME} && \
    rm fs.tar.gz && \
    # Remove unnecessary FreeSurfer components while preserving MATLAB and CUDA libraries
    rm -rf ${FREESURFER_HOME}/average/mult-comp-cor \
           ${FREESURFER_HOME}/subjects/fsaverage_sym \
           ${FREESURFER_HOME}/subjects/cvs_avg35 \
           ${FREESURFER_HOME}/subjects/cvs_avg35_inMNI152 \
           ${FREESURFER_HOME}/subjects/fsaverage3 \
           ${FREESURFER_HOME}/subjects/fsaverage4 \
           ${FREESURFER_HOME}/subjects/fsaverage5 \
           ${FREESURFER_HOME}/subjects/fsaverage6 \
           ${FREESURFER_HOME}/trctrain \
           ${FREESURFER_HOME}/diffusion \
           ${FREESURFER_HOME}/docs \
           ${FREESURFER_HOME}/lib/qt

# Install FreeSurfer MCR and clean up
RUN ${FREESURFER_HOME}/bin/fs_install_mcr R2019b && \
    rm -rf /tmp/* /var/tmp/*

# # Create a non-root user with sudo privileges
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends sudo && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/* && \
#     useradd -m fsuser && \
#     echo "fsuser ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/fsuser && \
#     chmod 0440 /etc/sudoers.d/fsuser

# # Set appropriate permissions for workspace and FreeSurfer/FSL directories
RUN mkdir -p /workspace
# RUN mkdir -p /workspace && \
#     chown -R fsuser:fsuser /workspace && \
#     chmod -R 775 /workspace && \
#     chown -R fsuser:fsuser ${FREESURFER_HOME} && \
#     chown -R fsuser:fsuser ${FSLDIR}

# Copy FreeSurfer scripts
# COPY --chown=fsuser:fsuser recon_all.py /workspace
# COPY --chown=fsuser:fsuser hippocampus.py /workspace
COPY mri_processing.py /workspace

# If you want the license file to be copied to the container, uncomment the line below.
# COPY --chown=fsuser:fsuser license.txt ${FREESURFER_HOME}/.license

# Set working directory
WORKDIR /workspace

# Switch to non-root user
USER fsuser

# Set the default command
CMD ["/bin/bash"]