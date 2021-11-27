FROM node:14.17.0 as base

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

ENV FIREBASE_URL ${FIREBASE_URL}
ENV AUTH_URL ${AUTH_URL}
ENV AUTH_API_KEY ${AUTH_API_KEY}
ENV API_URL_BROWSER ${API_URL_BROWSER}

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