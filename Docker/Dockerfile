FROM argnctu/oop:latest

ARG DISPLAY
ENV DISPLAY=${DISPLAY}
ENV QT_X11_NO_MITSHM=1
ENV XAUTHORITY=/tmp/.docker.xauth

WORKDIR /home/arg/oop-proj-survive

COPY . .

USER root

RUN chmod +x require.sh && ./require.sh
# RUN chmod 777 /tmp/.X11-unix
CMD ["bash"]
