FROM nginx:stable

# Remove any existing config files
RUN rm /etc/nginx/conf.d/*

# Copy config files
# *.conf files in "conf.d/" dir get included in main config
COPY ./nginx.conf /etc/nginx/conf.d/