# This started as an attempt to emulate the `jupyter/scipy-notebook` adding R and
# python dependencies but but I quickly gave up because of its use of `conda`

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=lukauskas/noconda-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Saulius Lukauskas <https://github.com/lukauskas>"

USER root

# Install new version of R first
# Based on https://cran.r-project.org/bin/linux/debian/#debian-buster-stable
#And on https://github.com/rocker-org/rocker/blob/master/r-base/4.0.3/Dockerfile
RUN apt-key adv --keyserver keys.gnupg.net --recv-key 'E19F5F87128899B192B1A2C2AD5F960A256A04AF' \
    && echo "deb http://cloud.r-project.org/bin/linux/debian buster-cran40/" >> /etc/apt/sources.list \
    && echo 'APT::Install-Recommends "false";' > /etc/apt/apt.conf.d/90local-no-recommends

## Now install R and littler, and create a link for littler in /usr/local/bin
RUN apt-get update \
    && apt-get install -y --no-install-recommends -t buster-cran40 r-base \
    && apt-get install -y --no-install-recommends \
		littler \
        r-cran-littler \
		r-recommended \
	&& ln -s /usr/lib/R/site-library/littler/examples/install.r /usr/local/bin/install.r \
	&& ln -s /usr/lib/R/site-library/littler/examples/install2.r /usr/local/bin/install2.r \
	&& ln -s /usr/lib/R/site-library/littler/examples/installBioc.r /usr/local/bin/installBioc.r \
	&& ln -s /usr/lib/R/site-library/littler/examples/installDeps.r /usr/local/bin/installDeps.r \
	&& ln -s /usr/lib/R/site-library/littler/examples/installGithub.r /usr/local/bin/installGithub.r \
	&& ln -s /usr/lib/R/site-library/littler/examples/testInstalled.r /usr/local/bin/testInstalled.r \
	&& install.r docopt \
	&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
	&& rm -rf /var/lib/apt/lists/*

# Other apt-get dependancies
RUN apt-get update -qq && apt-get -y --no-install-recommends install \
  bedtools \
  cm-super \
  libcurl4-openssl-dev \
  dvipng \
  ffmpeg \
  fonts-dejavu \
  gcc \
  gfortran \
  libxml2-dev \
  libcairo2-dev \
  libfreetype6-dev \
  libgit2-dev \
  libpng-dev \
  libtiff5-dev \
  libjpeg-dev \
  libfribidi-dev \
  libharfbuzz-dev \
  libsqlite-dev \
  libmariadbd-dev \
  libmariadbclient-dev \
  libopenblas-base \
  libopenblas-dev \
  libpq-dev \
  libsasl2-dev \
  libssl-dev \
  libssh2-1-dev \
  libxt-dev \
  samtools \
  unixodbc \
  unixodbc-dev \
  zlib1g-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

#  R Packages
RUN install2.r --error \
    --deps TRUE \
    tidyverse \
    dplyr \
    devtools \
    formatR \
    ggrepel \
    remotes \
    selectr \
    caTools \
    caret \
    crayon \
    forecast \
    htmltools \
    htmlwidgets \
    IRkernel \
    pheatmap \
    randomForest \
    rmarkdown \
    RCurl \
    RODBC \
    RSQLite \
    shiny \
    tidymodels \
    ## Somehow the BioCManager needs to be installed without deps
    ## As it creates an unsatisfiable constraint
    && install2.r --error \
        BiocManager \
    ## Require Bioconductor packages
    && R -e "BiocManager::install()" \
    && R -e "BiocManager::install('affy')" \
    && R -e "BiocManager::install('Biobase')" \
    && R -e "BiocManager::install('BiocStyle')" \
    && R -e "BiocManager::install('BiocVersion')" \
    && R -e "BiocManager::install('clusterProfiler')" \
    && R -e "BiocManager::install('DESeq2')" \
    && R -e "BiocManager::install('DOSE')" \
    && R -e "BiocManager::install('edgeR')" \
    && R -e "BiocManager::install('fgsea')" \
    && R -e "BiocManager::install('GOSemSim')" \
    && R -e "BiocManager::install('limma')" \
    && R -e "BiocManager::install('tximport')" \
    && R -e "BiocManager::install('marray')" \
    && R -e "BiocManager::install('rtracklayer')" \
    && R -e "BiocManager::install('Rsamtools')" \
    # Packages that depend on Bioconductor
    && install2.r --error --deps TRUE \
    hexbin

USER $NB_UID

# Python packages & jupyter extensions
RUN pip install --no-cache-dir \
    'adjustText==0.7.3' \
    'arch==4.19' \
    'bokeh==2.3.0' \
    'bottleneck==1.3.2' \
    'cloudpickle==1.6.0' \
    'cython==0.29.22' \
    'dask==2021.4.0' \
    'dill==0.3.3' \
    'h5py==3.2.1' \
    'ipywidgets==7.6.3' \
    'ipympl==0.7.0'\
    'matplotlib==3.4.1' \
    'matplotlib-venn==0.11.6' \
    'networkx==2.5.1' \
    'numba==0.53.1' \
    'numexpr==2.7.3' \
    'nteract-scrapbook==0.4.2' \
    'pandas==1.2.3' \
    'papermill==2.3.3' \
    'patsy==0.5.1' \
    'pingouin==0.3.10' \
    'protobuf==3.15.7' \
    'pyBigWig==0.3.18' \
    'pybedtools==0.8.2' \
    'pysam==0.16.0.1' \
    'sinfo==0.3.1' \
    'tables==3.6.1' \
    'scikit-image==0.18.1' \
    'scikit-learn==0.24.1' \
    'scipy==1.6.2' \
    'seaborn==0.11.1' \
    'sqlalchemy==1.4.5' \
    'statsmodels==0.12.2' \
    'statannot==0.2.3' \
    'sympy==1.7.1' \
    'tqdm==4.60.0' \
    'vincent==0.4.4' \
    'widgetsnbextension==3.5.1'\
    'xlrd==2.0.1' \
 && jupyter nbextension enable --py widgetsnbextension && \
    # Also activate ipywidgets extension for JupyterLab
    # Check this URL for most recent compatibilities
    # https://github.com/jupyter-widgets/ipywidgets/tree/master/packages/jupyterlab-manager
    jupyter labextension install @jupyter-widgets/jupyterlab-manager@^2.0.0 --no-build && \
    jupyter labextension install @bokeh/jupyter_bokeh@^2.0.0 --no-build && \
    jupyter labextension install jupyter-matplotlib@^0.7.2 --no-build && \
    jupyter lab build -y && \
    jupyter lab clean -y && \
    npm cache clean --force && \
    rm -rf "/home/${NB_USER}/.cache/yarn" && \
    rm -rf "/home/${NB_USER}/.node-gyp" && \
    rm -rf "/home/${NB_USER}/.cache/pip" && \
    fix-permissions "/home/${NB_USER}"

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME="/home/${NB_USER}/.cache/"

RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \
    fix-permissions "/home/${NB_USER}"

USER $NB_UID

WORKDIR $HOME
