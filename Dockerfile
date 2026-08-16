# Site estático do Tapi (docs/) servido por nginx.
# Sem build step: docs/ é HTML/CSS/JS puro.
FROM nginx:1.27-alpine

COPY infra/nginx.conf /etc/nginx/conf.d/default.conf
COPY docs/ /usr/share/nginx/html/

# CNAME é artefato do GitHub Pages; não serve dentro do container.
RUN rm -f /usr/share/nginx/html/CNAME

EXPOSE 80
