FROM ubuntu/freesurfer:7.4.1

# This is an extension to the base image that includes the hippocampus segmentation from FreeSurfer 7.4.1.
# You would need to first build the base image and give it the name ubuntu/freesurfer with tag 7.4.1. 
# Doing it this way lets you save space instead of having one container image for just FS7 and one container with FS7+hippocampus.
# You can also just opt to create a Dockerfile that install both components already. I just did it this way in case people want a choice.
# If you want to change the name just change the "FROM ubuntu/freesurfer:7.4.1

RUN fs_install_mcr R2019b

CMD ["/bin/bash"]