# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=jupyter/minimal-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Saulius Lukauskas <https://github.com/lukauskas>"

USER root

# ffmpeg for matplotlib anim & dvipng+cm-super for latex labels
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    bedtools \
    cm-super \
    dvipng \
    ffmpeg \
    fonts-dejavu \
    gcc \
    gfortran \
    r-cran-rodbc \
    unixodbc \
    unixodbc-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Fix for devtools https://github.com/conda-forge/r-devtools-feedstock/issues/4
RUN ln -s /bin/tar /bin/gtar

USER $NB_UID

# Scipy notebook
RUN conda install --quiet --yes \
    'beautifulsoup4=4.9.*' \
    'conda-forge::blas=*=openblas' \
    'bokeh=2.2.*' \
    'bottleneck=1.3.*' \
    'cloudpickle=1.6.*' \
    'cython=0.29.*' \
    'dask=2.30.*' \
    'dill=0.3.*' \
    'h5py=2.10.*' \
    'ipywidgets=7.5.*' \
    'ipympl=0.5.*'\
    'matplotlib-base=3.3.*' \
    'numba=0.51.*' \
    'numexpr=2.7.*' \
    'pandas=1.1.*' \
    'patsy=0.5.*' \
    'protobuf=3.13.*' \
    'pytables=3.6.*' \
    'scikit-image=0.17.*' \
    'scikit-learn=0.23.*' \
    'scipy=1.5.*' \
    'seaborn=0.11.*' \
    'sqlalchemy=1.3.*' \
    'statsmodels=0.12.*' \
    'sympy=1.6.*' \
    'vincent=0.4.*' \
    'widgetsnbextension=3.5.*'\
    'xlrd=1.2.*' \
    && conda clean --all -f -y \
    && fix-permissions "${CONDA_DIR}"

# R-notebook
RUN conda install --quiet --yes \
        'r-base=4.0.3' \
        'r-caret=6.*' \
        'r-crayon=1.3*' \
        'r-devtools=2.3*' \
        'r-forecast=8.13*' \
        'r-hexbin=1.28*' \
        'r-htmltools=0.5*' \
        'r-htmlwidgets=1.5*' \
        'r-irkernel=1.1*' \
        'r-nycflights13=1.0*' \
        'r-randomforest=4.6*' \
        'r-rcurl=1.98*' \
        'r-rmarkdown=2.5*' \
        'r-rodbc=1.3*' \
        'r-rsqlite=2.2*' \
        'r-shiny=1.5*' \
        'r-tidyverse=1.3*' \
        'unixodbc=2.3.*' \
        'r-tidymodels=0.1*' \
        && conda clean --all -f -y \
        && fix-permissions "${CONDA_DIR}"

# Install e1071 R package (dependency of the caret R package)
RUN conda install --quiet --yes r-e1071

# 'bashtage::arch=4.15.*' \
# 'bioconda::bioconductor-clusterprofiler=3.8.*' \
# 'bioconda::bioconductor-deseq2=1.30.*' \
# 'bioconda::bioconductor-edger=3.32.*' \
# 'conda-forge::feather-format==0.4.*' \
# 'conda-forge::karateclub=1.0.*' \
# 'conda-forge::pygsp=0.5.*' \
# 'bioconda::bioconductor-limma=3.46.*' \
# 'bioconda::pybedtools=0.8.*' \
# 'conda-forge::palettable=3.3.*' \
# 'r-cowplot=0.9.*' \
# 'r-feather=0.3.*' \
# 'bioconda::r-ggrepel=0.6.*' \
# 'r-pheatmap=1.0.*'\
# 'r-rcolorbrewer=1.*' \
# 'statsmodels=0.12.*' \
# 'conda-forge::pingouin=0.3.*' \
# 'bioconda::snakemake=5.3.*' \
# 'bioconda::bioconductor-tximport==1.18.*' \

# Bioinformatics stuff
# Install Python 3 packages


# 'bashtage::arch=4.15.*' \
# 'bioconda::bioconductor-clusterprofiler=3.8.*' \
# 'bioconda::bioconductor-deseq2=1.30.*' \
# 'bioconda::bioconductor-edger=3.32.*' \
# 'conda-forge::feather-format=0.4.*' \
# 'conda-forge::karateclub=1.0.*' \
# 'conda-forge::pygsp=0.5.*' \
# 'bioconda::bioconductor-limma=3.46.*' \
# 'bioconda::pybedtools=0.8.*' \
# 'conda-forge::palettable=3.3.*' \
# 'r-cowplot=0.9.*' \
# 'r-feather=0.3.*' \
# 'bioconda::r-ggrepel=0.6.*' \
# 'r-pheatmap=1.0.*'\
# 'r-rcolorbrewer=1.*' \
# 'statsmodels=0.12.*' \
# 'conda-forge::pingouin=0.3.*' \
# 'bioconda::snakemake=5.3.*' \
# 'bioconda::bioconductor-tximport=1.18.*' \

RUN conda config --add channels conda-forge \
    && conda config --add channels bioconda \
    && conda config --set channel_priority strict \
    && conda install --quiet --yes \
    'bashtage::arch' \
    'bioconda::bioconductor-clusterprofiler' \
    'bioconda::bioconductor-deseq2' \
    'bioconda::bioconductor-edger' \
    'conda-forge::feather-format' \
    'conda-forge::karateclub' \
    'conda-forge::pygsp' \
    'bioconda::bioconductor-limma' \
    'bioconda::pybedtools' \
    'conda-forge::palettable' \
    'r-cowplot' \
    'r-feather' \
    'bioconda::r-ggrepel' \
    'r-pheatmap'\
    'r-rcolorbrewer' \
    'statsmodels' \
    'conda-forge::pingouin' \
    'bioconda::snakemake' \
    'bioconda::bioconductor-tximport' \
    && conda clean --all -f -y \
    && fix-permissions "${CONDA_DIR}"

# Jupyter extensions
RUN jupyter nbextension enable --py widgetsnbextension --sys-prefix && \
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
    fix-permissions "/home/${NB_USER}"



# Install facets which does not have a pip or conda package at the moment
WORKDIR /tmp
RUN git clone https://github.com/PAIR-code/facets.git && \
    jupyter nbextension install facets/facets-dist/ --sys-prefix && \
    rm -rf /tmp/facets && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME="/home/${NB_USER}/.cache/"

RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \
    fix-permissions "/home/${NB_USER}"

USER $NB_UID

WORKDIR $HOME
