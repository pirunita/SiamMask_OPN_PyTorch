### Edit parameter ###
DATA_NAME="hollywood"
VIDEO_SCALE_FACTOR=0.25
PADDING_FACTOR=0.05
OPN_DILATE_FACTOR=3
OPN_SCALE_FACTOR=0.5

######################
DATA_PATH="data/${DATA_NAME}"
ROOT_PATH="results/"
RESULT_PATH="${ROOT_PATH}${DATA_NAME}/"
MASK_PATH="${RESULT_PATH}masks/"
MASK_PATH2="${RESULT_PATH}masks2/"
SAVE_PATH="${RESULT_PATH}final/"

echo "Data name: ${DATA_NAME}, Data path: ${DATA_PATH}, Result path: ${RESULT_PATH} \n"
echo "Mask path: ${MASK_PATH}, Save path: ${SAVE_PATH}"

python video_preprocess.py --base_path ${DATA_PATH} --f ${VIDEO_SCALE_FACTOR}
python siammask.py --base_path ${DATA_PATH} \
                   --root_path ${ROOT_PATH} \
                   --result_path ${RESULT_PATH} \
                   --mask_path ${MASK_PATH} \
                   --padding_factor ${PADDING_FACTOR}
python opn.py --base_path ${DATA_PATH} \
              --root_path ${ROOT_PATH} \
              --result_path ${RESULT_PATH} \
              --mask_path ${MASK_PATH} \
              --mask_path2 ${MASK_PATH2} \
              --save_path ${SAVE_PATH} \
              --dilate_factor ${OPN_DILATE_FACTOR} \
              --scale_factor ${OPN_SCALE_FACTOR} \
              
python make_gif.py --base_path ${DATA_PATH} \
                   --root_path ${ROOT_PATH} \
                   --result_path ${RESULT_PATH} \
                   --mask_path ${MASK_PATH} \
                   --mask_path2 ${MASK_PATH2} \
                   --save_path ${SAVE_PATH} \