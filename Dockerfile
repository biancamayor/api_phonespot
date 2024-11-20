FROM python:3.11

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["uvicorn", "main:api"]
ENTRYPOINT ["sh", "-c", "if [ \"$RUN_STREAMLIT\" = \"1\" ]; then streamlit run streamlit/main.py; else uvicorn main:api; fi"]