# Build a static version in a separate image
FROM node:slim as builder
WORKDIR /usr/src/app
# Install NodeJS requirements
ADD frontend/package* ./
RUN npm install
# Create static version
ADD frontend/src ./src
ADD frontend/public ./public
RUN npm run build


FROM nginx
WORKDIR /usr/src/app
# Copy pre-built static version
COPY --from=builder /usr/src/app/build ./build
# Copy nginx configuration
ADD provision/nginx_default /etc/nginx/conf.d/default.conf
