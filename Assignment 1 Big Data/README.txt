Assignment 1 Commands

### In your local terminal

cd bd-a1
docker build -t bd-a1 .
docker run -it bd-a1

### Within the docker container ###

python3 load.py dataset.csv
python3 dpre.py
python3 eda.py
python3 vis.py
python3 model.py

### Return to local terminal

chmod +x final.sh
.final.sh
