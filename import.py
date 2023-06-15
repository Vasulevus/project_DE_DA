import pandas
import numpy


csv = pandas.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSKB0ufDrMisLON7WX023JBDTHnG0-ZXRJA6RLJSRV9iOnDA5IlHOYGavPwmpeIoenB3jhE-nxDRQth/pub?gid=2072565988&single=true&output=csv")
df = pandas.DataFrame(csv)
df.head()

