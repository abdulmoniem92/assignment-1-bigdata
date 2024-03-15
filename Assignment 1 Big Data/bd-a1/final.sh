#!/bin/bash

echo mkdir ~/bd-a1/service-result/

echo docker cp bd-a1:/home/doc-bd-a1/dpre_output.txt ~/bd-a1/service-result/dpre_output.txt
echo docker cp bd-a1:/home/doc-bd-a1/eda_output.txt ~/bd-a1/service-result/eda_output.txt
echo docker cp bd-a1:/home/doc-bd-a1/vis_output.txt ~/bd-a1/service-result/vis_output.txt
echo docker cp bd-a1:/home/doc-bd-a1/model_output.txt ~/bd-a1/service-result/model_output.txt

echo docker stop bd-a1
