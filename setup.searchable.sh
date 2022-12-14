#!/bin/bash
DIRS=("BCCP"     "CP"       "CPPD"     "EPA"      "FWS.GOV"  "HOA"      "HoaLAWYER" "TBPE" "TXDOT"   "WILCO")
rm -rf ./_as_text_
for dir in ${DIRS[@]};
do
    cd _with_/$dir
    exec $(python3 ../../parse.py)
    cd ../../
    mkdir -p _as_text_/$dir/
    mv _with_/$dir/*.txt _as_text_/$dir/

    rm cscope.* tags || true; find . -type f -name \*.txt -exec echo \"{}\" \; > cscope.files
    cat cscope.files | xargs cscope -b
done
