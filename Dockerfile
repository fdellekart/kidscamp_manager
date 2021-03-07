FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /app
COPY ./backend .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0" ,"--port", "80"]
