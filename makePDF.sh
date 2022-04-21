pdfjam --a4paper --fitpaper true pics/trainset_WF_*.png
rm -rf pics/trainset_WF_*.png
mv trainset_WF_*.png-pdfjam.pdf pics/
mv pics/trainset_WF_*.png-pdfjam.pdf pics/trainset_WF.pdf