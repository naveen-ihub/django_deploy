FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Pushing images
# You can push a new image to this repository using the CLI:

# docker tag local-image:tagname new-repo:tagname
# docker push new-repo:tagname
# Make sure to replace tagname with your desired image repository tag.