FROM python
WORKDIR /app
COPY . /app
COPY paragraphs.txt /app/
 # Copy the paragraph.txt file into the /app/ directory
RUN pip install nltk
CMD ["python3","app.py"]