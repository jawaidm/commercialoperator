FROM ubuntu:18.04 as builder_base_cols
MAINTAINER asi@dbca.wa.gov.au
ENV DEBIAN_FRONTEND=noninteractive
ENV DEBUG=True
ENV TZ=Australia/Perth
ENV EMAIL_HOST="smtp.corporateict.domain"
ENV DEFAULT_COLS_EMAIL='cols@dbca.wa.gov.au'
ENV DEFAULT_FROM_EMAIL='no-reply@dbca.wa.gov.au'
ENV NOTIFICATION_EMAIL='jawaid.mushtaq@dbca.wa.gov.au'
ENV NON_PROD_EMAIL='jawaid.mushtaq@dbca.wa.gov.au'
ENV PRODUCTION_EMAIL=False
ENV EMAIL_INSTANCE='DEV'
ENV SECRET_KEY="ThisisNotRealKey"
ENV SITE_PREFIX='cols-dev'
ENV SITE_DOMAIN='dbca.wa.gov.au'
ENV OSCAR_SHOP_NAME='Parks & Wildlife'
ENV BPAY_ALLOWED=False
ENV DISABLE_EMAIL=False
RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -yq git mercurial gcc gdal-bin libsasl2-dev libpq-dev \
  python python-setuptools python-dev python-pip \
  imagemagick poppler-utils \
  libldap2-dev libssl-dev wget build-essential \
  libmagic-dev binutils libproj-dev tzdata
RUN pip install --upgrade pip
#RUN apt-get install -yq vim

# Install Python libs from requirements.txt.
FROM builder_base_cols as python_libs_cols
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
  # Update the Django <1.11 bug in django/contrib/gis/geos/libgeos.py
  # Reference: https://stackoverflow.com/questions/18643998/geodjango-geosexception-error
  && sed -i -e "s/ver = geos_version().decode()/ver = geos_version().decode().split(' ')[0]/" /usr/local/lib/python2.7/dist-packages/django/contrib/gis/geos/libgeos.py \
  && rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*


# Install the project (ensure that frontend projects have been built prior to this step).
FROM python_libs_cols
COPY gunicorn.ini manage_co.py ./
RUN touch /app/.env
COPY .git ./.git
#COPY ledger ./ledger
COPY commercialoperator ./commercialoperator
RUN python manage_co.py collectstatic --noinput
EXPOSE 8080
HEALTHCHECK --interval=1m --timeout=5s --start-period=10s --retries=3 CMD ["wget", "-q", "-O", "-", "http://localhost:8080/"]
CMD ["gunicorn", "commercialoperator.wsgi", "--bind", ":8080", "--config", "gunicorn.ini"]


