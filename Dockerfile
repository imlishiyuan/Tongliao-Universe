FROM nginx:mainline-alpine3.18-slim
COPY ./dist /usr/share/nginx/html

