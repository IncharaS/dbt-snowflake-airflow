FROM quay.io/astronomer/ap-airflow:2.4.3-onbuild

WORKDIR "/home/incs/AirflowHome"

COPY requirements.txt ./

# Install DBT and dependencies in a virtual environment
RUN python -m virtualenv /home/incs/dbt_venv && \
    /home/incs/dbt_venv/bin/pip install --no-cache-dir dbt-snowflake

# Ensure proper permissions for the virtual environment
RUN chown -R astro:astro /home/incs/dbt_venv

# Set the virtual environment in the PATH for runtime access
ENV PATH="/home/incs/dbt_venv/bin:$PATH"

# Switch back to Airflow user
USER airflow
