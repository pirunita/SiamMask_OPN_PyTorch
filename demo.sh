DATA_PATH="data/tennis"

python siammask.py --base_path ${DATA_PATH}
python opn.py --base_path ${DATA_PATH}
python make_gif.py