FROM node:22.14.0 as base

# Set working directory to /app
WORKDIR /app
RUN chown node:node .

# setup entry point
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

USER node

# Install requirements
COPY --chown=node:node package.json .
COPY --chown=node:node yarn.lock .
RUN yarn install --non-interactive --audit

# Copy all files (note .dockerignore)
COPY --chown=node:node . .

# set app serving to permissive / assigned
ENV NUXT_HOST=0.0.0.0

ARG FIREBASE_URL
ARG AUTH_URL
ARG AUTH_API_KEY
ARG API_URL_BROWSER
ARG CONFIRMATION_MAIL
ARG CONFIRMATION_MAIL_PASSWORD
ARG FIREBASE_AUTH_DOMAIN
ARG FIREBASE_PROJECT_ID
ARG FIREBASE_STORAGE_BUCKET
ARG FIREBASE_MESSAGING_SENDER_ID
ARG FIREBASE_APP_ID
ARG FIREBASE_USER
ARG FIREBASE_PW

ENV FIREBASE_URL ${FIREBASE_URL}
ENV AUTH_URL ${AUTH_URL}
ENV AUTH_API_KEY ${AUTH_API_KEY}
ENV API_URL_BROWSER ${API_URL_BROWSER}
ENV CONFIRMATION_MAIL ${CONFIRMATION_MAIL}
ENV CONFIRMATION_MAIL_PASSWORD ${CONFIRMATION_MAIL_PASSWORD}
ENV FIREBASE_AUTH_DOMAIN ${FIREBASE_AUTH_DOMAIN}
ENV FIREBASE_PROJECT_ID ${FIREBASE_PROJECT_ID}
ENV FIREBASE_STORAGE_BUCKET ${FIREBASE_STORAGE_BUCKET}
ENV FIREBASE_MESSAGING_SENDER_ID ${FIREBASE_MESSAGING_SENDER_ID}
ENV FIREBASE_APP_ID ${FIREBASE_APP_ID}
ENV FIREBASE_USER ${FIREBASE_USER}
ENV FIREBASE_PW ${FIREBASE_PW}


# expect the commit hash to be passed at build-time
ARG CI_COMMIT_SHORT_SHA
# add it to the image to pass it to the container at runtime
ENV CI_COMMIT_SHORT_SHA $CI_COMMIT_SHORT_SHA

# Build app (minify JS & CSS)
RUN yarn build

EXPOSE 3000

ENTRYPOINT ["docker-entrypoint.sh"]

# arguments to docker-entrypoint.sh
CMD ["entry"]