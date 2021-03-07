FROM node:14.4.0 as base

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