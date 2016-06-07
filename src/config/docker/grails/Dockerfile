FROM java:8
MAINTAINER  Fish, Wu

RUN mkdir /app
COPY se3502-0.1.war /app
WORKDIR /app
CMD ["java", "-Dgrails.env=prod", "-jar", "se3502-0.1.war"]